import boto3
from datetime import datetime, timezone, timedelta


def get_cpu_avg(instance_id, region="ap-south-1"):
    """
    Get average CPU utilization for last 14 days from CloudWatch
    """

    try:

        cloudwatch = boto3.client(
            "cloudwatch",
            region_name=region
        )

        end_time = datetime.now(
            timezone.utc
        )

        start_time = end_time - timedelta(
            days=14
        )

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

            Period=86400,

            Statistics=["Average"]

        )

        datapoints = response.get(
            "Datapoints",
            []
        )

        if not datapoints:

            return None

        avg_cpu = sum(
            dp["Average"]
            for dp in datapoints
        ) / len(datapoints)

        return round(
            avg_cpu,
            4
        )

    except Exception as e:

        print(
            f"[CloudWatch Error] {str(e)}"
        )

        return None