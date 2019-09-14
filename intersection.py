"""
This file helps check for intersections. Algorithm used from http://www.cs.swan.ac.uk/~cssimon/line_intersection.html
but implementation is my own.
"""


def side(a,b,c):
    """
    This function checks where point c is in relation with the line segment a,b
    :param a: (1d array) describing x,y coordinates for point a
    :param b: (1d array) describing x,y coordinates for point b
    :param c: (1d array) describing x,y coordinates for point c
    :return: int: 1,-1 or 0 depending on orientation
    """
    d = (c[1]-a[1])*(b[0]-a[0]) - (b[1]-a[1])*(c[0]-a[0])

    return 1 if d > 0 else (-1 if d < 0 else 0)


def is_point_in_closed_segment(a, b, c):
    """
    This function checks if point c is inside line segment a,b
    :param a: (1d array) describing x,y coordinates for point a
    :param a: (1d array) describing x,y coordinates for point b
    :param a: (1d array) describing x,y coordinates for point c
    :return: bool
    """
    """ Returns True if c is inside closed segment, False otherwise.
        a, b, c are expected to be collinear
    """
    if a[0] < b[0]:
        return a[0] <= c[0] and c[0] <= b[0]
    if b[0] < a[0]:
        return b[0] <= c[0] and c[0] <= a[0]

    if a[1] < b[1]:
        return a[1] <= c[1] and c[1] <= b[1]
    if b[1] < a[1]:
        return b[1] <= c[1] and c[1] <= a[1]

    return a[0] == c[0] and a[1] == c[1]


def closed_segment_intersect(a,b,c,d):
    """
    This function checks if line segment a,b intersects with c,d
    :param a: (1d array) describing x,y coordinates for point a
    :param b: (1d array) describing x,y coordinates for point b
    :param c: (1d array) describing x,y coordinates for point c
    :param d: (1d array) describing x,y coordinates for point d
    :return: bool
    """
    if a == b:
        return a == c or a == d
    if c == d:
        return c == a or c == b

    s1 = side(a,b,c)
    s2 = side(a,b,d)

    # All points are collinear
    if s1 == 0 and s2 == 0:
        return \
            is_point_in_closed_segment(a, b, c) or is_point_in_closed_segment(a, b, d) or \
            is_point_in_closed_segment(c, d, a) or is_point_in_closed_segment(c, d, b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    s1 = side(c,d,a)
    s2 = side(c,d,b)

    # No touching and on the same side
    if s1 and s1 == s2:
        return False

    return True


def get_intersection(a,b,c,d):
    """
    This function gives the co-ordinates of intersection between segment a,b and c,d
    :param a: (1d array) representing [x,y] coordinates for point a
    :param b: (1d array) describing x,y coordinates for point b
    :param c: (1d array) describing x,y coordinates for point c
    :param d: (1d array) describing x,y coordinates for point d
    :return: [x,y] coordinates of intersection point
    """
    t = ((c[1]-d[1]) * (a[0]-c[0]) + (d[0]-c[0]) * (a[1]-c[1]) )/( (d[0]-c[0])*(a[1]-b[1]) - (a[0]-b[0])*(d[1]-c[1]))
    x = a[0] + t*(b[0]-a[0])
    y = a[1] + t*(b[1]-a[1])
    return [x, y]
