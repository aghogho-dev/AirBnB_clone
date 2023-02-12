#!/usr/bin/python3
"""Inside the console module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Inside the HBNBC class."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")

    def emptyline(self):
        pass

    def help_emptyline(self):
        print("Emptyline does not execute")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
