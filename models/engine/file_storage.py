#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a list of objects of one type, if class is provided
        or all objects if cls is None.
        """
        if cls is not None:
            # retrieve all objects
            cls_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    # if cls is found add item to cls_objects
                    cls_objects[key] = obj
            return cls_objects
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects"""
        # handle: obj is None
        if obj is not None:
            obj_key = "{}.{}".format(type(obj).__name__, obj.id)
            if obj_key in self.__objects:
                del self.__objects[obj_key]

    def close(self):
        """Calls reload method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """ Gets a specified object using its class and id """
        if cls is None or id is None:
            return None
        all_objs = storage.all(cls)
        key = "{}.{}".format(cls.__name__, id)

        return all_objs.get(key, None)

    def count(self, cls=None):
        """ Count all objects or objects of specified class """
        if cls is None:
            return len(storage.all())
        else:
            return len(storage.all(cls))
