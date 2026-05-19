from utils.logger import logger


def scan_ebs_volumes():
    """
    Scan unattached EBS volumes
    """

    try:
        logger.info("Starting EBS volume scan...")

        # Mock EBS data
        # TODO: Replace with real Boto3 integration

        ebs_volumes = [
            {
                "VolumeId": "vol-001",
                "Size": 100,
                "State": "available",
                "Region": "us-east-1",
                "EstimatedSavings": "$12/month",
                "Recommendation": "Delete unattached EBS volume"
            },
            {
                "VolumeId": "vol-002",
                "Size": 50,
                "State": "available",
                "Region": "ap-south-1",
                "EstimatedSavings": "$6/month",
                "Recommendation": "Remove unused storage"
            }
        ]

        logger.info(f"Found {len(ebs_volumes)} unattached EBS volumes")

        return ebs_volumes

    except Exception as e:
        logger.error(f"EBS Scanner Error: {str(e)}")
        return []