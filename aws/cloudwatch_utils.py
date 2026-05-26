import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

def get_cpu_avg(instance_id):
    end = datetime.utcnow()
    start = end - timedelta(days=14)

    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {'Name': 'InstanceId', 'Value': instance_id}
        ],
        StartTime=start,
        EndTime=end,
        Period=86400,
        Statistics=['Average']
    )

    points = response.get("Datapoints", [])

    if not points:
        return None

    return sum(p["Average"] for p in points) / len(points)