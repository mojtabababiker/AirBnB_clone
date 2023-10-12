#!/usr/bin/python3
"""
base_model is the containing the base class for all the BnB models objects
BaseModle(self, *args, **kwargs)
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        Args:
            *args: won't be used.
            **kwargs (dict): dictonary  of attributes.
        """
        str_form = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, str_form)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """Prints: [<class name>] (<self.id>) <self.__dict__>"""
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        """Updates updated_at attribute with the current datetime"""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing pairs of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict


if __name__ == "__main__":
    base = BaseModel()
