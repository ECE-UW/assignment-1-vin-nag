"""
This file helps check for intersections. Algorithm used from http://www.cs.swan.ac.uk/~cssimon/line_intersection.html
but implementation is my own. It is a fascinating read and Simon Walton derives the equation and explains why it
works way better than I can.  For more information check the page linked

Date:
    September 14, 2019

Course:
    ECE 650 Assignment #1

Author:
    name: Vineel Nagisetty
    student #: 20270395
    contact: vineel.nagisetty@uwaterloo.ca
"""

import math


def get_denominator(a, b, c, d):
    """
    This function calculates the denominator. If the denominator is 0, the line segments are either collinear (parallel)
    or have infinite number of intersections (lie on top of each other).
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param b: (1d array) point [x, y] representing cartesian coordinate of point b
    :param c: (1d array) point [x, y] representing cartesian coordinate of point c
    :param d: (1d array) point [x, y] representing cartesian coordinate of point d
    :return: (float) denominator
    """
    num = (d[0] - c[0]) * (a[1] - b[1]) - (a[0] - b[0]) * (d[1] - c[1])

    # raise an error if this is 0
    if num == 0:
        raise ValueError(' line segments ', a, b, c, d, ' are collinear or parallel')
    return num


def get_numerator(a, c, e, f):
    """
    This function calculates the numerator for the t values.
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param c: (1d array) point [x, y] representing cartesian coordinate of point c
    :param e: (1d array) point [x, y] representing cartesian coordinate of point e
    :param f: (1d array) point [x, y] representing cartesian coordinate of point f
    :return: (float) numerator
    """
    return (e[1] - f[1]) * (a[0] - c[0]) + (f[0] - e[0]) * (a[1] - c[1])


def get_distance(a, b):
    """
    This function gets the distance between point a and b
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param b: (1d array) point [x, y] representing cartesian coordinate of point b
    :return: (float) distance
    """
    return math.sqrt( abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2 )


def get_equation_of_line(a, b):
    """
    This function gets the equation of the line with y = mx + b
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param b: (1d array) point [x, y] representing cartesian coordinate of point b
    :return: (1d array) of slope (m) and intercept (b) values
    """
    if (a[0] - b[0]) == 0:
        return [0, a[1]]
    m = (a[1] - b[1])/(a[0] - b[0])
    b = a[1] - m * a[0]
    return [m, b]


def is_on_segment(a, b, x):
    """
    This function checks if a given point is within the line segment ab. Note that this is only after we know the
    lines are collinear
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param b: (1d array) point [x, y] representing cartesian coordinate of point b
    :param x: (1d array) point [x, y] representing cartesian coordinate of point x
    :return:
    """
    dist1 = get_distance(a, x) + get_distance(b, x)
    dist2 = get_distance(a, b)
    return dist1 == dist2


def parallel_or_collinear(a, b, c, d):
    """
    This function checks whether line segments ab and cd are parallel or collinear. If collinear, it checks if they
    overlap
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param b: (1d array) point [x, y] representing cartesian coordinate of point b
    :param c: (1d array) point [x, y] representing cartesian coordinate of point c
    :param d: (1d array) point [x, y] representing cartesian coordinate of point d
    :return: (bool, [x,y]) whether they have one intersection and the co-ordinate if true
    """
    # get equations of line segments to check whether parallel
    l1 = get_equation_of_line(a, b)
    l2 = get_equation_of_line(c, d)
    if l1 != l2:
        # is parallel
        return False, [None, None]
    else:
        # is collinear - check whether there is an overlap - if there is, send that point as intersection
        if is_on_segment(a, b, c):
            return True, c
        elif is_on_segment(a, b, d):
            return True, d
        elif is_on_segment(c, d, a):
            return True, a
        elif is_on_segment(c, d, b):
            return True, b
        else:
            # no overlap
            return False, [None, None]


def is_intersecting_once(a, b, c, d):
    """
    This function checks if line segments <a,b> and <c,d> intersect, using Simon Waltons algorithm listed above
    :param a: (1d array) point [x, y] representing cartesian coordinate of point a
    :param b: (1d array) point [x, y] representing cartesian coordinate of point b
    :param c: (1d array) point [x, y] representing cartesian coordinate of point c
    :param d: (1d array) point [x, y] representing cartesian coordinate of point d
    :return: (bool, [x,y]) whether they have one intersection and the co-ordinate if true
    """
    try:
        denominator = get_denominator(a, b, c, d)
    except ValueError:
        return parallel_or_collinear(a, b, c, d)

    t1 = get_numerator(a, c, c, d) / denominator
    t2 = get_numerator(a, c, a, b) / denominator

    # line segments intersect only when both t values are in range of [0,1]
    if all(0 <= val <= 1 for val in [t1, t2]):
        x = a[0] + t1*(b[0]-a[0])
        y = a[1] + t1*(b[1]-a[1])
        return True, [round(x,2), round(y,2)]
    else:
        return False, [None, None]
