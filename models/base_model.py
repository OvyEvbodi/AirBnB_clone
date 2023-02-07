#!/usr/bin/python3

"""This module defines a base class ``BaseModel``
from which all Airbnb classes inherit attributes and methods"""

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(unsafe_hash=True)
class BaseModel:
    """Defines a base class for Airbnb objects
    Attributes:
        id (str): the universal unique identifier of a BaseModel instance
        created_at (datetime): the time of creation of a BaseModel instance
        updated_at (datetime): the last time a BaseModel instance was updated
    """

    id: str = str(uuid4())
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __str__(self):
        """Updates the string representation of a BaseModel instance
        Returns:
            a string representation of a BaseModel instance"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute ``updated_at``
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dctionary representation of an instance"""

        dict_repr = self.__dict__
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr

#=========================test==================================
if __name__ == "__main__":
    base = BaseModel()
    print(base.created_at)
    print(base)
    print(base.updated_at)
    print(base.id)
    print()
    print(base.to_dict)
    print()
    print(base.__dict__)
