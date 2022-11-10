# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00_core.system.ipynb.

# %% auto 0
__all__ = ['System']

# %% ../../nbs/00_core.system.ipynb 4
from ..imports import *

# %% ../../nbs/00_core.system.ipynb 6
@docs
class System(metaclass=PrePostInitMeta):
    def __init__(self, reactions=[]):  # list of reactions
        self._universe = None
        self._current_time: int = None
        self._highest_time: int = None
        self._reactions: list = reactions
        self._subscribers = dict()
        self._idx_rxn: int = None

    def __post_init__(self, *args, **kwargs):
        self._setup_reaction()

    def _setup_reaction(self) -> None:
        if len(self.reactions) < 1: return
        
        for name, compound in self.reactions[0].compounds.items():
            compound._set_system(self)
    
    @property
    def universe(self):
        return self._universe
    
    @universe.setter
    def universe(self, unv):
        self._universe = unv
    
    @property
    def reactions(self):
        return self._reactions
    
    @property
    def rxns(self):
        return self._reactions
    
    @rxns.setter
    def rxns(self, rxns):
        self._reactions = rxns
    
    @property
    def num_rxns(self) -> int:
        return len(self.reactions)
    
    @property
    def idx_rxn(self) -> int:
        return self._idx_rxn
    
    @idx_rxn.setter
    def idx_rxn(self, idx: int): # the index of the reaction  # the reaction
        self._idx_rxn = idx
    
    # def set_idx_rxn(
    #     self, idx: int # the index of reaction in self.reactions
    # ):
    #     self._idx_rxn = idx

    def reaction(self, idx: int):  # the index of the reaction  # the reaction

        if idx > self.num_rxns:
            return "Sorry. idx too big"

        self.idx_rxn = idx
        return self

    _docs = dict(
        cls_doc="A container that acts as a mediator help compound, reaction and universe communicate to each other",
        reaction="",
    )

# %% ../../nbs/00_core.system.ipynb 7
_msg = dict(no_property="Can't find the property")

# %% ../../nbs/00_core.system.ipynb 9
@patch
def get_coeff(self: System, cmp):
    return

# %% ../../nbs/00_core.system.ipynb 10
@patch
def get_prop(self: System, name: str, t: int, instance, **kwargs):
    return instance.properties[name](t, **kwargs)

# %% ../../nbs/00_core.system.ipynb 11
@patch
def set_prop(self: System, name, val, t, instance, **kwargs):
    return instance.properties[name].set_val(val, t, **kwargs)

# %% ../../nbs/00_core.system.ipynb 12
@patch
def get_law(self: System, name, t, instance, **kwargs):
    return instance.laws[name](t, **kwargs)
