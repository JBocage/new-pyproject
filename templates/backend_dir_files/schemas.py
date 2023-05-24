"""Defines payload structures"""
from pydantic import BaseModel


class AddPayload(BaseModel):
    """Payload example"""

    first_number: int
    second_number: int
