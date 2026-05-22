from botocore.exceptions import BotoCoreError, ClientError

from auth.aws_auth import create_aws_session
from utils.logger import logger
from utils.aws_regions import get_all_regions


def scan_ec2_instances():
    """
    Scan EC2 instances across multiple AWS regions
    """

    try:
        session = create_aws_session()

        regions = get_all_regions()

        instances_data = []

        for region in regions:

            logger.info(f"Scanning EC2 instances in region: {region}")

            ec2_client = session.client("ec2", region_name=region)

            response = ec2_client.describe_instances()

            for reservation in response["Reservations"]:

                for instance in reservation["Instances"]:

                    instance_info = {
                        "InstanceId": instance.get("InstanceId"),
                        "State": instance.get("State", {}).get("Name"),
                        "Type": instance.get("InstanceType"),
                        "Region": region
                    }

                    instances_data.append(instance_info)

        return instances_data

    except (BotoCoreError, ClientError) as error:

        logger.error(f"EC2 scanning failed: {str(error)}")

    return []