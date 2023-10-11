#!/usr/bin/env python3
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

    def __init__(self):
        """
        Consitructer for the class
        """

        self.__file_path = r"models/engine/file.json"
        self.__objects = dict()

    def all(self) -> dict:
        """
        all    return a dictionery consists of all the objects instances of
               the BnB models

        Syntax:
            FileStorage.all()

        Return:
            A dictionery contains BnB models instances
        """

        return self.__objects

    def new(self, obj: object):
        """
        new    add the obj information to the BnB objects dictionery

        Syntax:
            FileStorage.new(self, obj)
        """

        obj_value = obj.to_dict()
        obj_key = obj_value["__class__"]+"."+obj_value["id"]

        self.__objects[obj_key] = obj_value

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

        with open(self.__file_path, "w", encoding="utf-8") as fh:
            json.dump(self.__objects, fh, indent=2)

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

        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as fh:
                loded_obj = json.load(fh)
            self.__objects.update(loded_obj)
