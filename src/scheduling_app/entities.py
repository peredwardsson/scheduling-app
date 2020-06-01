from dataclasses import dataclass

import numpy as np

# import pandas as pd


@dataclass
class Employee:
    name: str
    experience: int
    preferences: list
    happiness: float


@dataclass
class BusinessRequirements:
    hours: np.array


@dataclass
class RegulatoryRequirements:
    laws: list


@dataclass
class Schedule:
    week: int
    requirements_regulatory: RegulatoryRequirements
    requirements_business: BusinessRequirements
    employees: list
