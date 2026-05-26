from botocore.exceptions import BotoCoreError, ClientError

from auth.aws_auth import create_aws_session
from utils.logger import logger
from utils.aws_regions import get_all_regions
from aws.cloudwatch_utils import get_cpu_avg


def scan_ec2_instances():
    """
    Scan EC2 instances across multiple AWS regions with CloudWatch CPU analysis
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

                    instance_id = instance.get("InstanceId")

                    
                    cpu = get_cpu_avg(instance_id, region)

                    
                    if cpu is None:
                        status = "NO DATA"
                    elif cpu < 5:
                        status = "UNDERUTILIZED"
                    else:
                        status = "ACTIVE"

                    instance_info = {
                        "InstanceId": instance_id,
                        "State": instance.get("State", {}).get("Name"),
                        "Type": instance.get("InstanceType"),
                        "Region": region,

                        
                        "CpuUtilization": cpu,
                        "AnalysisWindow": "14 days",
                        "MetricSource": "AWS CloudWatch (Average CPU)",

                        "Status": status
                    }

                    instances_data.append(instance_info)

        print(f"EC2 Instances Scanned: {len(instances_data)}")

        return instances_data

    except (BotoCoreError, ClientError) as error:
        logger.error(f"EC2 scanning failed: {str(error)}")

    return []