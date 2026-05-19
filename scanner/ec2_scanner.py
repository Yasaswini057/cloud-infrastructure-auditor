import boto3
from botocore.exceptions import BotoCoreError, ClientError

from auth.aws_auth import create_aws_session
from utils.logger import logger
from utils.logger import logger

def scan_ec2_instances():
    """
    Scan EC2 instances from AWS
    """

    try:
        session = create_aws_session()

        ec2_client = session.client("ec2")

        response = ec2_client.describe_instances()

        instances_data = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:

                instance_info = {
                    "InstanceId": instance.get("InstanceId"),
                    "State": instance["State"]["Name"],
                    "Type": instance.get("InstanceType")
                }

                instances_data.append(instance_info)

        return instances_data

    except (BotoCoreError, ClientError) as error:

        logger.error(f"EC2 Scan Failed: {str(error)}")

        print(f"Error scanning EC2 instances: {str(error)}")

        return []