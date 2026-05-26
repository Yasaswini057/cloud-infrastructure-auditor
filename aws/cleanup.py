from botocore.exceptions import BotoCoreError, ClientError
from auth.aws_auth import create_aws_session
from utils.logger import logger


def terminate_instance(instance_id: str, region: str = "ap-south-1", dry_run: bool = True):
    """
    Safely terminate EC2 instance with dry-run support
    """

    try:
        session = create_aws_session()
        ec2 = session.client("ec2", region_name=region)

        if dry_run:
            print(f"[DRY RUN] Would terminate instance: {instance_id}")
            return {
                "InstanceId": instance_id,
                "Action": "TERMINATE",
                "DryRun": True,
                "Status": "SIMULATED"
            }

        
        confirm = input(f"⚠ Are you sure you want to TERMINATE {instance_id}? (yes/no): ")

        if confirm.lower() != "yes":
            print("Termination cancelled by user.")
            return {
                "InstanceId": instance_id,
                "Action": "CANCELLED"
            }

        response = ec2.terminate_instances(InstanceIds=[instance_id])

        print(f" Instance terminated: {instance_id}")

        return {
            "InstanceId": instance_id,
            "Action": "TERMINATED",
            "Response": response
        }

    except (BotoCoreError, ClientError) as error:
        logger.error(f"Cleanup failed: {str(error)}")
        return {
            "InstanceId": instance_id,
            "Error": str(error)
        }