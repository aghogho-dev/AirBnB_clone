#!/usr/bin/python3
"""Inside the base_model module."""
from uuid import uuid4
from datetime import datetime as dt
from models import storage


class BaseModel:
    """Inside the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel instance.

        Args:
            *args: variable non-keyword args.
            **kwargs: variable named args.
        """

        self.id = str(uuid4())
        self.created_at = dt.now()
        self.updated_at = dt.now()

        if kwargs:
            for key in kwargs:
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = dt.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            storage.new(self)


    def save(self):
        """Update update_at."""
        self.updated_at = dt.now()
        storage.save()

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

