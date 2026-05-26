import csv
import json
import yaml
from datetime import datetime


def export_csv(data, filename="report.csv"):
    if not data:
        print("No data to export")
        return

    keys = data[0].keys()

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"[+] CSV saved: {filename}")


def export_yaml(data, filename="report.yaml"):
    if not data:
        print("No data to export")
        return

    with open(filename, "w") as f:
        yaml.dump(data, f)

    print(f"[+] YAML saved: {filename}")


def generate_finops_summary(data):
    """
    Cost optimization summary (for spec compliance)
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


def export_json_report(data, filename="output/reports/report.json"):
    summary = generate_finops_summary(data)

    report = {
        "summary": summary,
        "resources": data
    }

    with open(filename, "w") as f:
        json.dump(report, f, indent=4)

    print(f"[+] JSON report saved: {filename}")