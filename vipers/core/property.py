# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00c_core.property.ipynb.

# %% auto 0
__all__ = ['Object', 'PropertyData', 'Property', 'ConstantProperty', 'PropertyObservable']

# %% ../../nbs/00c_core.property.ipynb 5
from abc import abstractmethod
from typing import Dict, List, Optional

from ..imports import *
from .event import *
from .unit import *
from ..utils import camel_to_snake

# %% ../../nbs/00c_core.property.ipynb 7
class Object:
    pass

# %% ../../nbs/00c_core.property.ipynb 8
class PropertyData(dict):
    pass

# %% ../../nbs/00c_core.property.ipynb 13
class _BaseProperty:
    def __init__(self):
        self._data: Dict[str, Any] = dict()
        self._laws: Dict[str, Any] = dict()
        # self._stat

# %% ../../nbs/00c_core.property.ipynb 14
@docs
class _BaseProperty:
    def __init__(self, cmp):  # chemical substance
        self.is_constant: bool = False
        self._cmp = cmp
        self._data = PropertyData()

        self._laws = dict()
        
        #self._connections = []
        #self.func_changed = Event()
    
    def __call__(self, t: int, eval: bool = False, **kwargs):  # time
        self.t = t
        self.kwargs = {**kwargs, "eval": eval}

        expr = self.expr(t)

        if eval == True:
            return self.eval(expr, t)
        else:
            return expr

    @property
    def name(self) -> str:
        return camel_to_snake(self.__class__.__name__)

    @classmethod
    @property
    def snake_name(cls) -> str:  # return the snake style name
        return camel_to_snake(cls.__name__)
    
    @property
    def compound(self):
        return self.cmp
    
    @property
    def cmp(self):
        return self._cmp
    
    @cmp.setter
    def cmp(self, cmp):
        self._cmp = cmp
    
    @property
    def data(self):
        return self._data
    
    @property
    def laws(self): # get a list of laws that asscoiated to this property
        return self._laws
    
    @laws.setter
    def laws(self, laws):
        return self._laws
    
    def expr(self, t: int):  # time
        return self.symbol(t)

    def add_law(self, law):
        if not law in self.laws:
            self.laws[camel_to_snake(law.__class__.__name__)] = law
    
    def remove_law(self, law): pass

    _docs = dict(cls_doc="Property",
                 add_law="",
                 remove_law="",
                 expr="Symbolic expression")

# %% ../../nbs/00c_core.property.ipynb 15
@patch
def symbol(self: _BaseProperty, t):  # symbolic expression of the property
    """Rewrite this method if you want to modify"""
    return smp.symbols(f"{self.abbrv}_{self.cmp.snake_name}-{t}", real=True)

# %% ../../nbs/00c_core.property.ipynb 16
@patch
def set_val(self: _BaseProperty, val: str, t: int):
    self._data[t] = {"val": val}

# %% ../../nbs/00c_core.property.ipynb 17
@patch
def get_val(self: _BaseProperty, t: int):  # time
    if self.is_constant is True:
        return self.compute()
    else:
        return self._data[t]["val"] if t in self._data else self.symbol(t)

# %% ../../nbs/00c_core.property.ipynb 18
@patch
def eval(self: _BaseProperty, expr, t: int):  # express  # time
    return expr.xreplace({expr: self.get_val(t=t)})

# %% ../../nbs/00c_core.property.ipynb 19
@patch
def is_empty(self: _BaseProperty, t):
    return type(self.get_val(t))
    # return True if isinstance(type(self.get_val(t)), sympy.core.symbol.Symbol) else False

# %% ../../nbs/00c_core.property.ipynb 22
@docs
class Property(_BaseProperty):
    _docs = dict(cls_doc="Property that varies in time")

# %% ../../nbs/00c_core.property.ipynb 24
@docs
class ConstantProperty(Property):
    @abstractmethod
    def compute(self):
        pass

    _docs = dict(
        cls_doc="Property that invariant in time", compute="Calculate the value"
    )

# %% ../../nbs/00c_core.property.ipynb 26
class PropertyObservable(Property):
    pass