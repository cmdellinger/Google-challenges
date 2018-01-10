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
        The number of angles that hit a guard.
    """
    # Algorithm breakdown:
    # * recenter board to `your_position` (recentering will help with next step)
    #   and duplicate `your_position` and `guard_position` by repeating the
    #   board up to the max distance the laser can reach.
    # * transform list of `good_guys` and `bad_guys` to polar coordinates for
    #   easier comparison. a dictionary is more ideal so keys and values can be
    #   more easily separated.
    # * count all angles for `bad_guys` that aren't in `good_guys` dictionary or
    #   are in both lists but the `bad_guys` value is less.
    from itertools import product, izip
    from math import atan2, hypot
    x_len, y_len = dimensions
    # reposition `your_position` to (0,0) and generate positions
    good_guys = list(product(range(0,-distance+1, -x_len)
                             + range(0,distance+1, x_len),
                             range(0,-distance+1, -y_len)
                             + range(0,distance+1, y_len)))
    good_guys.remove((0,0))
    # reposition based on `good_guys` transformation and generate positions
    x_diff, y_diff = [x1-x2 for x1,x2 in izip(your_position, guard_position)]
    bad_guys = list(product(range(x_diff,-distance+1, -x_len)
                            + range(x_diff,distance+1, x_len),
                            range(y_diff,-distance+1, -y_len)
                            + range(y_diff,distance+1, y_len)))

    def quasi_polar(point_list):
        """ Transforms list of Cartesian points to a quasi-polar dictionary.
        
        Function transforms Cartesian coordinates to polar coordinates using
        built-in library functions `hypot` and `atan2`. `atan2` is used instead
        of the regular `atan` to preserve direction.
        
        Since we're looking for collisions, only the closest point is kept if
        more than one point exists at the same angle, because all other will
        never be reached.
        
        Args:
            points_list: a list of Cartesian points in the form of (x, y).
        
        Returns:
            A dictionary mapping the keys of angles in radians to shortest
            distance from the origin.
        """
        polar = {}
        for point in point_list:
            # change point to accomodate `atan2`
            # note: `atan2` takes args in y, x order
            point = list(point)
            point.reverse()
            # calculate quasi-polar coordinates
            angle = round(atan2(*point),3)
            r = round(hypot(*point),3)
            try:
                polar[angle] = min(polar[angle], r)
            except:
                polar[angle] = r
        return polar

    # transform `good_guys` and `bad_guys` to quasi-polar coordinate dictionary
    good_guys = quasi_polar(good_guys)
    bad_guys = quasi_polar(bad_guys)
    # count all `bad_guys` get hit without hitting a `good_guy` first
    good_directions = 0
    for key, value in bad_guys.iteritems():
        # count angle if it doesn't have a `good_guy` at the same angle.
        if key not in good_guys.keys():
            good_directions += 1
        # count angle if a `good_guy` is at the same angle, but the `bad_guy` is
        # in front of the `good_guy`.
        elif value < good_guys[key]:
            good_directions += 1
    return good_directions
