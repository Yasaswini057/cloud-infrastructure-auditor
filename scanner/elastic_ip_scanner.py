from auth.aws_auth import create_aws_session
from botocore.exceptions import BotoCoreError, ClientError
from utils.logger import logger


def scan_elastic_ips():
    """
    Scan Elastic IPs from AWS
    """

    try:
        session = create_aws_session()

        ec2_client = session.client("ec2")

        response = ec2_client.describe_addresses()

        elastic_ip_data = []

        for address in response["Addresses"]:

            ip_info = {
                "PublicIp": address.get("PublicIp"),
                "AllocationId": address.get(
                    "AllocationId",
                    "-"
                )
            }

            elastic_ip_data.append(ip_info)

        return elastic_ip_data

    except (BotoCoreError, ClientError) as error:

        logger.error(
            f"Elastic IP scanning failed: {str(error)}"
        )

        print(
            f"Error scanning Elastic IPs: {str(error)}"
        )

        return []