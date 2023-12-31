#!/usr/bin/python3

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
import shlex
import sys
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
    BnB_objects = storage.all()
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def preloop(self):
        """
            Check if the session is interactive session or non interactive
            and make a query for all the saved BnB objects
        """
        pass

    def do_help(self, line):
        """
            help    shows all the console services, or a selcted service

            Syntax:
                help [service_name]

            Descriptions:
                `help` shows the services that the console provides, and if
                the [service_name] is entered it print the help page of
                this service.
                The [servise_name] should be a valide service name

            __docfun = ['EOF', 'all', 'creat', 'destroy', 'help',
                        'quit', 'show', 'update']
        """
        # TODO: costumize the help function
        super().do_help(line)

    def do_quit(self, line):
        """
            quit   Terminate the console and exit the program

            Syntax:
                quit
        """
        return True

    def do_EOF(self, *args):
        """
            EOF | ^D    Terminate the console and exite the program

            Syntax:
                EOF
                ^D

            Descriptions:
                Same as the quit function, this one iis used to handel
                the End Of File situations
        """
        print()
        return True

    def emptyline(self, *args):
        """
            Handle the empty line
        """
        pass

    # -------------helper functions-----------
    def get_args(self, line):
        """
            Preprocessing the line from the interpeter before passing it
            to the onecmd() function.
            in this case we will handel the double qouted text, beside
            extracting args from line
        """
        args = shlex.split(line)
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

        if '.'.join(args[:2]) not in HBNBCommand.BnB_objects.keys() and args_num > 0:
            print("** no instance found **")
            return False
        args_num -= 1

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
                `create` creates new instance of the model `model_name` and prints
                its id, the `model_name` should be a valide class name.
        """
        args = self.get_args(line)
        if not self.validate(args, 2):
            return False
        __new = HBNBCommand.__classes[args[0]]()
        print(__new.id)
        storage.save()
        HBNBCommand.BnB_objects = storage.all()  # update the BnB_objects instantly

    def do_show(self, line):
        """
            show    show informations about an instance

            Syntax:
                show <model_name> <instance_id>

            Descriptions:
                `show` prints the string representation of an instance of the
                <model_name> class which has the id <instance_id>.
                The <model_name> should be a valide class name, and the
                <instance_id> should be a valide instance ID.
                The string representation consist of:
                    '[claseName] (instance_id) instance_attrs_dict'
        """
        args = self.get_args(line)
        if not self.validate(args, 4):
            return False
        instance = HBNBCommand.BnB_objects['.'.join(args[:2])]
        # instance = HBNBCommand.__classes[args[0]](**instance_dict)
        print(instance)

    def do_destroy(self, line):
        """
            destroy    delete instance of a class

            Syntax:
                destroy <model_name> <instance_id>

            Descriptions:
                `destroy` deletes the instance of the class <model_name> which
                has the id of <instance_id>.
                The <model_name> should be a valide class name, and the
                <instance_id> should be a valide instance ID.
        """
        args = self.get_args(line)
        if not self.validate(args, 4):
            return False
        del HBNBCommand.BnB_objects['.'.join(args[:2])]
        storage.save()

    def do_all(self, line):
        """
            all    print instances information

            Syntax:
                all [model_name]

            Descriptions:
                `all` prints the string representation of all the instance of
                all the models, if [model_name] was provided and it's a
                valide class name then `all` will prints only
                the [model_name] instances information.
                The string represntations consists of:
                    '["[className] (instance_id) instance_attrs_dict"]'
        """
        args = self.get_args(line)
        instances_list = list()

        if len(args) >= 1:

            if not self.validate(args, 2):
                return False

            for instance in HBNBCommand.BnB_objects.values():
                if instance.__class__.__name__ == args[0]:
                    instances_list.append(str(instance))

        else:
            for instance in HBNBCommand.BnB_objects.values():
                instances_list.append(str(instance))

        print(instances_list)

    def do_update(self, line, *iner_call):
        """
            update    update instance attributes

            Syntax:
                update <model_name> <instance_id> <atrr> "<value>"

            Descriptions:
                `update` updates the <model_name> instance with the ID of
                <instance_id>, by adding or changing the value of the
                attribute <attr> with the <value> value.
                Both the <model_name> and <instance_id> should be valide
                and the <attr> should be valide instance attribute.
        """
        args = self.get_args(line)
        if not self.validate(args, 6):
            return False
        instance = HBNBCommand.BnB_objects['.'.join(args[:2])]

        value = args[3]
        if '.' in value:
            value_type = float
        else:
            value_type = int

        try:
            value = value_type(value)
        except ValueError:
            pass

        setattr(instance, args[2], value)
        instance.save()

    # -------------- Advanced Services --------------
    def default(self, line):
        """
            Overide the Cmd.defautl method to controle the advance services
            syntax
        """

        _pat = r'(\w+)\.(update)\(([-"\w\s]*),? ?([-"\w\d]*),? ?([-"\w\d]*)\)'
        pat_s = re.compile(r"(\w+)\.(show)\((.*)\)")
        pat_d = re.compile(r"(\w+)\.(destroy)\((.*)\)")
        pat_u = re.compile(_pat)
        pat_u_dict = re.compile(r'(\w+)\.(update)\(([-"\w\s]*),? ?(\{.*\})')

        if line.endswith(".all()"):
            args = line.split('.')
            return self.do_all(args[0])

        elif line.endswith(".count()"):
            args = line.split('.')
            if not self.validate(args, 2):
                return False
            count = 0
            for instance in HBNBCommand.BnB_objects.values():
                if instance.__class__.__name__ == args[0]:
                    count += 1
            print(count)

        elif pat_s.match(line):
            matched = pat_s.match(line)
            _line = matched.group(1) + ' ' + matched.group(3)
            return self.do_show(_line)

        elif pat_d.match(line):
            matched = pat_d.match(line)
            _line = matched.group(1) + ' ' + matched.group(3)
            return self.do_destroy(_line)

        elif pat_u.match(line):
            matched = pat_u.match(line)

            _class = matched.group(1).strip(',')
            _id = matched.group(3).strip(',')
            _attr = matched.group(4).strip(',')
            _value = matched.group(5).strip(',')

            _line = _class + ' ' + _id + ' ' + _attr + ' ' + _value
            return self.do_update(_line)

        elif pat_u_dict.match(line):
            matched = pat_u_dict.match(line)

            _class = matched.group(1)
            _id = matched.group(3)
            _json_dict = matched.group(4).replace("'", "\"")
            _dict = json.loads(_json_dict)

            for key, val in _dict.items():
                _line = _class + ' ' + _id + ' ' + key + ' ' + str(val)
                self.do_update(_line, True)

        else:
            super().default(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
