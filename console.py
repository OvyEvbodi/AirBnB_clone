#!/usr/bin/python3
"""Entry point of the command interpreter for the AirBnb clone"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the HBNB command line interpreter
    This class inherits from cmd's ``Cmd`` class
    """

    prompt = "(hbnb) "

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
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif  not isinstance(line, BaseModel):
            print("** class doesn't exist **")
        else:
            new_obj = eval[line]()
            new_obj.save()
            print(new_obj.id)

    def do_show(self):
        """Prints the string representation of
        an instance based on the class name and id
        """
        if line:
            class_name, class_id = line.split(" ")
            if not class_name:
                print("** class name missing **")
            elif not isinstance(class_name, BaseModel):
                print("** class doesn't exist **")
            else:
                if not class_id:
                    print("** instance id missing **")
                else:
                    for key, value in storage.all().items():
                        if class_id == value.id:
                            print(str(value))
                            return
                    print("** no instance found **")
    def do_destroy(self):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        if line:
            class_name, class_id = line.split(" ")
            if not class_name:
                print("** class name missing **")
            elif not isinstance(class_name, BaseModel):
                print("** class doesn't exist **")
            else:
                if not class_id:
                    print("** instance id missing **")
                else:
                    dict_repr = storage.all()
                    for key, value in dict_repr.items():
                        if class_id == value.id:
                            del dict_repr[key]
                            storage.save()
                            return
                    print("** instance id missing **")

    def do_all(self):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if not line:
            for key, value in storage.all().items():
                print(str(value))
        else:
            if isinstance(line, BaseModel)
                for key, value in storage.all().items():
                    if line == value['__class__']:
                        print(str(value))

    def do_update(self):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com
        """"
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

