from auth.aws_auth import create_aws_session


def validate_credentials():
    try:
        session = create_aws_session()

        sts = session.client("sts")
        identity = sts.get_caller_identity()

        return True, identity

    except Exception as e:
        return False, str(e)