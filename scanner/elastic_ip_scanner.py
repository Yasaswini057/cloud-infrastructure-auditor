from botocore.exceptions import BotoCoreError, ClientError

from auth.aws_auth import create_aws_session
from utils.logger import logger
from utils.aws_regions import get_all_regions


def scan_elastic_ips():
    """
    Scan Elastic IPs across multiple AWS regions
    """

    try:
        session = create_aws_session()

        regions = get_all_regions()

        elastic_ips_data = []

        for region in regions:

            logger.info(f"Scanning Elastic IPs in region: {region}")

            ec2_client = session.client("ec2", region_name=region)

            response = ec2_client.describe_addresses()

            for address in response["Addresses"]:
                if "InstanceId" in address:
                    continue

                elastic_ip_info = {
                    "PublicIp": address.get("PublicIp"),
                    "AllocationId": address.get(
                        "AllocationId",
                        "-"
                    ),
                    "Region": region
                }

                elastic_ips_data.append(elastic_ip_info)

        return elastic_ips_data

    except (BotoCoreError, ClientError) as error:

        logger.error(
            f"Elastic IP scanning failed: {str(error)}"
        )

        return []