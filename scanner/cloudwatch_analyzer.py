from utils.logger import logger
from datetime import datetime, timezone


def analyze_ec2_cpu_utilization():
    """
    Analyze EC2 CPU utilization
    and detect underutilized instances.
    """

    try:

        logger.info(
            "Starting EC2 CPU utilization analysis..."
        )

        current_time = datetime.now(
            timezone.utc
        )

        logger.info(
            f"Analysis Time: {current_time}"
        )

        # Mock CPU analysis data
        # TODO: Replace with real CloudWatch metrics

        underutilized_instances = [

            {
                "InstanceId": "i-1234567890",
                "AverageCPU": "2.3%",
                "Recommendation":
                "Downsize or terminate instance",

                "EstimatedSavings":
                "$45/month"
            },

            {
                "InstanceId": "i-0987654321",

                "AverageCPU": "1.1%",

                "Recommendation":
                "Move to smaller instance type",

                "EstimatedSavings":
                "$60/month"
            }

        ]

        logger.info(
            f"Found {len(underutilized_instances)} underutilized instances"
        )

        return underutilized_instances

    except Exception as e:

        logger.error(
            f"CloudWatch Analyzer Error: {str(e)}"
        )

        return []