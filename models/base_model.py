#!/usr/bin/python3
"""Base module class"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """BaseModel's class definition"""

    def __init__(self, *args, **kwargs):
        """Const declaration."""
        format = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, format))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Print human readble str of an object."""
        cls_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
    """Public instance methods."""
    def save(self):
        """Update the attribute updated_at."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of an object."""
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict