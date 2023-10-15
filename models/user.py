#!/usr/bin/python3
"""Module contains User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """a class User that inherits from BaseModel
    Attributes:
        email: (str) - user's email
        password: (str) - user's password
        first_name: (str) - user's first name
        last_name: (str) - user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
