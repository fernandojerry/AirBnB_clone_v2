#!/usr/bin/python3
""" Class BaseModel """
from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """ BaseModel construction """

    def __init__(self, *args **kwargs):
        """ initialize a new BaseModel """

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                     self.__dict__[k] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

     def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

     def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

     def to_dict(self):
        """  returns a dictionary containing all keys/values of __dict__ of the              instance:
        """
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        ret_dict["__class__"] = self.__class__.__name__
        return ret_dict
