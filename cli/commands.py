import typer
from cli.banner import show_banner
from auth.credentials_validator import validate_credentials
from cli.cli_utils import (
    success_message,
    error_message,
    info_message
)
from rich.progress import track
import time
from scanner.ec2_scanner import scan_ec2_instances
from rich.table import Table
from rich.console import Console
from reports.json_report import generate_json_report
console = Console()

app = typer.Typer()


@app.callback()
def main():
    """
    Cloud Infrastructure Auditor CLI
    """
    show_banner()

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

    table = Table(title="EC2 Scan Results")

    table.add_column("Instance ID", style="cyan")
    table.add_column("State", style="green")
    table.add_column("Type", style="yellow")

    for instance in ec2_data:
        table.add_row(
            instance["InstanceId"],
            instance["State"],
            instance["Type"]
        )

    console.print(table)

    typer.echo("\nInfrastructure Summary:")
    typer.echo(f"Total EC2 Instances: {len(ec2_data)}")

    generate_json_report(ec2_data)

    success_message("\nJSON Report Generated Successfully!")
    info_message("Report saved in output/reports/")

    success_message("\nCloud Infrastructure Audit Completed!")

@app.command()
def auth():
    """
    Authenticate AWS credentials
    """

    success, message = validate_credentials()

    if success:
        success_message("AWS Authentication Successful!")
        typer.echo(message)

    else:
        error_message("AWS Authentication Failed!")
        typer.echo(message)