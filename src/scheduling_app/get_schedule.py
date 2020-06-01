from datetime import datetime
import os

import click

from scheduling_app.entities import (
    Schedule,
    # BusinessRequirements,
    # RegulatoryRequirements,
    # Employee,
)
from . import __version__


def month_int_to_str(month_idx: int) -> str:

    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    return switcher.get(month_idx, f"ERROR: input {month_idx} not found in switcher")


@click.command()
@click.option("--month", type=int, help="month (1-12) to generate schedule for")
@click.version_option(version=__version__)
def main(month: int) -> None:
    """A damn fine scheduling app."""
    click.echo("Hello world!")
    click.echo(os.getcwd())
    if month is None:
        month = datetime.now().month + 1
    month_str = month_int_to_str(month)
    click.echo(f"Picked month {month_str}")


def generate_base_schedule() -> Schedule:
    pass
