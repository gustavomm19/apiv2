import os
from io import BytesIO
from typing import Any, Awaitable, Callable, Optional, Type, TypedDict

from adrf.requests import AsyncRequest
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile

from breathecode.media.models import File
from breathecode.services.google_cloud.storage import Storage
from capyc.rest_framework.exceptions import ValidationException


class MediaSettings(TypedDict):
    chunk_size: int
    max_chunks: int
    is_quota_exceeded: Callable[[AsyncRequest, Optional[int]], Awaitable[bool]]
    is_authorized: Callable[[AsyncRequest, Optional[int]], Awaitable[bool]]
    is_mime_supported: Callable[[InMemoryUploadedFile | TemporaryUploadedFile, Optional[int]], Awaitable[bool]]
    schema = Optional[Callable[[dict[str, Any]], dict[str, Callable]]]
    process = Optional[Callable[[File, dict[str, Any], Optional[int]], None]]


MEDIA_MIME_ALLOWED = [
    "image/png",
    "image/svg+xml",
    "image/jpeg",
    "image/gif",
    "video/quicktime",
    "video/mp4",
    "audio/mpeg",
    "application/pdf",
    "image/jpg",
    "application/octet-stream",
]

PROOF_OF_PAYMENT_MIME_ALLOWED = [
    "image/png",
    "image/svg+xml",
    "image/jpeg",
    "image/gif",
    "image/jpg",
]

PROFILE_MIME_ALLOWED = [
    "image/png",
    "image/jpeg",
]


async def allow_any(request: AsyncRequest, academy_id: Optional[int] = None) -> bool:
    return True


async def no_quota_limit(request: AsyncRequest, academy_id: Optional[int] = None) -> bool:
    return False


async def media_is_mime_supported(
    file: InMemoryUploadedFile | TemporaryUploadedFile, academy_id: Optional[int] = None
) -> bool:
    return file.content_type in MEDIA_MIME_ALLOWED


async def proof_of_payment_is_mime_supported(
    file: InMemoryUploadedFile | TemporaryUploadedFile, academy_id: Optional[int] = None
) -> bool:
    return file.content_type in PROOF_OF_PAYMENT_MIME_ALLOWED


async def profile_is_mime_supported(
    file: InMemoryUploadedFile | TemporaryUploadedFile, academy_id: Optional[int] = None
) -> bool:
    return file.content_type in PROFILE_MIME_ALLOWED


async def no_schedule(meta: Any) -> bool:
    return False


async def no_schema(schema: Any) -> None:
    return []


def array(t: Type) -> Any:
    def wrapper(l: list[Any]) -> list[Any]:
        for item in l:
            if not isinstance(item, t):
                raise ValidationException(f"Invalid item type, expected {t.__name__}, got {type(item).__name__}")

    return wrapper


async def media_schema(schema: Any) -> None:
    return {
        "slug": str,
        # "mime": file.content_type,
        "name": str,
        "categories": array(str),
        "academy": int,
    }


def transfer(file: File, new_bucket, suffix=""):
    storage = Storage()
    uploaded_file = storage.file(file.bucket, file.name)
    if uploaded_file.exists() is False:
        raise Exception("File does not exists")

    f = BytesIO()
    uploaded_file.download(f)

    new_file = storage.file(new_bucket, file.hash + suffix)
    new_file.upload(f, content_type=file.mime, public=True)
    url = new_file.url()
    return url


def process_media(file: File, meta: dict[str, Any], academy_id: Optional[int] = None) -> None:
    from .models import Media

    url = transfer(file, os.getenv("MEDIA_GALLERY_BUCKET"))
    Media.objects.create(
        hash=file.hash,
        slug=meta["slug"],
        name=meta["name"] or file.name,
        mime=file.mime,
        categories=meta["categories"] or [],
        academy_id=academy_id,
        url=url,
        thumbnail=url + "-thumbnail",
    )


# def process_profile(file: File, meta: dict[str, Any]) -> None:
#     url = transfer(file, os.getenv("MEDIA_GALLERY_BUCKET"))
#     storage = Storage()
#     cloud_file = storage.file(get_profile_bucket(), hash)
#     cloud_file_thumbnail = storage.file(get_profile_bucket(), f"{hash}-100x100")

#     if thumb_exists := cloud_file_thumbnail.exists():
#         cloud_file_thumbnail_url = cloud_file_thumbnail.url()


MB = 1024 * 1024
CHUNK_SIZE = 10 * MB

# keeps
MEDIA_SETTINGS: dict[str, MediaSettings] = {
    "media": {
        "chunk_size": CHUNK_SIZE,
        "max_chunks": None,
        "is_quota_exceeded": no_quota_limit,
        "is_authorized": allow_any,
        "is_mime_supported": media_is_mime_supported,
        "schema": media_schema,
        "process": process_media,
    },
    "proof-of-payment": {
        "chunk_size": CHUNK_SIZE,
        "max_chunks": None,
        "is_quota_exceeded": no_quota_limit,
        "is_authorized": allow_any,
        "is_mime_supported": proof_of_payment_is_mime_supported,
        "schema": None,
        "process": None,
    },
    # disabled
    # "profile-pictures": {
    #     "chunk_size": CHUNK_SIZE,
    #     "max_chunks": 25,  # because currently it accepts 4K photos
    #     "is_quota_exceeded": no_quota_limit,  # change it in a future
    #     "is_authorized": allow_any,
    #     "is_mime_supported": profile_is_mime_supported,
    #     "schema": no_schema,
    #     "process": process_profile,
    # },
}
