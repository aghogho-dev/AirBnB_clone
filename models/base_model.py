#!/usr/bin/python3
"""Inside the base_model module."""
from uuid import uuid4
from datetime import datetime as dt


class BaseModel:
    """Inside the BaseModel class."""

    def __init__(self):
        """Initialize the BaseModel instance."""

        self.id = str(uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def save(self):
        """Update update_at."""

        self.updated_at = dt.now()

    def __str__(self):
        """Representation of the BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Dictionary of the BaseModel.
        
        Return: Dict.
        """

        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()

        return copy_dict

