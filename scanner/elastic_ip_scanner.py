from utils.logger import logger


def scan_elastic_ips():
    """
    Scan unused Elastic IPs
    """

    try:
        logger.info("Starting Elastic IP scan...")

        # Mock Elastic IP data
        # TODO: Replace with real Boto3 integration

        elastic_ips = [
            {
                "PublicIp": "52.10.20.30",
                "AllocationId": "eipalloc-001",
                "Region": "us-east-1",
                "EstimatedSavings": "$5/month",
                "Recommendation": "Release unused Elastic IP"
            },
            {
                "PublicIp": "18.60.10.40",
                "AllocationId": "eipalloc-002",
                "Region": "ap-south-1",
                "EstimatedSavings": "$5/month",
                "Recommendation": "Unused Elastic IP detected"
            }
        ]

        logger.info(f"Found {len(elastic_ips)} unused Elastic IPs")

        return elastic_ips

    except Exception as e:
        logger.error(f"Elastic IP Scanner Error: {str(e)}")
        return []