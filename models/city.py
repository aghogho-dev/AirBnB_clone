#!/usr/bin/python3
"""Iniside the city module."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class.

    Attrs:
        state_id (str): id state.
        name (str): city name.
    """
    state_id = ""
    name = ""
