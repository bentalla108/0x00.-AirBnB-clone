#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
"Base Model "


class BaseModel():
    """BaseModel class definies"""
    def __init__(self, *args, **kwargs):

        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Strings representation of a class"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionnary of all keys and value of __dict___"""

        selfDict = self.__dict__.copy()
        selfDict['__class__'] = self.__class__.__name__
        selfDict['created_at'] = self.created_at.isoformat()
        selfDict['updated_at'] = self.updated_at.isoformat()

        return selfDict
