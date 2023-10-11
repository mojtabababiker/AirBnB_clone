#!/usr/bin/env python3
"""
console model is the code entry point for the AirBnB console project
the console or the command line interpeter was build on the cmd.CMD
python class.

How to run it:
    1] Interactive mode:
        run it as executable file, or by python as model, eg..,
            `$ ./console.py`
            `$ python3 -m console.py`
    2] Non-Interactive mode:
        also can be used to execute a single command/script and exite
        after finsh, eg..,
             `$ echo '<command> <args>' | ./console.py`
             `$ ./console.py <command> <args>`
"""

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Syntax:
       console.HBNBCommand(*args, **kwargs)

    Description:
        This class represent the command line interpeter of the AirBnB
        project, which provides rich services for creating, editing,
        and more
    """

    prompt = "(hbnb) "
    __interactive = True
    __classes = {
        "BaseModel": BaseModel
        }

    def preloop(self):
        """
        Check if the session is interactive session or non interactive
        """
        HBNBCommand.__interactive = sys.stdin.isatty()

    def do_help(self, line):
        """
        Overrides the Cmd.do_help function to add some line before and
        after printing the help strings
        """
        __docfun = ['EOF', 'all', 'creat', 'destroy', 'help',
                    'quit', 'show', 'update']
        if not HBNBCommand.__interactive:
            print()
        if len(line) > 0:
            super().do_help(line)

        else:
            print()
            print("Documented commands (type help <topic>):")
            print("========================================")
            for i in range(len(__docfun) - 1):
                print(__docfun[i], end='  ')
                if not HBNBCommand.__interactive:
                    print(__docfun[-1])

                else:
                    print(__docfun[-1])
                    print()

    def do_quit(self, *args):
        """
        Exit the interpeter immediately, no wait for the calling processes
        """
        if not HBNBCommand.__interactive:
            print()

        return True

    def do_EOF(self, *args):
        """
        Exit the interpeter at the end of file or when pressing `^D`
        """
        print()
        return True

    def emptyline(self, *args):
        """
        Handle the empty line
        """
        if not HBNBCommand.__interactive:
            print()

        pass

    def get_args(self, line):
        """
        Preprocessing the line from the interpeter before passing it
        to the onecmd() function.
        in this case we will handel the double qouted text, beside
        extracting args from line
        """
        qouted_args = line.split('"')  # search for qouted arguments
        args = qouted_args[0].split()  # split the rest of the args by space
        if len(qouted_args) > 1:  # if there are qouted args
            args.append(qouted_args[1])  # append them to args list
        return (args)

    def validate(self, args, args_num):
        """
        Validate the commands arguments, and print the excpected error
        message

        Args:
            args: the command line arguments list to validare
            args_num: the number of arguments to validate
        """

        if len(args) < 1 and args_num > 0:
            print("** class name missing **")
            return False
        args_num -= 1
        if args[0] not in HBNBCommand.__classes.keys() and args_num > 0:
            print("** class doesn't exist **")
            return False
        args_num -= 1

        # check the instance id
        if len(args) < 2 and args_num > 0:
            print("** instance id missing **")
            return False
        args_num -= 1
        # if not is_instance(args[1]) and args_num > 0:
        #    print("** no instance found **")
        #    return False
        # args_num -= 1

        # check the atrribute name
        if len(args) < 3 and args_num > 0:
            print("** attribute name missing **")
            return False
        args_num -= 1

        # check the value
        if len(args) < 4 and args_num > 0:
            print("** value missing **")
            return False
        args_num -= 1

        return True

    # -----------Services Methods------------

    def do_create(self, line):
        """
        create    create a new modle instance

        Syntax:
            create <model_name>

        Descriptions:
            `create` creates a new instance of the model `model_name`,
             the `model_name` should be a valide class name.
        """
        if not HBNBCommand.__interactive:
            print()

        args = self.get_args(line)
        if not self.validate(args, 1):
            return False
        __new = HBNBCommand.__classes[args[0]]()
        # TODO:
        #     save it to json file
        print(__new.id)

    def do_show(self, line):
        """
        show    shows the informations about an instance

        Syntax:
            show <model_name> <instance_id>

        Descriptions:
            `show` prints the string representation of an instance of the
             <model_name> class that have the id <instance_id>.
             The <model_name> should be a valide class name, and the
             <instance_id> should be a valide instance ID.
        """
        if not HBNBCommand.__interactive:
            print()

        args = self.get_args(line)
        if not self.validate(args, 2):
            return False
        print(args)

    def do_destroy(self, line):
        """
        destroy    deletes an instance of a class

        Syntax:
            destroy <model_name> <instance_id>

        Descriptions:
            `destroy` deletes the instance of the class <model_name> that
             has the id of <instance_id>.
             The <model_name> should be a valide class name, and the
             <instance_id> should be a valide instance ID.
        """
        if not HBNBCommand.__interactive:
            print()

        args = self.get_args(line)
        if not self.validate(args, 2):
            return False
        print(arg)

    def do_all(self, line):
        """
        all    prints information about instances

        Syntax:
            all [model_name]

        Descriptions:
            `all` prints the string representation of all the instance of
             all the models, if [model_name] was provided and it's a
             valide class name then `all` will prints only
             the [model_name] instances information.
        """
        if not HBNBCommand.__interactive:
            print()

        args = self.get_args(line)
        if len(args) >= 1:
            if not self.validate(args, 1):
                return False
            print("getting class {} instances informations".format(args[0]))
        else:
            print("getting all classes instance informations")
        print(args)

    def do_update(self, line):
        """
        update    updates an instance attributes

        Syntax:
            update <model_name> <instance_id> <atrr> "<value>"

        Descriptions:
            `update` updates the <model_name> instance with the ID of
             <instance_id>, by adding or changing the value of the
             attribute <attr> with the <value> value.
             Both the <model_name> and <instance_id> should be valide.
        """
        if not HBNBCommand.__interactive:
            print()

        args = self.get_args(line)
        if not self.validate(args, 4):
            return False
        print(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
