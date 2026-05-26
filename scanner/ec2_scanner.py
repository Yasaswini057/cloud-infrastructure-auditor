import datetime
import boto3

def get_cpu_utilization(instance_id, cloudwatch_client=None):
    """
    Week 2 Day 4-6 Task: Fetches the average CPU utilization.
    MOCKED: Forced to return exactly 5.0 for project demonstration.
    """
    # Simply return 5.0 directly to simulate a 5% CPU load
    return 3.5

def scan_ec2_instances():
    """
    Week 2 Day 7 Task: Structures the aggregated scan data 
    into internal Python dictionaries.
    """
    ec2_client = boto3.client('ec2')
    
    ec2_results = []
    instances = ec2_client.describe_instances()
    
    for reservation in instances.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            instance_type = instance['InstanceType']
            
            # Call the mocked metric function
            cpu_utilization = get_cpu_utilization(instance_id)
            
            # Logic threshold check (< 5% is underutilized)
            # Change to <= 5.0 if you want an exact 5.0% to still trigger a recommendation
            is_underutilized = False
            if state == 'running' and cpu_utilization < 5.0:
                is_underutilized = True
            
            # Map into standard dictionary structure for the reporting module
            ec2_results.append({
                "InstanceId": instance_id,
                "State": state,
                "Type": instance_type,
                "AverageCPU": round(cpu_utilization, 2),
                "Underutilized": is_underutilized
            })
            
    return ec2_results