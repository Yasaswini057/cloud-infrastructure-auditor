import typer
import time
from datetime import datetime

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

from optimizer.analyzer import (
    analyze_ec2_instances,
    analyze_ebs_volumes
)

from optimizer.recommendations import (
    generate_recommendations
)

from optimizer.cost_calculator import (
    estimate_ec2_cost
)

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

        success_message(
            "AWS Authentication Successful!"
        )

    else:

        error_message(
            "AWS Authentication Failed!"
        )

        info_message(
            "Please verify Access Key, Secret Key and AWS Region."
        )


@app.command()
def version():

    typer.echo(
        "Project : Cloud Infrastructure Auditor"
    )

    typer.echo(
        "Version : v1.0"
    )

    typer.echo(
        "Module : CLI + Authentication"
    )


@app.command()
def help_command():

    typer.echo(
        "Available Commands:"
    )

    typer.echo(
        "auth -> Validate AWS credentials"
    )

    typer.echo(
        "scan -> Scan AWS resources"
    )

    typer.echo(
        "version -> Show project version"
    )


@app.command()
def scan():

    start_time = datetime.now()

    resources = [
        "EC2 Instances",
        "EBS Volumes",
        "Elastic IPs"
    ]

    info_message(
        "Starting AWS Infrastructure Scan...\n"
    )

    for resource in track(
        resources,
        description="Scanning Resources..."
    ):

        typer.echo(
            f"Checking {resource}..."
        )

        time.sleep(1)

        typer.echo(
            f"{resource} Scan Completed"
        )

    ec2_data = scan_ec2_instances()

    ebs_data = scan_ebs_volumes()

    elastic_ip_data = scan_elastic_ips()

    stopped_instances = analyze_ec2_instances(
        ec2_data
    )

    unused_volumes = analyze_ebs_volumes(
        ebs_data
    )

    estimated_cost = estimate_ec2_cost(
        ec2_data
    )

    resources_data = {
        "ec2": ec2_data,
        "ebs": ebs_data,
        "elastic_ips": elastic_ip_data
    }

    recommendations = generate_recommendations(
        resources_data
    )

    infrastructure_data = {
        "ec2_instances": ec2_data,
        "ebs_volumes": ebs_data,
        "elastic_ips": elastic_ip_data,
        "recommendations": recommendations
    }

    table = Table(
        title="EC2 Scan Results"
    )

    table.add_column(
        "Instance ID",
        style="cyan"
    )

    table.add_column(
        "State",
        style="green"
    )

    table.add_column(
        "Type",
        style="yellow"
    )

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

    ebs_table = Table(
        title="EBS Scan Results"
    )

    ebs_table.add_column(
        "Volume ID",
        style="cyan"
    )

    ebs_table.add_column(
        "State",
        style="green"
    )

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

    elastic_table = Table(
        title="Elastic IP Scan Results"
    )

    elastic_table.add_column(
        "Public IP",
        style="cyan"
    )

    elastic_table.add_column(
        "Allocation ID",
        style="yellow"
    )

    if elastic_ip_data:

        for ip in elastic_ip_data:

            elastic_table.add_row(
                ip["PublicIp"],
                ip["AllocationId"]
            )

    else:

        elastic_table.add_row(
            "No Elastic IPs Found",
            "-"
        )

    console.print(elastic_table)

    typer.echo(
        "\nInfrastructure Summary:"
    )

    typer.echo(
        f"Total EC2 Instances: {len(ec2_data)}"
    )

    typer.echo(
        f"Total EBS Volumes: {len(ebs_data)}"
    )

    typer.echo(
        f"Total Elastic IPs: {len(elastic_ip_data)}"
    )

    typer.echo(
        "\nOptimization Summary:"
    )

    typer.echo(
        f"Stopped EC2 Instances: {len(stopped_instances)}"
    )

    typer.echo(
        f"Unused EBS Volumes: {len(unused_volumes)}"
    )

    typer.echo(
        "\nEstimated Monthly Cost:"
    )

    typer.echo(
        f"EC2 Cost: ${estimated_cost}/month"
    )

    typer.echo(
        "\nRecommendations:"
    )

    if recommendations:

        for recommendation in recommendations:

            typer.echo(
                f"- {recommendation}"
            )

    else:

        typer.echo(
            "- No optimization recommendations found."
        )

    generate_json_report(
        infrastructure_data
    )

    success_message(
        "\nJSON Report Generated Successfully!"
    )

    info_message(
        "Report saved in output/reports/"
    )

    duration = (
        datetime.now() - start_time
    )

    console.print(
        f"\n[bold yellow]Scan Duration: {duration}[/bold yellow]"
    )

    console.print(
        "\n[bold green]Scan Status : Completed[/bold green]"
    )

    console.print(
        "[bold cyan]Resources Checked : EC2, EBS, Elastic IP[/bold cyan]"
    )

    console.print(
        "\n========== FINAL AUDIT REPORT =========="
    )

    console.print(
        f"EC2 Instances : {len(ec2_data)}"
    )

    console.print(
        f"EBS Volumes : {len(ebs_data)}"
    )

    console.print(
        f"Elastic IPs : {len(elastic_ip_data)}"
    )

    console.print(
        f"Estimated Cost : ${estimated_cost}/month"
    )

    console.print(
        "Status : Audit Completed"
    )

    success_message(
        "\nCloud Infrastructure Audit Completed!"
    )


if __name__ == "__main__":

    app()