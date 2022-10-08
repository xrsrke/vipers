# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/0_utils.ipynb.

# %% auto 0
__all__ = ['camel_to_snake']

# %% ../nbs/0_utils.ipynb 4
import re

from fastcore.test import test_eq

# %% ../nbs/0_utils.ipynb 6
def camel_to_snake(
    name: str # the string that you want to convert
    ) -> str: # converted string
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
