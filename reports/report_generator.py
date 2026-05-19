from reports.json_report import generate_json_report
from reports.csv_report import generate_csv_report


def generate_all_reports(resources):
    """
    Generate all report formats.
    """

    generate_json_report(resources)
    generate_csv_report(resources)