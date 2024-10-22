from django.db.models import QuerySet
from task_manager.core.exceptions import AbortTask

from breathecode.authenticate.models import CredentialsGoogle, User
from breathecode.services.google.utils import get_client


def participant_session(name: str, credentials: QuerySet[CredentialsGoogle]):
    from breathecode.mentorship.models import MentorshipSession

    errors = ""

    for credential in credentials:
        try:
            client = get_client(credential)
            participant_session = client.get_participant_session(name=name)
            names = name.split("/")
            space_name = "/".join(names[0:2])
            participant_name = "/".join(names[0:4])

            space = client.get_space(name=space_name)
            session = MentorshipSession.objects.filter(online_meeting_url=space.meeting_uri).first()
            if session is None:
                raise AbortTask(f"MentorshipSession with meeting url {space.meeting_uri} not found")

            try:
                participant = client.get_participant(name=participant_name)
                if participant.signedin_user:
                    user = User.objects.filter(credentialsgoogle__google_id=participant.signedin_user.user).first()
                    if session.mentor.user == user:
                        session.mentor_joined_at = session.mentor_joined_at or participant_session.start_time
                        session.mentor_left_at = participant_session.end_time

                    else:
                        raise Exception()

                else:
                    raise Exception()

            except Exception:
                session.started_at = session.started_at or participant_session.start_time
                session.mentee_left_at = participant_session.end_time

            session.save()

            return

        except AbortTask as e:
            raise e

        except Exception as e:
            errors += f"Error with credentials {credential.id}: {e}\n"

    raise AbortTask(errors)
