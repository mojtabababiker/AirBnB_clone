#!/usr/bin/python3
"""Module contains Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """a class Amenity inherits from BaseModel
    Attributes:
        name: (str) - Amenity's name
    """
    name = ""
