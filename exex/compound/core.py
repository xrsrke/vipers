# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01_compound.core.ipynb.

# %% auto 0
__all__ = ['Compound']

# %% ../../nbs/01_compound.core.ipynb 4
from dataclasses import dataclass
import chemlib

from ..imports import *
from ..core.all import *
from ..utils import *
from .law import *

# %% ../../nbs/01_compound.core.ipynb 6
@docs
class Compound(Matter):

    LAWS = [MassMoleRatio]

    def __init__(self, formula: str) -> None:  # the chemical formula
        super().__init__()

        compound = chemlib.Compound(formula)
        self.add_laws = [MassMoleRatio]
    
        self.set_elements(compound.elements)

        self.formula = compound.formula
        self.str_formula = formula
        
        self.coefficient = compound.coefficient
        self.occurences = compound.occurences

        self._setup_laws([MassMoleRatio])
    
    @property
    def formula(self) -> str:
        return self._unicode_formula
    
    @formula.setter
    def formula(self, formula: str) -> None:
        self._unicode_formula = formula
    
    @property
    def snake_name(self) -> str:  # return the snake name style
        return self.str_formula
    
    @property

    def get_data(self, time: int, name: str):  # the time  # the property name
        if not name in self.properties:
            return "The property don't exist"
        pass

    def __repr__(self):
        return f"Compound({self.formula})"

    _docs = dict(cls_doc="Compound",
                 get_data="",
                 snake_name="the snake name style"
                )

# %% ../../nbs/01_compound.core.ipynb 7
@patch(as_prop=True)
def elements(self: Matter): # return elements of the compound
    return self._elements

# %% ../../nbs/01_compound.core.ipynb 8
@patch
def set_elements(self: Matter, elements):
    self._elements = elements

# %% ../../nbs/01_compound.core.ipynb 10
@patch(as_prop=True)
def coeffs(self: Compound):
    return self._coeffs

# %% ../../nbs/01_compound.core.ipynb 11
@patch
def info(self: Compound, **kwargs): # the info
    dta = {}

    for k, v in self.properties.items():
        # data_point = {}
        # print(v._data)
        key = k
        # if v.unit:
        #     key += f' ({v.unit})'

        dta[key] = v._data

    df = pd.DataFrame(data=dta, **kwargs)
    df.index.name = "Time"
    return df.sort_index()
