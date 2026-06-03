# reports/yaml_report.py

import yaml
import os

def generate_yaml_report(data):
    os.makedirs("output/reports", exist_ok=True)

    with open(
        "output/reports/audit_report.yaml",
        "w"
    ) as file:
        yaml.dump(
            data,
            file,
            default_flow_style=False
        )

    print("YAML Report Generated Successfully!")