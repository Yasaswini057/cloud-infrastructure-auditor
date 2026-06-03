import os
import boto3


def get_cpu_utilization(instance_id, cloudwatch_client=None):
    """
    Mocked CPU utilization
    """
    return 3.5


def scan_ec2_instances():
    """
    Scan EC2 Instances
    """

    ec2_client = boto3.client(
        "ec2",
        region_name=os.getenv("AWS_REGION", "ap-south-1")
    )

    ec2_results = []

    instances = ec2_client.describe_instances()

    for reservation in instances.get("Reservations", []):

        for instance in reservation.get("Instances", []):

            instance_id = instance["InstanceId"]
            state = instance["State"]["Name"]
            instance_type = instance["InstanceType"]

            cpu_utilization = get_cpu_utilization(instance_id)

            is_underutilized = (
                state == "running"
                and cpu_utilization < 5.0
            )

            ec2_results.append({
                "InstanceId": instance_id,
                "State": state,
                "Type": instance_type,
                "AverageCPU": round(cpu_utilization, 2),
                "Underutilized": is_underutilized
            })

    return ec2_results