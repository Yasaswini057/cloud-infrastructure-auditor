import json
import os
from datetime import datetime
from utils.logger import logger


def generate_json_report(data, filename="audit_report.json"):
    """
    Generate JSON report from scanned cloud resources.
    """

    output_dir = "output/reports"
    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, filename)
    report_data = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "scan_status": "Completed",

        "summary": {
            "total_ec2_instances": len(data.get("ec2_instances", [])),
            "total_ebs_volumes": len(data.get("ebs_volumes", [])),
            "total_elastic_ips": len(data.get("elastic_ips", []))
        },

        "resources": data
    }

    try:
        with open(filepath, "w") as json_file:
            json.dump(report_data, json_file, indent=4)

        logger.info(f"JSON report generated successfully: {filepath}")
       

    except Exception as e:
        logger.error(f"Failed to generate JSON report: {str(e)}")
  