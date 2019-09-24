"""
This file describes a graph that handles generating vertices and edges and printing them

Date:
    September 14, 2019

Course:
    ECE 650 Assignment #1

Author:
    name: Vineel Nagisetty
    student #: 20270395
    contact: vineel.nagisetty@uwaterloo.ca

"""

from check_intersection import is_intersecting_once


class Graph:

    """
    A Class that acts as a database for streets. It handles basic commands such as add, remove, change and generate
    graphs

    Attributes
    ----------
    streets_list: 2d list
        list representing coordinates for each street
    verbose : bool
        determine whether to print out intermediate steps for debugging (default False)

    Methods
    -------
    generate_and_simplify():
        generate graphs from the streets list
    """

    def __init__(self, streets_list, verbose=False):
        """
        Standard init method
        :param streets_list: (2d array) list representing coordinates list for each street
        :param verbose: (bool) printing statements for debugging purposes
        """
        self.streets = streets_list
        self.vertices = {}
        self.num = 1
        self.edges = []
        self.verbose = verbose
        self.lookup = {}
        self.connected_components = []

    def generate_and_simplify(self):
        """
        This function is called by street database to generate the graphs
        :return: None
        """
        self._find_connected_components()
        self._add_vertices()
        self._add_edges()

    def _find_connected_components(self):
        """
        This function finds all connected components by checking for intersections
        :return: None
        """
        num_streets = len(self.streets)

        # go over every combination of a street segment with all segments in other streets
        for idx_a in range(num_streets - 1):
            for idx_c in range(len(self.streets[idx_a]) - 1):
                for idx_b in range(idx_a + 1, num_streets):
                    for idx_d in range(len(self.streets[idx_b]) - 1):

                        # check for an intersection
                        a, b = self.streets[idx_a][idx_c], self.streets[idx_a][idx_c + 1]
                        c, d = self.streets[idx_b][idx_d], self.streets[idx_b][idx_d + 1]
                        intersecting, x = is_intersecting_once(a, b, c, d)

                        # add to connected components if intersecting
                        if intersecting:
                            self._add_connected_components(a, b, x)
                            self._add_connected_components(c, d, x)

    def _add_connected_components(self, a, b, x):
        """
        This function adds coordinates to connected components
        :param a: (1d array) point [x, y] representing cartesian coordinate of point a
        :param b: (1d array) point [x, y] representing cartesian coordinate of point b
        :param x: (1d array) point [x, y] representing cartesian coordinate of point x (intersecting point)
        :return: None
        """
        if self.verbose:
            print 'reached here with' + str([a, b, x])

        # check if a vertex already is part of a component
        found = False
        for component in self.connected_components:
            if a in component or b in component:
                if self.verbose:
                    print 'true for ' +str([a, b]) + ' in ' + str(component)
                found = True

                # add intersection point to the existing component, if its not already in the component
                if a not in component:
                    component.append(a)
                if b not in component:
                    component.append(b)
                if x not in component:
                    component.append(x)
        # add all points to a new component
        if not found:
            self.connected_components.append([a, x, b])

    def _add_vertices(self):
        """
        This function adds vertices to the data structure
        :return: None
        """
        for component in self.connected_components:
            for vertex in component:
                vertex = tuple(vertex)
                if vertex not in self.lookup:
                    self.vertices[self.num] = vertex
                    self.lookup[vertex] = self.num
                    self.num += 1

    def _add_edges(self):
        """
        This function adds edges to the data structure
        :return: None
        """
        for component in self.connected_components:
            vertices = sorted(component)
            for idx in range(len(vertices) - 1):
                key_a, key_b = self.lookup[tuple(vertices[idx])], self.lookup[tuple(vertices[idx + 1])]
                if key_a == key_b:
                    continue
                edge = tuple([key_a, key_b])
                if edge not in self.edges:
                    self.edges.append(edge)

    def __repr__(self):
        """
        This function overrides the print command on the graph object, giving an output similar to whats requested
        :return: str
        """
        # Vertices
        two_spaces = '  '
        output = 'V = {\n'
        for key in self.vertices.keys():
            output += two_spaces + str(key) + ': ' + str(self.vertices[key]) + '\n'
        output += '}\n'

        # Edges
        output += 'E = {\n'
        for edge in range(len(self.edges)-1):
            output += two_spaces + '<' + str(self.edges[edge][0]) + ',' + str(self.edges[edge][1]) + '>,\n'

        if len(self.edges) > 0:
            output += two_spaces + '<' + str(self.edges[-1][0]) + ',' + str(self.edges[-1][1]) + '>\n'

        output += '}\n'

        return output
