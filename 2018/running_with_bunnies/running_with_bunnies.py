"""
Google Problem: Running with Bunnies
Written by cmdellinger
Python version: 2.7
    
Problem:
Write a function of the form answer(times, time_limit) to calculate the most
bunnies you can pick up and which bunnies they are, while still escaping through
the bulkhead before the doors close for good. If there are multiple sets of
bunnies of the same size, return the set of bunnies with the lowest prisoner IDs
(as indexes) in sorted order. The bunnies are represented as a sorted list by
prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and
time_limit is a non-negative integer that is at most 999.
    
See README for problem details and specifications.
    
Algorithm breakdown:
* relax edges using Floyd-Warshall algorithm since edge weights are + and -
* check for negative loops
* check bunny permutations to find max retrievable in the time limit
"""


def answer(times, time_limit):
    """ Determines the maximum amount of bunnies that can be rescued.
        
    Args:
        times (int matrix): matrix of unidirectional time weights of node edges.
                            example: w(u,v) -> times[u][v]; w(u,v) != w(v,u)
        time_limit (int): time limit to collect all bunnies (max path distance).
    Returns:
        A sorted list containing the bunny indices for the maximum amount that
        can be rescued. if multiple solutions exist, priority is for permutation
        with lower node indices.
    """
    from itertools import product, permutations
    V = len(times)
    # check for edge case of no bunnies
    if V <= 2:
        return []
    # relax edges based on Floyd-Warshall algorithm
    for k, i, j in product(range(V), repeat=3):
        times[i][j] = min(times[i][j],
                          times[i][k]+ times[k][j])
    # check for negative loops
    if any([times[i][i] < 0 for i in range(V)]):
        return range(V-2)

    def path_distance(bunny_sequence):
        """ helper function: finds the distance of the complete path from the
            sequence of bunnies to be saved """
        path = [0] + list(bunny_sequence) + [V-1] #add start and end indices
        return sum(times[path[i]][path[i+1]] for i in range(len(path)-1))

    # check path permutations with decreasing bunny quantities to yield max. the
    # `permutations` generator goes in increasing order, so escaping the loop
    # for the first found, will give the lowest bunny values.
    bunny_nodes = range(1, V-1) # name bunny indices for readablity
    for max_bunnies in range(V-2, -1, -1):
        for bunny_sequence in permutations(bunny_nodes, max_bunnies):
            if path_distance(bunny_sequence) <= time_limit:
                return sorted(map(lambda x: x-1, bunny_sequence))
