# src/scheduling_app/get_schedule.py
import click
from datetime import datetime

from . import __version__

def month_int_to_str(month_idx: int):
    
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
        12: "December"
    }
    return switcher.get(month_idx, f"ERROR: input {month_idx} not found in switcher")

@click.command()
@click.option("--month", type=int, help="month (1-12) which to generate schedule for")
@click.version_option(version=__version__)
def main(month):
    """A damn fine scheduling app."""
    click.echo("Hello world!")
    if month == None:
        month = datetime.now().month + 1
    month = month_int_to_str(month)
    click.echo(f"Picked month {month}")

