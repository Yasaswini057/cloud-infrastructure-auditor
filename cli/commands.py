import typer
import time

from rich.progress import track
from rich.table import Table
from rich.console import Console

from cli.banner import show_banner
from auth.credentials_validator import validate_credentials
from cli.cli_utils import (
    success_message,
    error_message,
    info_message
)

from scanner.ec2_scanner import scan_ec2_instances
from scanner.ebs_scanner import scan_ebs_volumes
from scanner.elastic_ip_scanner import scan_elastic_ips

from reports.json_report import generate_json_report

app = typer.Typer()
console = Console()


@app.callback()
def main():
    """
    Cloud Infrastructure Auditor CLI
    """
    show_banner()


@app.command()
def auth():
    """
    Validate AWS credentials
    """

    if validate_credentials():
        success_message("AWS Authentication Successful!")

    else:
        error_message("AWS Authentication Failed!")


@app.command()
def scan():
    """
    Scan AWS resources
    """

    resources = [
        "EC2 Instances",
        "EBS Volumes",
        "Elastic IPs"
    ]

    info_message("Starting AWS Infrastructure Scan...\n")

    for resource in track(resources, description="Scanning Resources..."):
        typer.echo(f"Checking {resource}...")
        time.sleep(1)

    ec2_data = scan_ec2_instances()
    ebs_data = scan_ebs_volumes()
    elastic_ip_data = scan_elastic_ips()

    # ---------------- EC2 TABLE ---------------- #

    table = Table(title="EC2 Scan Results")

    table.add_column("Instance ID", style="cyan")
    table.add_column("State", style="green")
    table.add_column("Type", style="yellow")

    if ec2_data:

        for instance in ec2_data:
            table.add_row(
                instance["InstanceId"],
                instance["State"],
                instance["Type"]
            )

    else:
        table.add_row(
            "No Instances Found",
            "-",
            "-"
        )

    console.print(table)

    # ---------------- EBS TABLE ---------------- #

    ebs_table = Table(title="EBS Scan Results")

    ebs_table.add_column("Volume ID", style="cyan")
    ebs_table.add_column("State", style="green")

    if ebs_data:

        for volume in ebs_data:
            ebs_table.add_row(
                volume["VolumeId"],
                volume["State"]
            )

    else:
        ebs_table.add_row(
            "No Volumes Found",
            "-"
        )

    console.print(ebs_table)

    # ---------------- ELASTIC IP TABLE ---------------- #

    elastic_ip_table = Table(title="Elastic IP Scan Results")

    elastic_ip_table.add_column("Public IP", style="cyan")
    elastic_ip_table.add_column("Allocation ID", style="yellow")

    if elastic_ip_data:

        for ip in elastic_ip_data:
            elastic_ip_table.add_row(
                ip["PublicIp"],
                ip["AllocationId"]
            )

    else:
        elastic_ip_table.add_row(
            "No Elastic IPs Found",
            "-"
        )

    console.print(elastic_ip_table)

    # ---------------- INFRASTRUCTURE SUMMARY ---------------- #

    typer.echo("\nInfrastructure Summary:")

    typer.echo(f"Total EC2 Instances: {len(ec2_data)}")
    typer.echo(f"Total EBS Volumes: {len(ebs_data)}")
    typer.echo(f"Total Elastic IPs: {len(elastic_ip_data)}")

    if not ec2_data:
        error_message(
            "No EC2 instances found or AWS credentials could not be validated."
        )

    # ---------------- REPORT GENERATION ---------------- #

    infrastructure_data = {
        "ec2_instances": ec2_data,
        "ebs_volumes": ebs_data,
        "elastic_ips": elastic_ip_data
    }

    generate_json_report(infrastructure_data)

    success_message("\nJSON Report Generated Successfully!")
    info_message("Report saved in output/reports/")

    success_message("\nCloud Infrastructure Audit Completed!")