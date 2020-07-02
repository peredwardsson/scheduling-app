"""This script generates workshifts saves into a json file for further use."""

import os
import pickle
from typing import List

from .entities import Time, Workshift, Workshift_base


def generate() -> List[Workshift]:
    """Generates workshifts and saves them if none are found."""
    shifts = []

    shifts.append(Workshift("a-tur", Time(7), Time(15), [0, 1, 2, 3, 4]))
    shifts.append(Workshift("c-tur", Time(13, 30), Time(21, 30), [0, 1, 2, 3, 4]))
    poptur = Workshift("p-op-tur", Time(9), Time(17), [0, 1, 2, 3, 4])
    poptur.add_alternative_schedule(
        Workshift_base("p-op-tur fredag", Time(10), Time(19), [4])
    )
    shifts.append(poptur)
    # shifts.append(Workshift("natt", Time(21), Time(7, 30), days=[0, 1, 2, 3, 4]))
    filename = "test_data/workshifts.pkl"
    if not os.path.isfile(filename):
        with open("test_data/workshifts.pkl", "wb") as f:
            pickle.dump(shifts, f)
        return shifts
    else:
        return shifts
