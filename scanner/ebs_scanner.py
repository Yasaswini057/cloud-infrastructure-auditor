from botocore.exceptions import BotoCoreError, ClientError

from auth.aws_auth import create_aws_session
from utils.logger import logger
from utils.aws_regions import get_all_regions


def scan_ebs_volumes():
    """
    Scan EBS volumes across multiple AWS regions
    """

    try:
        session = create_aws_session()

        regions = get_all_regions()

        volumes_data = []

        for region in regions:

            logger.info(f"Scanning EBS volumes in region: {region}")

            ec2_client = session.client("ec2", region_name=region)

            response = ec2_client.describe_volumes()

            for volume in response["Volumes"]:

                volume_info = {
                    "VolumeId": volume.get("VolumeId"),
                    "State": volume.get("State"),
                    "Region": region
                }

                volumes_data.append(volume_info)

        return volumes_data

    except (BotoCoreError, ClientError) as error:

        logger.error(
            f"EBS scanning failed: {str(error)}"
        )

        return []