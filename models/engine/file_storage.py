#!user/bin/python3
"""Module filestorage."""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Definition of class FileStorage."""

    __file_path = "file.json"
    __objects = {}
    """Public instance methods."""
    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf_8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the json file."""
        try:
            path = FileStorage.__file_path
            with open(path, mode="r", encoding="utf_8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = BaseModel
                    if class_name == 'BaseModel':
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == 'User':
                        cls = User
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == 'State':
                        cls = State
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == 'City':
                        cls = City
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == 'Amenity':
                        cls = Amenity
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == 'Place':
                        cls = Place
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    elif class_name == 'Review':
                        cls = Review
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    else:
                        pass
        except FileNotFoundError:
            pass
