#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        obj_dict = {}
        # get the class name
        name = cls.__name__
        # iterate through the key values of my __object dict
        for k in FileStorage.__objects.keys():
            # I extract the class name from the . id
            if k.split('.')[0] == name:
                # I populate my dict with the objects of the same kind
                obj_dict[k] = FileStorage.__objects[k]
        return obj_dict

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
        """ Function that deletes obj in __object if it is inside
            - if obj is not inside, it does nothing
        """
        if obj is None:
            return
        new_obj = obj.to_dict()
        class_name = new_obj['__class__']
        obj_id = obj.id
        key_obj = class_name + '.' + obj_id
        if key_obj in self.__object.keys():
            print(key_obj)
            del self.__objects[key_obj]
