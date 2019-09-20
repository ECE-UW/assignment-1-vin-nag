"""
This file is the main function that handles input. It solves the problem described in Assignment 1

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
        line = sys.stdin.readline().strip()
        if verbose:
            print 'read a line:', line
        if line == '':
            break
        try:
            func, args = parse(line, street_db_instance)
            sys.stdout.write(func(*args))
        except Exception as detail:
            print >> sys.stderr, detail
            continue
    print 'Finished reading input'
    sys.exit(0)


class TestWrapper:

    def __init__(self):
        self.commands = ""
        self.output = ""
        pass

    def run(self, commands, out=sys.stdout):
        """
        Function made to test inputs from file for testing efficiently
        :return:
        """
        verbose = False
        street_db_instance = StreetDb(verbose=verbose, test=True)

        for line in commands:
            try:
                func, args = parse(line, street_db_instance)
                out.write(func(*args))
            except Exception as detail:
                out.write('\n' + str(detail))
                continue


if __name__ == '__main__':
    main()
