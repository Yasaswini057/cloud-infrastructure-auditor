import csv
import json
import yaml
import os
from datetime import datetime


OUTPUT_DIR = "output/reports"


def ensure_output_directory():
    """
    Create output directory if not present.
    """

    os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_csv(data, filename="report.csv"):

    ensure_output_directory()

    if not data:
        return

    filepath = os.path.join(OUTPUT_DIR, filename)

    keys = data[0].keys()

    with open(filepath, "w", newline="") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=keys
        )

        writer.writeheader()
        writer.writerows(data)


def export_yaml(data, filename="report.yaml"):

    ensure_output_directory()

    if not data:
        return

    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w") as f:

        yaml.dump(
            data,
            f,
            default_flow_style=False
        )


def generate_finops_summary(data):
    """
    Cost optimization summary
    """

    summary = {
        "timestamp": str(datetime.now()),
        "total_resources": len(data),
        "underutilized": 0,
        "running": 0
    }

    for item in data:

        if item.get("Status") == "UNDERUTILIZED":

            summary["underutilized"] += 1

        if item.get("State") == "running":

            summary["running"] += 1

    return summary


def export_json_report(
    data,
    filename="report.json"
):

    ensure_output_directory()

    summary = generate_finops_summary(data)

    report = {
        "summary": summary,
        "resources": data
    }

    filepath = os.path.join(
        OUTPUT_DIR,
        filename
    )

    with open(filepath, "w") as f:

        json.dump(
            report,
            f,
            indent=4
        )