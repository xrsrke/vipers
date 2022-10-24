# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_system.ipynb.

# %% auto 0
__all__ = ['System']

# %% ../nbs/00_system.ipynb 4
from .imports import *
from .core import *

# %% ../nbs/00_system.ipynb 5
@docs
class System(metaclass=PrePostInitMeta):
    def __init__(
        self,
        reactions = [] # list of reactions
    ):
        self.universe = None
        self.current_time: int = None
        self.highest_time: int = None
        self.reactions: list = reactions
        self._subscribers = dict()
        self.idx_reaction: int = None
    
    def __post_init__(self, *args, **kwargs):
        self._setup_reaction()
    
    def _setup_reaction(self) -> None:
        if len(self.reactions) < 1: return
        for name, compound in self.reactions[0].compounds.items():
            compound._set_system(self)

    def reaction(
        self,
        idx: int # the index of the reaction
    ): # the reaction
        
        if idx > len(self.reactions): return 'Sorry. idx too big'
        
        self.idx_reaction = idx
        return self
    
    _docs = dict(cls_doc='A container that acts as a mediator help compound, reaction and universe communicate to each other',
                 reaction='',)

# %% ../nbs/00_system.ipynb 6
_msg = dict(
    no_property = "Can't find the property"
)

# %% ../nbs/00_system.ipynb 8
@patch
def get_prop(self: System, name: str, t: int, instance, **kwargs):
    return instance.properties[name](t, **kwargs)

# %% ../nbs/00_system.ipynb 9
@patch
def set_prop(self: System, name, val, t, instance, **kwargs):        
    return instance.properties[name].set_val(val, t, **kwargs)
