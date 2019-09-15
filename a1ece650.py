"""
This file is the main function that handles CLI input. It solves the problem described in Assignment 1

Date:
    September 14, 2019

Course:
    ECE 650 Assignment #1

Author:
    name: Vineel Nagisetty
    student #: 20270395
    contact: vineel.nagisetty@uwaterloo.ca
"""

import sys
from street_db import StreetDb
from parser import parse


def main():
    """
    The main function of our program
    :return: None
    """
    verbose = False
    street_db_instance = StreetDb(verbose=verbose)

    while True:
        line = sys.stdin.readline()
        if verbose:
            print 'read a line:', line
        if line == '':
            break
        try:
            func, args = parse(line, street_db_instance)
            func(*args)
        except Exception as detail:
            print detail
            continue
    if verbose:
        print 'Finished reading input'
    sys.exit(0)


def main_from_file():
    """
    Function made to test inputs from file for testing efficiently
    TODO: Update unit test so this is not needed.
    :return:
    """
    verbose = False
    street_db_instance = StreetDb(verbose=verbose)
    file_name = raw_input('enter file with commands: ')

    with open(file_name, 'r') as file_handler:
        for line in file_handler:
            if verbose:
                print '\n'+ line[:-1]
            try:
                func, args = parse(line, street_db_instance)
                func(*args)
            except Exception as detail:
                print detail
                continue


if __name__ == '__main__':
    main()
