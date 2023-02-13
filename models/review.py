#!/usr/bin/python3
"""Inside the review module."""
from models.base_model import BaseModel



class Review(BaseModel):
    """Inside Review class.

    Attrs:
        place_id (str): id place.
        user_id (str): id user.
        text (str): review.
    """
    place_id = ""
    user_id = ""
    text = ""
