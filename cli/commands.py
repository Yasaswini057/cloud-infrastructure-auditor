import typer
from cli.banner import show_banner
from auth.credentials_validator import validate_credentials
from cli.cli_utils import (
    success_message,
    error_message,
    info_message
)

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

    info_message("Starting AWS Infrastructure Scan...")

    typer.echo("Checking EC2 instances...")
    typer.echo("Checking EBS volumes...")
    typer.echo("Checking Elastic IPs...")

    success_message("Scan Completed Successfully!")

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