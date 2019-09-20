# TODO: Add more unit tests (error checks for co-ordinates list and function calls)

import sys
import unittest
from a1ece650 import TestWrapper


class MyTest(unittest.TestCase):

    def setUp(self):
        """
        create instance of test wrapper
        :return:
        """
        self.test_instance = TestWrapper()

    def tearDown(self):
        """
        delete instance of test wrapper
        :return:
        """
        del self.test_instance

    def test_function_calls(self):
        """
        Test if error raised when wrong function given
        :return:
        """
        with open('input_functions.txt', 'r') as input_file:
            with open('output_functions.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        from StringIO import StringIO
        out = StringIO()
        self.test_instance.run(commands, out=out)
        self.assertEqual(out.getvalue().strip(), expected_output.strip())

    def test_street_names(self):
        """
        Test for street names regex
        :return:
        """
        with open('input_street_names.txt', 'r') as input_file:
            with open('output_street_names.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        from StringIO import StringIO
        out = StringIO()
        self.test_instance.run(commands, out=out)
        self.assertEqual(out.getvalue().strip(), expected_output.strip())

    def test_coordinates_list(self):
        """
        Test for coordinates list regex
        :return:
        """
        with open('input_coordinates_list.txt', 'r') as input_file:
            with open('output_coordinates_list.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        from StringIO import StringIO
        out = StringIO()
        self.test_instance.run(commands, out=out)
        self.assertEqual(out.getvalue().strip(), expected_output.strip())

    def test_example(self):
        """
        Test the example given in class
        :return:
        """
        with open('input_example.txt', 'r') as input_file:
            with open('output_example.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        from StringIO import StringIO
        out = StringIO()
        self.test_instance.run(commands, out=out)
        self.assertEqual(out.getvalue().strip(), expected_output.strip())

    def test_graph3(self):
        """
        Test new graph
        :return:
        """
        with open('input_example3.txt', 'r') as input_file:
            with open('output_example3.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        from StringIO import StringIO
        out = StringIO()
        self.test_instance.run(commands, out=out)
        self.assertEqual(out.getvalue().strip(), expected_output.strip())


if __name__ == '__main__':
    unittest.main()
