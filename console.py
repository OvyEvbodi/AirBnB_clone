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

    Attributes:
        prompt (str): the prefix prompt
        to be displayed during cmdloop's runtime
    """

    prompt = "(hbnb) "
    intro = "----Welcome to hbnb!----\nEnter \"help\" or \"?\" to get started."
    __valid_classes = ["BaseModel", "User", "Place", "State", "City",
                       "Amenity", "Review"]
    __valid_commands = {"create": "create", "count": "count",
                        "all": "all", "show": "show",
                        "destroy": "destroy", "update": "update"}
    __no_args_cmds = {"create()": "create", "all()": "all", "count()": "count"}

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
        saves it (to the JSON file), and prints the id
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

    def help_create(self):
        """Prints the usage of the show method"""
        print("syntax: create <class name> or <class name.create>")
        print(f"Creates a new instance of BaseModel,",
              "saves it (to the JSON file), and prints the id")

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

    def help_show(self):
        """Prints the usage of the show method"""
        print("syntax: show <class name> <id> or <class name>.show(<id>)")
        print("Prints the string representation of",
              "an instance based on the class name and id")

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
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        """Prints the usage of the destroy method"""
        print(f"syntax: destroy <class name> <id>",
              "or <class name>.destroy(<id>)")
        print(f"Deletes an instance based on the class name",
              "and id (save the change into the JSON file)")

    def do_all(self, line):
        """Prints all string representation of all instances
        based on the class name or not
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

    def help_all(self):
        """Prints the usage of the all method"""
        print(f"syntax: all or all <class name> or <class name>.all()")
        print(f"Prints all string representations of all instances",
              "based on the class name or not")

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
                            # value = eval(obj_attr_type(value))
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

    def help_update(self):
        """prints the usage of the update method"""
        print(f"syntax: update <class name> <id>",
              "<attribute name> \"<attribute value>\" or",
              "<class name>.update(<id>, <attribute name>, <attribute value>)")
        print(f"Updates an instance based on the class name and id by adding",
              "or updating attribute (save the change into the JSON file).",
              'Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"')

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        count = 0
        for key in storage.all():
            if key.split(".")[0] == line:
                count += 1
        print(count)

    def help_count(self):
        """prints the usage of the count method"""
        print(f"syntax: <class name>.count()")
        print(f"Retrieves the number of instances of a class")

    def precmd(self, line: str) -> str:
        args = line.split(".")
        if len(args) >= 2:
            class_name, command = args[0], args[1].split("(")[0]
            if class_name in HBNBCommand.__valid_classes:
                if command in HBNBCommand.__valid_commands:
                    command = args[1]
                    if command in HBNBCommand.__no_args_cmds:
                        new_line = HBNBCommand.__no_args_cmds[command] \
                            + " " + class_name
                        return super().precmd(new_line)
                    else:
                        line_list = args[1].split("(")
                        if line_list:
                            command = line_list[0]
                            new_line = command + " " + class_name
                            if len(line_list) >= 2:
                                line_list = line_list[1].strip(")")
                                args_list = line_list.split(",")
                                if len(args_list) <= 1:
                                    id_arg = line_list.strip('"')
                                    new_line += " " + id_arg
                                else:
                                    for arg in args_list:
                                        new_line += " " + arg.strip(' "')
                            return super().precmd(new_line)
                else:
                    return super().precmd(line)
        else:
            return super().precmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
