from auth.aws_auth import create_aws_session
from botocore.exceptions import BotoCoreError, ClientError
from utils.logger import logger


def scan_ebs_volumes():
    """
    Scan EBS volumes from AWS
    """

    try:
        session = create_aws_session()

        ec2_client = session.client("ec2")

        response = ec2_client.describe_volumes()

        volumes_data = []

        for volume in response["Volumes"]:

            volume_info = {
                "VolumeId": volume.get("VolumeId"),
                "State": volume.get("State")
            }

            volumes_data.append(volume_info)

        return volumes_data

    except (BotoCoreError, ClientError) as error:

        logger.error(
            f"EBS scanning failed: {str(error)}"
        )

        print(
            f"Error scanning EBS volumes: {str(error)}"
        )

        return []