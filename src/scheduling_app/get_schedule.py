"""Scheduling app."""
from datetime import datetime
import pickle
import random
from typing import List

import click
import numpy as np


from scheduling_app.entities import (
    Employee,
    Schedule,
    Workforce,
    # RegulatoryRequirements,
)
from . import __version__


MIDADJUST = 2
FIRSTCOL = 30


def month_int_to_str(month_idx: int) -> str:
    """Converts an integer [1-12] into a string of equivalent month."""
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
    with open("test_data/workshifts.pkl", "rb") as f:
        workshifts = pickle.load(f)
    business_hours = np.genfromtxt("test_data/business.csv", delimiter=",")
    if month is None:
        month = datetime.now().month + 1
    p = generate_test_employee()
    p3 = generate_test_employee()
    p2 = generate_test_employee(name="Person B")
    s = Schedule(
        hours=business_hours, laws=[], employees=[p, p2, p3], shifts=workshifts
    )
    schedule_employees(s)
    print_schedule(s)


def generate_test_employee(
    name: str = "Person A", exp: int = 3, pref: List = None, happiness: float = 1.0
) -> Employee:
    """Generates an employee for testing purposes."""
    e = Employee(name=name, experience=exp, preferences=pref)
    return e


def schedule_employees(s: Schedule) -> None:
    """Schedules all employees according to an optimization algorithm."""
    assert s.employees, "schedule_employees(): No employees in input schedule."
    for person in s.employees:
        shift = random.choice(s.shifts)
        s.assign(person, shift)


def print_schedule(schedule: Schedule) -> None:
    """Prints the given schedule in console."""
    hours = np.linspace(0, 23, num=24)
    click.echo(f"Schedule for {schedule.weekday}, {schedule.date}.")
    click.echo("-" * 205)
    print("{:<30}".format("## clock"), end="")
    for clock in hours:
        print(f"{clock:02n}:00", end=" ")
    click.echo("")
    print("{:<30}".format("## need"), end="")
    for need in schedule.hours:
        print(f"{need:<6n}", end="")
    click.echo("")
    click.echo("-" * 205)
    if schedule.employees is not None:
        for person in schedule.employees:
            print(f"{person.name:<32}", end="")
            shift = schedule.assignments[person]
            for hour in hours:
                s = (
                    "####"
                    if hour >= shift.start_hour.hour and hour < shift.finish_hour.hour
                    else ""
                )
                print("{:<6}".format(s), end="")
            print("")


def init_workforce() -> Workforce:
    """Initializes a Workforce with three unit employees."""
    p1 = Employee(name="Person A", experience=1, preferences=[])
    p2 = Employee(name="Person B", experience=1, preferences=[])
    p3 = Employee(name="Person C", experience=1, preferences=[])
    return Workforce([p1, p2, p3])
