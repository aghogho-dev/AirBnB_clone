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
        print("")

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("EOF command to exit the program")
        print("")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
