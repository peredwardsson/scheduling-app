"""Contains entities for scheduling-app."""

import calendar
from dataclasses import dataclass, field
import datetime
from random import randint
from typing import Any, Dict, List

import numpy as np


@dataclass(eq=True)
class Employee:
    """Class for an employee.

    Attributes:
    - name(string) : Name of employee
    - experience(int): Experience level of employee.
        0-1 years = 1,
        2-4 years = 2,
        >4 years = 3
    - perference(list): List of this employees personal preferences.
    """

    name: str
    experience: int
    preferences: list
    id: int

    def __init__(self, name: str, experience: int, preferences: List) -> Any:
        """Returns an Employee with name, experience and perferences."""
        self.name = name
        self.experience = experience
        self.preferences = preferences
        self.id = hash((randint(0, 2e64), datetime.datetime.now()))

    def __hash__(self) -> int:
        """Hash stored in self.id."""
        return self.id


@dataclass
class Workforce:
    """Class to hold a workforce of Employees.

    Attributes:
    - employees(list): Contains a list of employees.

    """

    employees: List[Employee]

    def __str__(self) -> str:
        """Prints the name of the employees in the workforce."""
        s = "Workforce contains:\n"
        for x in self.employees:
            s += "- " + x.name + "\n"
        return s


@dataclass
class Calendar:
    """Class that holds a schedule for each day."""

    pass


@dataclass
class RegulatoryRequirements:
    """Holds regulatory requirements in a list."""

    laws: list


@dataclass
class Time_base:
    """A class that holds a time.

    Attributes:
        hour: The hour in question, 0-23
        minute: The minute in question, 0-59
    """

    hour: int = 0
    minute: int = 0

    assert hour > -1 and hour < 24
    assert minute > -1 and minute < 60

    def __repr__(self) -> str:
        """Returns a string on the form 23:59."""
        s = f"{self.hour:02d}:{self.minute:02d}"
        return s


@dataclass
class Time(Time_base):
    """Class that performs time calculations."""

    def add(self, time: Time_base) -> Time_base:
        """Adds the time to the object."""
        dm = self.minute + time.minute
        dt = self.hour + time.hour
        if dm > 60:
            dm -= 60
            dt += 1
        if dt > 23:
            dt -= 24
        self.hour = dt
        self.minute = dm
        return self

    @staticmethod
    def delta(time: Time_base, time2: Time_base) -> Time_base:
        """Calculates the time between time and time2."""
        dt = time2.hour - time.hour
        dm = time2.minute - time.minute
        if dm < 0:
            dt -= 1
            dm += 60
        if dt < 0:
            T = Time(dt, dm).add(Time(24, 0))
            return T
        return Time(dt, dm)

    def __repr__(self) -> str:
        """Returns the superclass __repr__."""
        return super().__repr__()


@dataclass
class Workshift_base:
    """An approved workshift that can be scheduled to employees."""

    name: str
    start_hour: Time
    finish_hour: Time
    days: List[int] = field(default_factory=list)


@dataclass
class Workshift(Workshift_base):
    """An approved workshift that can be scheduled to employees."""

    alternative_schedule: List[Workshift_base] = field(default_factory=list)

    def shift_length(self) -> Time_base:
        """Returns the length of the shift."""
        return Time.delta(self.start_hour, self.finish_hour)

    def add_alternative_schedule(self, shift: Workshift_base) -> None:
        """Appends an alternative schedule if the shift is laid on a specific day."""
        if bool(self.days) and all(x not in self.days for x in shift.days):
            raise AssertionError(
                "Alternative schedule needs to be defined \
                for a weekday that the workshift is valid."
            )
        self.alternative_schedule.append(shift)


@dataclass
class Schedule:
    """A schedule for a single day.

    Attributes:
        date: The day of the schedule
        requirements_regulatory: A list of functions for calculating
        regulatory requirements
        requirements_business: An np.array of employment needs per hour
        for a full day.
    """

    date: datetime.date = datetime.date(2020, 1, 1)
    weekday: str = calendar.day_name[date.weekday()]
    laws: list = field(default_factory=list)
    hours: np.ndarray = field(default_factory=np.ndarray)
    employees: List[Employee] = field(default_factory=list)
    shifts: List[Workshift] = field(default_factory=list)
    assignments: Dict[Employee, Workshift] = field(default_factory=dict)

    def assign_employee_to_shift(self, employee: Employee, shift: Workshift) -> None:
        """Assigns a Workshift to an Employee and adds a record to the Schedule."""
        self.assignments[employee] = shift

    assign = assign_employee_to_shift
