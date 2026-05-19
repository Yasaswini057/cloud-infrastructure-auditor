from rich.console import Console
from rich.table import Table

console = Console()


def display_ec2_table(ec2_data):
    """
    Display EC2 instances in table format.
    """

    table = Table(title="EC2 Instances")

    table.add_column("Instance ID", style="cyan")
    table.add_column("State", style="green")
    table.add_column("Instance Type", style="yellow")
    table.add_column("Public IP", style="magenta")

    for instance in ec2_data:
        table.add_row(
            str(instance.get("instance_id", "N/A")),
            str(instance.get("state", "N/A")),
            str(instance.get("instance_type", "N/A")),
            str(instance.get("public_ip", "N/A"))
        )

    console.print(table)


def display_ebs_table(ebs_data):
    """
    Display EBS volumes in table format.
    """

    table = Table(title="EBS Volumes")

    table.add_column("Volume ID", style="cyan")
    table.add_column("State", style="green")
    table.add_column("Size (GB)", style="yellow")

    for volume in ebs_data:
        table.add_row(
            str(volume.get("volume_id", "N/A")),
            str(volume.get("state", "N/A")),
            str(volume.get("size", "N/A"))
        )

    console.print(table)


def display_elastic_ip_table(elastic_ip_data):
    """
    Display Elastic IPs in table format.
    """

    table = Table(title="Elastic IPs")

    table.add_column("Public IP", style="cyan")
    table.add_column("Associated Instance", style="green")

    for ip in elastic_ip_data:
        table.add_row(
            str(ip.get("public_ip", "N/A")),
            str(ip.get("instance_id", "Unassociated"))
        )

    console.print(table)