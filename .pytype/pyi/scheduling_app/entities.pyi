# (generated with --quick)

import numpy
from typing import Callable, Type, TypeVar

np: module

_T = TypeVar('_T')

class Employee:
    experience: int
    happiness: float
    name: str
    preferences: list
    def __init__(self, name: str, experience: int, preferences: list, happiness: float) -> None: ...

class RegulatoryRequirements:
    laws: list
    def __init__(self, laws: list) -> None: ...

class Schedule:
    __doc__: str
    employees: list
    hours: numpy.ndarray
    laws: list
    def __init__(self, laws: list, hours: numpy.ndarray, employees: list) -> None: ...

class Workforce:
    employees: Type[list]
    def __init__(self) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
