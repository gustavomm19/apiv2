from capyc.rest_framework.exceptions import ValidationException
from django.conf import settings
from rest_framework import serializers

from breathecode.admissions.models import Academy
from breathecode.authenticate.serializers import GetSmallAcademySerializer
from breathecode.utils import serpy

from .models import Hook


class UserSerializer(serpy.Serializer):
    id = serpy.Field()
    first_name = serpy.Field()
    last_name = serpy.Field()


class DeviceSerializer(serpy.Serializer):
    id = serpy.Field()
    registration_id = serpy.Field()
    created_at = serpy.Field()


class HookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hook
        read_only_fields = ("user",)
        exclude = ["sample_data"]

    def validate(self, data):

        if data["event"] not in settings.HOOK_EVENTS:
            err_msg = "Unexpected event {}".format(data["event"])
            raise ValidationException(err_msg, slug="invalid-event")

        # superadmins can subscribe to any hook without needed an academy token
        if not self.context["request"].user.is_superuser:
            academy = Academy.objects.filter(slug=self.context["request"].user.username).first()
            if academy is None:
                raise ValidationException("No valid academy token found", slug="invalid-academy-token")

        data["user"] = self.context["request"].user

        return super().validate(data)


class SlackTeamSerializer(serpy.Serializer):
    id = serpy.Field()
    slack_id = serpy.Field()
    name = serpy.Field()
    academy = GetSmallAcademySerializer(required=False)
    created_at = serpy.Field()
    sync_status = serpy.Field()
    sync_message = serpy.Field()


class NotificationSerializer(serpy.Serializer):
    id = serpy.Field()
    message = serpy.Field()
    status = serpy.Field()
    type = serpy.Field()
    academy = GetSmallAcademySerializer(required=False)
    meta = serpy.Field()
    sent_at = serpy.Field()
    done_at = serpy.Field()
    seen_at = serpy.Field()
