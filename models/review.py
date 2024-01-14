#!/usr/bin/python3
"""User Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """DClass Review's definition"""

    place_id = ""
    user_id = ""
    text = ""