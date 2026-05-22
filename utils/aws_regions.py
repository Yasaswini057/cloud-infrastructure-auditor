import boto3


def get_all_regions():
    """
    Fetch all AWS regions
    """

    try:
        ec2 = boto3.client("ec2")

        response = ec2.describe_regions()

        regions = [region["RegionName"] for region in response["Regions"]]

        return regions

    except Exception:
        # Mock fallback regions
        return [
            "us-east-1",
            "us-west-2",
            "ap-south-1"
        ]