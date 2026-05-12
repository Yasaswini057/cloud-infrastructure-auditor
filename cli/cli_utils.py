import typer


def success_message(message):
    typer.secho(
        message,
        fg=typer.colors.GREEN,
        bold=True
    )


def error_message(message):
    typer.secho(
        message,
        fg=typer.colors.RED,
        bold=True
    )


def info_message(message):
    typer.secho(
        message,
        fg=typer.colors.CYAN,
        bold=True
    )