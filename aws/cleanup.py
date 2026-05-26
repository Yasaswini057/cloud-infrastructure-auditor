import boto3

ec2 = boto3.client("ec2")


def terminate_instance(instance_id, dry_run=True):
    """
    Terminate EC2 instance safely
    """
    if dry_run:
        print(f"[DRY RUN] Would terminate instance: {instance_id}")
        return

    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminated instance: {instance_id}")


def release_eip(allocation_id, dry_run=True):
    """
    Release Elastic IP safely
    """
    if dry_run:
        print(f"[DRY RUN] Would release Elastic IP: {allocation_id}")
        return

    ec2.release_address(AllocationId=allocation_id)
    print(f"Released Elastic IP: {allocation_id}")


def delete_volume(volume_id, dry_run=True):
    """
    Delete unused EBS volume safely
    """
    if dry_run:
        print(f"[DRY RUN] Would delete volume: {volume_id}")
        return

    ec2.delete_volume(VolumeId=volume_id)
    print(f"Deleted volume: {volume_id}")