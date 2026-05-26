import typer
from rich import print

app = typer.Typer()


# ----------------------------
# SCAN COMMAND
# ----------------------------
@app.command()
def scan():
    """
    Scan AWS EC2 instances
    """
    from scanner.ec2_scanner import scan_ec2_instances

    print("[green]Scanning AWS resources...[/green]")

    data = scan_ec2_instances()

    for item in data:
        print(item)


# ----------------------------
# REPORT COMMAND
# ----------------------------
@app.command()
def report(format: str = "json"):
    """
    Generate report in JSON / CSV / YAML
    """
    from scanner.ec2_scanner import scan_ec2_instances
    from utils.report import export_csv, export_yaml

    print("[blue]Generating report...[/blue]")

    data = scan_ec2_instances()

    if format == "csv":
        export_csv(data)
        print("[green]CSV report generated[/green]")

    elif format == "yaml":
        export_yaml(data)
        print("[green]YAML report generated[/green]")

    else:
        print(data)


# ----------------------------
# CLEANUP COMMAND (UPDATED)
# ----------------------------
@app.command()
def cleanup(instance_id: str, dry_run: bool = True, execute: bool = False):
    """
    Cleanup EC2 instance safely (dry-run or execute mode)
    """
    from aws.cleanup import terminate_instance

    # if execute flag is used → force real execution
    if execute:
        dry_run = False

    print(f"[yellow]Cleanup mode (dry_run={dry_run})[/yellow]")

    result = terminate_instance(instance_id, dry_run=dry_run)

    print(result)


# ----------------------------
# ENTRY POINT
# ----------------------------
if __name__ == "__main__":
    app()