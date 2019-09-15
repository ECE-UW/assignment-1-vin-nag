"""
This file is intended to help parse user commands, throw necessary errors and return function and arguments

Date:
    September 14, 2019

Course:
    ECE 650 Assignment #1

Author:
    name: Vineel Nagisetty
    student #: 20270395
    contact: vineel.nagisetty@uwaterloo.ca
"""

import re


def parse_name(name_input):
    """
    This function parses the name of a street from the input
    :param name_input: (str) name part (between quotes) of the user input command
    :return: str: name of the street
    """
    name = name_input.lower()

    # check for containing only alphabets and spaces
    r = re.compile("^[a-zA-Z ]*$")
    if not r.match(name):
        raise NameError('Error: street name should only contain alphabets and spaces')
    return name


def parse_coordinates(coordinates_input):
    """
    This function parses the coordinates list from the input
    :param coordinates_input: (str) coorindates list part of the user input command
    :return: 2d-array of list of [x,y] coordinates
    """

    # split the string to a list of (float,float) format
    r = re.compile("[(][-]?[0-9]+[,][-]?[0-9]+[)]")
    split = r.findall(coordinates_input)

    # check if the size is consistent
    if sum([len(x) for x in split]) != len(coordinates_input):
        raise NameError('Error: coordinates provided or not formatted correctly (using () )')

    lst = []
    for coordinate in split:
        trim_brackets = coordinate[1:-1]
        num = trim_brackets.split(',')
        point = [float(num[0]), float(num[1])]
        lst.append(point)

    return lst


def parse(user_input, graph_instance):
    """
     This function parses the commands, calling the name and coordinates parser if needed
    :param user_input: (str) user input command
    :param graph_instance: (Graph) graph instance
    :return: func: function of graph instance, args: arguments for the function
    """

    # define static commands and arguments list
    commands = {
        'a': graph_instance.add,
        'c': graph_instance.change,
        'r': graph_instance.remove,
        'g': graph_instance.generate_graph
    }
    args_list = {
        graph_instance.add: ['name','coordinates_list'],
        graph_instance.change: ['name', 'coordinates_list'],
        graph_instance.remove: ['name'],
        graph_instance.generate_graph: []
    }

    if user_input[0] not in commands:
        raise NameError('Error: incorrect command given or not formatted correctly')

    func = commands[user_input[0]]
    required_args = args_list[func]
    args = []

    # add necessary arguments if needed
    if 'name' in required_args:
        user_input_no_command = user_input[2:]
        start_index, end_index = user_input_no_command.find('"'), user_input_no_command.rfind('"')

        # check if name is formatted correctly
        if start_index == -1 or end_index == -1 or start_index == end_index:
            raise NameError('Error: street name not provided or not formatted correctly (using \"\")')

        name_input = user_input_no_command[start_index + 1: end_index]
        args.append(parse_name(name_input))

    if 'coordinates_list' in required_args:
        end_quote_index = user_input.rfind('"')
        # remove all newlines and spaces
        coordinate_input = user_input[end_quote_index + 2:].replace(' ', '').replace('\n', '')
        args.append(parse_coordinates(coordinate_input))

    return func, args

