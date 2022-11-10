# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00b_core.unit.ipynb.

# %% auto 0
__all__ = ['ureg', 'Q', 'Unit', 'unit2expr']

# %% ../../nbs/00b_core.unit.ipynb 4
from dataclasses import dataclass
from abc import ABC, abstractmethod

from exex.imports import *

# %% ../../nbs/00b_core.unit.ipynb 7
class Unit:
    """
    Default SI Units
    """

    LENGTH = u.meter
    MASS = u.kilogram
    TIME = u.second
    TEMPERATURE = u.kelvin

    """
    Derived from SI Units
    """
    MOLAR_MASS = u.gram / u.mole
    MOLE = u.mole
    SPECIFIC_HEAT = u.joule / (u.kilogram * u.kelvin)
    PRESSURE = u.pascal
    VOLUME = u.liter

# %% ../../nbs/00b_core.unit.ipynb 8
def unit2expr(unit):
    pass

# %% ../../nbs/00b_core.unit.ipynb 12
ureg = pint.UnitRegistry(system="SI")
Q = ureg.Quantity  # quantity
