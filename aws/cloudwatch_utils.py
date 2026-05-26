from datetime import datetime, timezone, timedelta
import boto3
from botocore.exceptions import BotoCoreError, ClientError

from auth.aws_auth import create_aws_session
from utils.logger import logger


def get_cpu_avg(instance_id: str, region: str = "ap-south-1"):
    """
    Fetch average CPU utilization over last 14 days for an EC2 instance
    using AWS CloudWatch.
    """
    try:
        session = create_aws_session()
        cloudwatch = session.client("cloudwatch", region_name=region)

        # 14-day analysis window
        end_time = datetime.now(timezone.utc)
        start_time = end_time - timedelta(days=14)

        response = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[
                {
                    "Name": "InstanceId",
                    "Value": instance_id
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=86400,  # daily average
            Statistics=["Average"]
        )

        datapoints = response.get("Datapoints", [])

        if not datapoints:
            return None

        # Calculate average CPU over period
        avg_cpu = sum(dp["Average"] for dp in datapoints) / len(datapoints)

        return round(avg_cpu, 4)

    except (BotoCoreError, ClientError) as error:
        logger.error(f"[CloudWatch Error] {str(error)}")
        return None