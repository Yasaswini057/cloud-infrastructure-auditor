import csv
import os
from utils.logger import logger


def generate_csv_report(data, filename="audit_report.csv"):
    """
    Generate CSV report from scanned cloud resources.
    """

    output_dir = "output/reports"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)

    try:
        if not data:
            logger.warning("No data available for CSV report generation")
            return

        ec2_data = data.get("ec2_instances", [])

        if not ec2_data:
            logger.warning("No EC2 data available for CSV report generation")
            return

        keys = ec2_data[0].keys()

        with open(filepath, mode="w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)

            writer.writeheader()
            writer.writerows(ec2_data)

        logger.info(f"CSV report generated successfully: {filepath}")

    except Exception as e:
        logger.error(f"Failed to generate CSV report: {str(e)}")