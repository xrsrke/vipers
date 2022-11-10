# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01_compound.property.ipynb.

# %% auto 0
__all__ = ['Mass', 'MolarMass', 'Mole', 'Pressure', 'Volume', 'Temperature']

# %% ../../nbs/01_compound.property.ipynb 4
from exex.imports import *
from exex.core.unit import Unit
from exex.core.property import Property, ConstantProperty

# %% ../../nbs/01_compound.property.ipynb 7
class Mass(Property):
    def __init__(self, compound):
        super().__init__(compound)
        self.abbrv = "m"
        self.unit = Unit.MASS

# %% ../../nbs/01_compound.property.ipynb 8
class MolarMass(ConstantProperty):
    def __init__(self, compound):
        self.abbrv = "M"
        self.unit = Unit.MOLAR_MASS
        super().__init__(compound)
        self.is_constant = True

    def compute(self):
        mass = 0
        for element in self.compound.elements:
            mass += element.AtomicMass

        return mass * self.unit

# %% ../../nbs/01_compound.property.ipynb 9
class Mole(Property):
    def __init__(self, compound):
        super().__init__(compound)
        self.abbrv = "n"
        self.unit = Unit.MOLE

# %% ../../nbs/01_compound.property.ipynb 10
class Pressure(Property):
    def __init__(self, compound):
        super().__init__(compound)
        self.abbrv = "P"
        self.unit = Unit.PRESSURE

# %% ../../nbs/01_compound.property.ipynb 11
class Volume(Property):
    def __init__(self, compound):
        super().__init__(compound)
        self.abbrv = "V"
        self.unit = Unit.VOLUME

# %% ../../nbs/01_compound.property.ipynb 12
class Temperature(Property):
    def __init__(self, compound):
        super().__init__(compound)
        self.abbrv = "T"
        self.unit = Unit.TEMPERATURE
