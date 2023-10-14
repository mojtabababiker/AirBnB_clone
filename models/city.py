#!/usr/bin/python3
"""Module contains City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """a class City that inherits from BaseModel
    Attributes:
        state_id: (str) - State.id
        name: (str) - city's mane
    """
    state_id = ""
    name = ""
