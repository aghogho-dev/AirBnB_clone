#!/usr/bin/python3
"""Inside the console module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Inside the HBNBC class."""

    prompt = '(hbnb) '

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_EOF(self, line):
        "EOF command to exit the program"
        return True

    def emptyline(self):
        "Empty line doesn't execute"
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
