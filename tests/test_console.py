import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class ConsoleTestCase(unittest.TestCase):
    """Test case for the console commands."""

    def test_error_classname_missing(self):
        """Test command with missing class name."""
        cmds = ["create", "update", "show", "destroy"]
        expected_output = "** class name missing **"

        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(cmd)
                self.assertEqual(expected_output, f.getvalue().strip())

    def test_error_class_does_not_exist(self):
        """Test command with non-existing class."""
        cmds = ["create x", "update x", "show x", "destroy x"]
        expected_output = "** class doesn't exist **"

        for cmd in cmds:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd(cmd)
                self.assertEqual(expected_output, f.getvalue().strip())

    def test_error_instance_id_missing(self):
        """Test command with missing instance ID."""
        cmds = ["update", "show", "destroy"]
        classes = HBNBCommand().classes
        expected_output = "** instance id missing **"

        for cmd in cmds:
            for clas in classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{cmd} {clas}")
                    self.assertEqual(expected_output, f.getvalue().strip())

    def test_error_no_instance_found(self):
        """Test command with non-existing instance ID."""
        cmds = ["update", "show", "destroy"]
        classes = HBNBCommand().classes
        wrong_id = "x"
        expected_output = "** no instance found **"

        for cmd in cmds:
            for clas in classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
                    self.assertEqual(expected_output, f.getvalue().strip())
