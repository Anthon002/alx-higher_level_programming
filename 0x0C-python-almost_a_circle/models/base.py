#!/usr/bin/python3
""" this module contains the Base class
"""


class Base:
    """ this is the Base class """
    __nb_objects = 0
    def __init__(self, id = None):
        if (id != None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a file in JSON format.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.convert_to_json(dict_list)
                json_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a Python list.

        Args:
            json_string (str): A JSON string representation of a list of dictionaries.

        Returns:
            list: The Python list represented by the JSON string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an object instance from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize the object.

        Returns:
            object: An instance of the class with the specified attributes.
        """
        if attributes and attributes != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects from a JSON file.

        Reads from '<cls.__name__>.json'.

        Returns:
            list: A list of instantiated objects.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                json_string = json_file.read()
                dict_list = Base.convert_from_json(json_string)
                return [cls.create_object(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes a list of objects to a CSV file.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of objects from a CSV file.

        Reads from '<cls.__name__>.csv'.

        Returns:
            list: A list of instantiated objects.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                dict_list = [dict([(k, int(v)) for k, v in d.items()]) for d in reader]
                return [cls.create_object(**d) for d in dict_list]
        except IOError:
            return []

