#!/usr/bin/python3
"""Module contains  Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """a class Review that inherits from BaseModel
    Attributes:
        place_id: (str) - will be the Place.id
        user_id: (str) - will be the User.id
        text: (str) - review
    """
    place_id = ""
    user_id = ""
    text = ""
