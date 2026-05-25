from auth.aws_auth import create_aws_session
from botocore.exceptions import ClientError, BotoCoreError
import os


def validate_credentials():
    """
    Validate AWS credentials
    """

    try:

        session = create_aws_session()

        sts = session.client("sts")

        identity = sts.get_caller_identity()

        print("AWS Authentication Successful!")

        print(
            f"AWS Account ID: {identity['Account']}"
        )

        print(
            f"Region: {os.getenv('AWS_REGION')}"
        )

        return True

    except (ClientError, BotoCoreError) as e:

        print(
            f"AWS Error: {str(e)}"
        )

        return False

    except Exception as e:

        print(
            f"General Error: {str(e)}"
        )

        return False