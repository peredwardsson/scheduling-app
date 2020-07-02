# (generated with --quick)

import click.core
import scheduling_app.entities
from typing import Type

Employee: Type[scheduling_app.entities.Employee]
FIRSTCOL: int
MIDADJUST: int
Schedule: Type[scheduling_app.entities.Schedule]
Workforce: Type[scheduling_app.entities.Workforce]
__version__: str
click: module
datetime: Type[datetime.datetime]
main: click.core.Command
np: module

def generate_test_employee(name = ...) -> scheduling_app.entities.Employee: ...
def init_workforce() -> scheduling_app.entities.Workforce: ...
def month_int_to_str(month_idx: int) -> str: ...
def print_schedule(schedule: scheduling_app.entities.Schedule) -> None: ...
def schedule_employees(s: scheduling_app.entities.Schedule) -> None: ...
