"""
Google Problem: Bringing a Gun to a Guard Fight
Written by cmdellinger

Problem:
Write a function answer(dimensions, your_position, guard_position, distance)
that gives an array of 2 integers of the width and height of the room, an array
of 2 integers of your x and y coordinates in the room, an array of 2 integers of
the guard's x and y coordinates in the room, and returns an integer of the
number of distinct directions that you can fire to hit the elite guard, given
the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and
the elite guard are both positioned on the integer lattice at different distinct
positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim].
Finally, the maximum distance that the beam can travel before becoming harmless
will be given as an integer 1 < distance <= 10000.

See README for problem details and specifications.

Algorithm breakdown:
* Generate possible solutions by mirroring `your_position` and `guard_position`
  up to the max distance the laser can reach.
* Transform list of `good_guys` and `bad_guys` to polar coordinates for easier
  comparison. A dictionary is more ideal so keys and values can be more easily
  separated.
* Count all angles for `bad_guys` that aren't in `good_guys` dictionary or are
  in both lists but the `bad_guys` distance is less.
"""
from itertools import product, izip, cycle
from math import atan2, hypot

def get_slope(pt1, pt2):
    """ calculates the slope b/t pt1 and pt2 assuming start, end order """
    return [x2-x1 for x1,x2 in izip(pt1,pt2)]

def get_dist(pt1, pt2):
    """ calculates the distance between pt1 and pt2 """
    return hypot(*get_slope(pt1,pt2))

def get_angle(pt1, pt2):
    """ calculates the polar angle of the slope """
    x,y = get_slope(pt1,pt2)
    return atan2(y,x)

def get_series(dimensions, pt, your_position, distance, i):
    """ generates the series of one part of the coordinates, x or y in (x, y)"""
    # calculate maximum and minimum for index position
    minimum = your_position[i] - distance
    maximum = your_position[i] + distance
    # split dimension into segments at point for mirroring
    segment = [dimensions[i] - pt[i], pt[i]]
    series = []
    # generate positive values
    current = pt[i]
    seg_ind = cycle([0,1])
    while current <= maximum:
        series.append(current)
        current += 2*segment[seg_ind.next()]
    # generate negative values
    current = pt[i]
    seg_ind = cycle([1,0])
    while current >= minimum:
        series.append(current)
        current -= 2* segment[seg_ind.next()]
    return series

def get_all_series(dimensions, pt, your_position, distance):
    """ generates series for each part of the coordinates (x, y) """
    return [get_series(dimensions, pt, your_position, distance, i) for i in range(len(dimensions))]

def get_valid_angles(dimensions, pt, your_position, distance):
    """ retrieves mirrored locations and converts them to a polar dictionary """
    polar_dict = {}
    for test_pt in product(*get_all_series(dimensions, pt, your_position, distance)):
        test_pt = list(test_pt)
        r = get_dist(test_pt, your_position)
        angle = get_angle(test_pt, your_position)
        if test_pt != your_position and r <= distance:
            try:
                polar_dict[angle] = min(polar_dict[angle], r)
            except:
                polar_dict[angle] = r
    return polar_dict

def answer(dimensions, your_position, guard_position, distance):
    """ Determines the number of angles a laser can be shot to hit a guard.
        
    Calculates the number of angles that a laser can shoot in order to hit a
    guard but not yourself given the board dimensions and the distance the laser
    can travel. The laser can bounce off walls without losing momentum.
        
    Args:
        dimensions (int list): Dimensions of the rectangular room in the form
        (int x_max, int y_max).
        your_position (int list): location of person escaping in Cartesian
        coordinates in the form (int x, int y).
        guard_position (int list): location of guard as a Cartesian coordinate
        in the form (int x, int y)
        distance (int): maximum distance the laser can travel
    Returns:
        The integer number of angles that hit a guard.
    """
    good_guys = get_valid_angles(dimensions, your_position, your_position, distance)
    bad_guys = get_valid_angles(dimensions, guard_position, your_position, distance)
    solutions = 0
    for angle in bad_guys:
        if angle in good_guys:
            if bad_guys[angle] < good_guys[angle]:
                solutions += 1
        else:
            solutions += 1
    return solutions
