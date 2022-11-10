# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00b_core.symbolic.ipynb.

# %% auto 0
__all__ = ['Symbol', 'Function', 'Equation']

# %% ../../nbs/00b_core.symbolic.ipynb 4
from exex.imports import *

# %% ../../nbs/00b_core.symbolic.ipynb 6
@docs
class Symbol(sympy.core.symbol.Symbol):
    def __new__(cls, name: str):
        _obj = sympy.core.symbol.Symbol.__new__(cls, name)
        return _obj

    def set_data(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    _docs = dict(cls_doc="The symbol", set_data="Set data", data="Set data")

# %% ../../nbs/00b_core.symbolic.ipynb 7
@patch(as_prop=True)
def is_evaled(self: Symbol): # Check whether the symbol is evaluated
    pass

# %% ../../nbs/00b_core.symbolic.ipynb 20
class Function(sympy.core.function.Function):
    def __new__(cls, name):
        _obj = sympy.core.function.Function.__new__(cls, name)
        return _obj

# %% ../../nbs/00b_core.symbolic.ipynb 24
class Equation:
    ...
