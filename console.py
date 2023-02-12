#!/usr/bin/python3
"""Inside the console module."""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Inside the HBNBC class."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print("")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")
        print("")

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        else:
            if line != "BaseModel":
                print("** class doesn't exist **")
            else:
                print(eval(line)().id)
                storage.save()

    def help_create(self):
        print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id")
        print("")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        elif "BaseModel" not in line:
            print("** class doesn't exist **")
        else:

            sline = line.split()
            dict_obj = storage.all()
            
            if len(sline) != 2:
                print("** instance id missing **")
            elif "{}.{}".format(sline[0], sline[1]) not in dict_obj:
                print("** no instance found **")
            else:
                print(dict_obj["{}.{}".format(sline[0], sline[1])])

    def help_show(self):
        print(" Prints the string representation of an instance based on the class name and id.")
        print("")

    def do_destroy(self, line):
        dict_obj = storage.all()
        sline = line.split()

        if not line:
            print("** class name missing **")
        elif "BaseModel" not in line:
            print("** class doesn't exist **")
        elif len(sline) != 2:
            print("** instance id missing **")
        elif "{}.{}".format(sline[0], sline[1]) not in dict_obj:
            print("** no instance found **")
        else:
            del dict_obj["{}.{}".format(sline[0], sline[1])]
            storage.save()

    def help_destroy(self):
        print(" Deletes an instance based on the class name and id (save the change into the JSON file)")
        print("")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
