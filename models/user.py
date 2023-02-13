#!/usr/bin/python3
"""Inisde the user module."""
from models.base_model import BaseModel


class User(BaseModel):
    """Inside the User class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
