#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in dictionary the obj with key <obj class name>.id """
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as fname:
                objdict = json.load(fname)
                for key in objdict.values():
                    cls_name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(cls_name)(**key))
        except FileNotFoundError:
            return
