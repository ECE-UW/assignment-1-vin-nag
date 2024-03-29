"""
This file describes a streets database object that adds, changes and removes streets

Date:
    September 14, 2019

Course:
    ECE 650 Assignment #1

Author:
    name: Vineel Nagisetty
    student #: 20270395
    contact: vineel.nagisetty@uwaterloo.ca

"""

from graph import Graph


class StreetDb:

    """
    A Class that acts as a database for streets. It handles basic commands such as add, remove, change and generate
    graphs

    Attributes
    ----------
    verbose : bool
        determine whether to print out intermediate steps for debugging (default False)
    test : bool
        determine whether unit tests are run (default False)

    Methods
    -------
    add(name, coordinates_list):
        add a street to the graph
    change(name, coordinates_list):
        change the coordinates of a street
    remove(name):
        remove a street from the map
    generate_graph():
        generate the graphs and edges of the map and prints it
    """

    def __init__(self, verbose=False, test=False):
        """
        Standard init method
        :param verbose: (bool) whether to display steps for debugging
        """
        self.dictionary = {}
        self.verbose = verbose
        self.test = test
        return

    def add(self, name, coordinates_list):
        """
        This function adds a street to the graph
        :param name: (str) name of the street
        :param coordinates_list: (2d array) list with [x,y] coordinates
        :return: None
        """
        if self.verbose:
            print 'reached add with ', name, coordinates_list

        if name in self.dictionary:
            raise NameError('Error: trying to add a street that already exists')

        self.dictionary[name] = coordinates_list
        if self.verbose:
            print 'added'
        return ''

    def change(self, name, coordinates_list):
        """
        This function changes the coordinates of a street
        :param name: (str) name of the street
        :param coordinates_list: (2d array) list with [x,y] coordinates
        :return: None
        """
        if self.verbose:
            print 'reached change with ', name, coordinates_list

        if name not in self.dictionary:
            raise NameError('Error: c specified for a street that does not exist')

        self.dictionary[name] = coordinates_list
        if self.verbose:
            print 'changed'
        return ''

    def remove(self, name):
        """
        This function removes a street from the map
        :param name: (str) name of the street
        :return: None
        """
        if self.verbose:
            print 'reached removed with ', name

        if name not in self.dictionary:
            raise NameError('Error: r specified for a street that does not exist')

        del self.dictionary[name]
        if self.verbose:
            print 'removed'
        return ''

    def generate_graph(self):
        """
        This function generates the graphs and edges of the map and prints it
        :return: None
        """
        if self.verbose:
            print('reached generate ')

        graph_instance = Graph(streets_list=[x for x in self.dictionary.values()], verbose=self.verbose)
        graph_instance.generate_and_simplify()

        if self.verbose:
            print('dictionary =' + str(self.dictionary))

        return graph_instance.__repr__()

