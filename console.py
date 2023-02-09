#!/usr/bin/python3
"""Entry point of the command interpreter for the AirBnb clone"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command line interpreter
    This class inherits from cmd's ``Cmd`` class
    """

    prompt = "(hbnb) "
    # __valid_classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
    #                    "State": State, "City": City, "Amenity": Amenity,
    #                    "Review": Review}

    __valid_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity",
                        "Review"]

    def do_EOF(self, line):
        """End Of File"""
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """Does nothing when an empty line + ENTER is passed"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        and saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__valid_classes:
            print(line, type(line))
            print("** class doesn't exist **")
        else:
            new_obj = eval(line + "()")
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id
        """
        if line:
            args = line.split(" ")
            if args[0] not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    for key, value in storage.all().items():
                        if args[1] == value.id:
                            print(str(value))
                            return
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if line:
            args = line.split(" ")
            if args[0] not in HBNBCommand.__valid_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    dict_repr = storage.all()
                    for key, value in dict_repr.items():
                        if args[1] == value.id:
                            del dict_repr[key]
                            storage.save()
                            return
                    print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        all_list = []
        if not line:
            for key, value in storage.all().items():
                all_list.append(str(value))
            print(all_list)
        else:
            if line in HBNBCommand.__valid_classes:
                for key, value in storage.all().items():
                    if line == key.split(".")[0]:
                        all_list.append(str(value))
                print(all_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if line:
            args = line.split(" ")
            if args[0] in HBNBCommand.__valid_classes:
                if len(args) >= 2:
                    found = False
                    for key, value in storage.all().items():
                        if args[1] == value.id:
                            found = True
                            dict_key = key
                            break
                    if len(args) >= 3:
                        if len(args) >= 4:
                            obj_repr = storage.all()
                            attribute = args[2]
                            if args[3][0] == '"':
                                value = args[3].split("\"")[1]
                                i = 4
                                while args[i] and args[i][-1] != '"':
                                    value += " " + args[i]
                                    i += 1
                                value += " " + args[i].split("\"")[0]
                            else:
                                value = args[3]
                            obj_attr = getattr(obj_repr[dict_key], attribute)
                            obj_attr_type = type(obj_attr)
                            attribute = str(attribute)
                            #attribute = eval(obj_attr(attribute))
                            setattr(obj_repr[dict_key], attribute, value)
                            obj_repr[dict_key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                    if not found:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
