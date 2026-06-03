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
from reports.csv_report import generate_csv_report
from reports.yaml_report import generate_yaml_report

from optimizer.analyzer import (
    analyze_ec2_instances,
    analyze_ebs_volumes
)

from optimizer.recommendations import (
    generate_recommendations
)

from optimizer.cost_calculator import (
    calculate_total_cost,
    calculate_potential_savings
)


from aws.cleanup import terminate_instance

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
    """
    Show project version
    """
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
    """
    Show available commands
    """

    typer.echo("\n========== Cloud Infrastructure Auditor ==========\n")

    typer.echo("auth")
    typer.echo("   Validate AWS credentials")

    typer.echo("\nscan")
    typer.echo("   Scan AWS resources and generate report")

    typer.echo("\ncleanup <instance_id>")
    typer.echo("   Simulate EC2 instance cleanup (Dry Run)")

    typer.echo("\nversion")
    typer.echo("   Show project version")

    typer.echo("\nhelp-command")
    typer.echo("   Show available commands")

    typer.echo("\n==================================================")

@app.command()
def cleanup(
    instance_id: str,
    dry_run: bool = True
):
    result = terminate_instance(
        instance_id=instance_id,
        dry_run=dry_run
    )

    print(result)

@app.command()
def scan():
    """
    Scan AWS resources
    """
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

    resources_data = {
        "ec2": ec2_data,
        "ebs": ebs_data,
        "elastic_ips": elastic_ip_data
    }

    recommendations = generate_recommendations(
        resources_data
    )
    monthly_cost = calculate_total_cost(
    ec2_data
    )

    potential_savings = calculate_potential_savings(
    ec2_data
   )

    annual_savings = round(
    potential_savings * 12,
    2
   )
    infrastructure_data = {
        "ec2_instances": ec2_data,
        "ebs_volumes": ebs_data,
        "elastic_ips": elastic_ip_data,
        "recommendations": recommendations
    }

    # EC2 TABLE WITH AVERAGE CPU UPDATE
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
    table.add_column(
        "Average CPU (%)",
        style="magenta"
    )

    if ec2_data:
        for instance in ec2_data:
            # Safely fetch the custom metric fields added by member 2
            cpu_val = instance.get("AverageCPU", 0.0)
            table.add_row(
                instance["InstanceId"],
                instance["State"],
                instance["Type"],
                f"{cpu_val}%"
            )
    else:
        table.add_row(
            "No Instances Found",
            "-",
            "-",
            "-"
        )

    console.print(table)

    # EBS TABLE
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

    console.print(
        ebs_table
    )

    # ELASTIC IP TABLE
    elastic_ip_table = Table(
        title="Elastic IP Scan Results"
    )
    elastic_ip_table.add_column(
        "Public IP",
        style="cyan"
    )
    elastic_ip_table.add_column(
        "Allocation ID",
        style="yellow"
    )

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

    console.print(
        elastic_ip_table
    )

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

    if not ec2_data:
        error_message(
            "No EC2 instances found or AWS credentials could not be validated."
        )

    # UNDERUTILIZED METRIC COUNT ADDED HERE
    underutilized_ec2 = sum(1 for inst in ec2_data if inst.get("Underutilized", False))

    typer.echo(
        "\nOptimization Summary:"
    )
    typer.echo(
        f"Stopped EC2 Instances: {len(stopped_instances)}"
    )
    typer.echo(
        f"Underutilized EC2 Instances: {underutilized_ec2}"
    )
    typer.echo(
        f"Unused EBS Volumes: {len(unused_volumes)}"
    )
    typer.echo(
    "\nEstimated Monthly Cost:"
    )

    typer.echo(
    f"EC2 Cost: ${monthly_cost}/month"
    )

    typer.echo(
    "\nPotential Savings:"
    )

    typer.echo(
    f"Monthly Savings: ${potential_savings}"
    )

    typer.echo(
    f"Annual Savings: ${annual_savings}"
    )
    typer.echo(
        "\nRecommendations:"
    )
    for recommendation in recommendations:
        typer.echo(
            f"- {recommendation}"
        )

    generate_json_report(
        infrastructure_data
    )
    generate_csv_report(
    infrastructure_data
    )
    generate_yaml_report(
    infrastructure_data
    )

    success_message(
        "\nJSON Report Generated Successfully!"
    )
    success_message(
    "CSV Report Generated Successfully!"
    )
    info_message(
        "Report saved in output/reports/"
    )

    end_time = datetime.now()
    duration = end_time - start_time

    console.print(
        f"\n[bold yellow]Scan Duration: {duration}[/bold yellow]"
    )
    console.print(
        "\n[bold green]Scan Status : Completed[/bold green]"
    )
    console.print(
        "[bold cyan]Resources Checked : EC2, EBS, Elastic IP[/bold cyan]"
    )
    success_message(
        "\nCloud Infrastructure Audit Completed!"
    )