"""Contains entities for scheduling-app."""

import calendar
from dataclasses import dataclass, field
import datetime
from random import randint
from typing import Any, Dict, List, Tuple

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
class RegulatoryRequirements:
    """Holds regulatory requirements in a list."""

    laws: list


@dataclass
class Time:
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

    def add(self, time: "Time") -> "Time":
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
    def delta(time: "Time", time2: "Time") -> "Time":
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


@dataclass
class Workshift:
    """An approved workshift that can be scheduled to employees.

    Attributes:
    - name(str): Name of the workshift
    - start_hour(Time): Starting time of shift
    - finish_hour(Time): Finishing time of shift
    - days(List[int]): List of weekdays at which shift is applicable
    - alternative_schedule(List[Workshift]): Optional, if some days require different
      workshifts, these can be added here.
    """

    name: str
    start_hour: Time
    finish_hour: Time
    days: List[int] = field(default_factory=list)

    alternative_schedule: List["Workshift"] = field(default_factory=list)

    @property
    def time_tuple(self) -> Tuple[Time, Time]:
        """Returns a tuple containing start and finishing hours."""
        return (self.start_hour, self.finish_hour)

    @property
    def overnight(self) -> bool:
        """Returns a bool indicating whether this shift runs overnight."""
        return self.finish_hour.hour < self.start_hour.hour

    @property
    def overnight_pre(self) -> Tuple[Time, Time]:
        """Returns the first part of an overnight shift if overnight."""
        if self.overnight:
            return (self.start_hour, Time(23, 59))
        else:
            return self.time_tuple

    @property
    def overnight_post(self) -> Tuple[Time, Time]:
        """Returns the second part of an overnight shift if overnight."""
        if self.overnight:
            return (Time(0, 0), self.finish_hour)
        else:
            return self.time_tuple

    def shift_length(self) -> Time:
        """Returns the length of the shift."""
        return Time.delta(self.start_hour, self.finish_hour)

    def add_alternative_schedule(self, altshift: "Workshift") -> None:
        """Appends an alternative schedule if the shift is laid on a specific day."""
        if bool(self.days) and all(x not in self.days for x in altshift.days):
            raise AssertionError(
                "Alternative schedule needs to be defined \
                for a weekday that the workshift is valid."
            )
        self.alternative_schedule.append(altshift)


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
    laws: list = field(default_factory=list)
    hours: np.ndarray = field(default_factory=np.ndarray)
    employees: List[Employee] = field(default_factory=list)
    shifts: List[Workshift] = field(default_factory=list)
    assignments: Dict[Employee, Workshift] = field(default_factory=dict)

    @property
    def weekday(self) -> str:
        """Returns the weekday of the schedule as a string."""
        return calendar.day_name[self.date.weekday()]

    def assign_employee_to_shift(self, employee: Employee, shift: Workshift) -> None:
        """Assigns a Workshift to an Employee and adds a record to the Schedule."""
        if shift.alternative_schedule is not None:
            for altshift in shift.alternative_schedule:
                if self.date.weekday in altshift.days:
                    shift = altshift

        self.assignments[employee] = shift

    assign = assign_employee_to_shift


@dataclass
class Calendar:
    """Class that holds a schedule for each day."""

    daybyday: Dict[datetime.date, Schedule]

    def assign_employee_to_shift(
        self, date: datetime.date, employee: Employee, shift: Workshift
    ) -> None:
        """Assigns shift to employee on the date supplied."""
        self.daybyday[date].assign(employee, shift)
