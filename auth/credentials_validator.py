from auth.aws_auth import create_aws_session
from botocore.exceptions import ClientError, BotoCoreError


def validate_credentials():

    try:

        session = create_aws_session()

        sts_client = session.client("sts")

        response = sts_client.get_caller_identity()

        print(response)

        return True

    except (ClientError, BotoCoreError) as e:

        print("AWS Error:", e)

        return False

    except Exception as e:

        print("General Error:", e)

        return False