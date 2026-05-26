import boto3

ec2 = boto3.client("ec2")


def terminate_instance(instance_id, dry_run=True):
    if dry_run:
        print(f"[DRY RUN] Would terminate instance: {instance_id}")
        return

    confirm = input(f"Are you sure you want to terminate {instance_id}? (yes/no): ")

    if confirm.lower() != "yes":
        print("Cancelled termination.")
        return

    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"[+] Terminated instance: {instance_id}")


def release_eip(allocation_id, dry_run=True):
    if dry_run:
        print(f"[DRY RUN] Would release EIP: {allocation_id}")
        return

    confirm = input(f"Release Elastic IP {allocation_id}? (yes/no): ")

    if confirm.lower() != "yes":
        print("Cancelled.")
        return

    ec2.release_address(AllocationId=allocation_id)
    print(f"[+] Released EIP: {allocation_id}")


def delete_volume(volume_id, dry_run=True):
    if dry_run:
        print(f"[DRY RUN] Would delete volume: {volume_id}")
        return

    confirm = input(f"Delete volume {volume_id}? (yes/no): ")

    if confirm.lower() != "yes":
        print("Cancelled.")
        return

    ec2.delete_volume(VolumeId=volume_id)
    print(f"[+] Deleted volume: {volume_id}")