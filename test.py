# TODO: Add more unit tests (co-ordinates list, functions, test other graphs)

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
        pass

    def test_street_names(self):
        """
        Test for street names regex
        :return:
        """

        with open('input_street_names.txt', 'r') as input_file:
            with open('output_street_names.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        self.test_instance.run(commands)
        self.assertEqual(self.test_instance.output, expected_output)

    def test_coordinates_list(self):
        """
        Test for coordinates list regex
        :return:
        """
        pass

    def test_example(self):
        """
        Test the example given in class
        :return:
        """
        with open('input_example.txt', 'r') as input_file:
            with open('output_example.txt', 'r') as output_file:
                commands = input_file.readlines()
                expected_output = output_file.read()

        self.test_instance.run(commands)
        self.assertEqual(self.test_instance.output, expected_output)


    def test_graph2(self):
        """
        Test new graph
        :return:
        """
        pass

    def test_graph3(self):
        """
        Test new graph
        :return:
        """
        pass


if __name__ == '__main__':
    unittest.main()
