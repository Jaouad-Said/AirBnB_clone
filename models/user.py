#!/usr/bin/python3
"""User class model"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User's definition."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""