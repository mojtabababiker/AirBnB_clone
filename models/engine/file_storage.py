#!/usr/bin/python3
"""
A Storage Engine based on file storage mechanisim and the JSON format.
This model is used to create a presistent copy of all the BnB models objects
in the form of a json file
"""

import json
import os.path


class FileStorage:
    """
    Syntax:
        FileStorage()

    Description:
        Creates a presistent copy of the BnB models objects in the form of
        json file

        FileStorage.all(self):
            returns a dicitionery consists of all the objects of the Bnb models
        FileStorage.new(self, obj):
            Update the objects dictionery with the
            <obj.__class__.__name__>.<obj.id> as the key
            and obj.to_dict() as its value

        FileStorage.save(self):
            Serializes the objects dictionery to a JSON file

        FileStorage.reload(self):
            Deserializes the JSON file to the objects dictionery
    """

    __file_path = r"file.json"
    __objects = dict()

    def all(self) -> dict:
        """
        all    return a dictionery consists of all the objects instances of
               the BnB models

        Syntax:
            FileStorage.all()

        Return:
            A dictionery contains BnB models instances
        """

        return FileStorage.__objects

    def new(self, obj: object):
        """
        new    add the obj information to the BnB objects dictionery

        Syntax:
            FileStorage.new(self, obj)
        """

        __obj_key = obj.__class__.__name__ + '.' + obj.id

        FileStorage.__objects[__obj_key] = obj

    def save(self):
        """
        save   save the BnB objects dictionery into a JSON file

        Syntax:
            FileStoarge.save()

        Descriptons:
            `save` saves all the BnB objects instances to a JSON file, in the
             form of json key:value pairs.
             If the file dose not exists the `save` will creates a new one, if
             it's already exist it will be over-written
        """

        __objects_dict = dict()
        for key, obj in FileStorage.__objects.items():
            __objects_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as fh:
            json.dump(__objects_dict, fh)

    def reload(self):
        """
        reload    load the contents of the json file to the BnB objects
                  instances dictionery

        Syntax:
            FileStorage.load()

        Descriptions:
            `reload` get the contents of the json file and converts them into
             python dictionery, and the value of the BnB objects instances
             dictionery will be updated with it.
        """
        from models.models import BaseModel, User, State, City
        from models.models import Amenity, Place, Review

        __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fh:
                __objects_dict = json.load(fh)
            for key, obj in __objects_dict.items():
                __instance = __classes[obj["__class__"]](**obj)
                FileStorage.__objects[key] = __instance
