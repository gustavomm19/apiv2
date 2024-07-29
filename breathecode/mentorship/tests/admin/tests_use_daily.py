"""
Test mentorships
"""

import pytest

from breathecode.mentorship.admin import use_daily
from capyc.rest_framework import pytest as capy


@pytest.mark.fixture(autouse=True)
def setup(db):
    yield


@pytest.mark.parametrize("model_path", ["mentorship.MentorshipService", "mentorship.AcademyMentorshipSettings"])
def test_no_items(database: capy.Database, model_path: str):
    Model = database.get_model(model_path)
    queryset = Model.objects.filter()

    use_daily(None, None, queryset)

    assert database.list_of(model_path) == []


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.parametrize(
    "model_path, model_name, includes_academy",
    [
        ("mentorship.MentorshipService", "mentorship_service", False),
        ("mentorship.AcademyMentorshipSettings", "academy_mentorship_settings", True),
    ],
)
def test_two_items__changed(
    database: capy.Database, model_path: str, model_name: str, format: capy.Format, includes_academy: bool
):
    extra = {
        "city": 1,
        "country": 1,
    }

    if includes_academy:
        extra["academy"] = (2, {"name": "Test Academy"})
        extra[model_name] = [{"video_provider": "GOOGLE_MEET", "academy_id": n + 1} for n in range(2)]

    else:
        extra[model_name] = (2, {"video_provider": "GOOGLE_MEET"})

    model = database.create(**extra)
    Model = database.get_model(model_path)
    queryset = Model.objects.filter()

    use_daily(None, None, queryset)

    assert database.list_of(model_path) == [
        {
            **format.to_obj_repr(model[model_name][n]),
            "video_provider": "DAILY",
        }
        for n in range(2)
    ]


@pytest.mark.django_db(reset_sequences=True)
@pytest.mark.parametrize(
    "model_path, model_name, includes_academy",
    [
        ("mentorship.MentorshipService", "mentorship_service", False),
        ("mentorship.AcademyMentorshipSettings", "academy_mentorship_settings", True),
    ],
)
def test_two_items__did_not_changed(
    database: capy.Database, model_path: str, model_name: str, format: capy.Format, includes_academy: bool
):
    extra = {
        "city": 1,
        "country": 1,
    }

    if includes_academy:
        extra["academy"] = (2, {"name": "Test Academy"})
        extra[model_name] = [{"video_provider": "DAILY", "academy_id": n + 1} for n in range(2)]

    else:
        extra[model_name] = (2, {"video_provider": "DAILY"})

    model = database.create(**extra)
    Model = database.get_model(model_path)
    queryset = Model.objects.filter()

    use_daily(None, None, queryset)

    assert database.list_of(model_path) == [
        {
            **format.to_obj_repr(model[model_name][n]),
            "video_provider": "DAILY",
        }
        for n in range(2)
    ]
