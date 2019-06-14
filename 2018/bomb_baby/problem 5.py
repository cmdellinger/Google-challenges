"""
Google Problem 5: Bomb, Baby!
Written by cmdellinger
    
Usage:
    import solution
    answer(M, F)
    
Returns a string number of generation cycles required to generate #M and #F bombs.
1.  Each generation cycle, either:
        M bombs can generate F bombs
            OR
        F bombs can generate M bombs
2.  If the amount of M and F bombs can't be generated return "impossible"
"""

def answer(M = '', F = ''): # -> string
    ''' returns number of generation cycles as a string needed to generate the passed M and F bombs '''

    def is_possible(bombs = [0,0]): # -> bool
        ''' returns True if both values are greater than 0, else False '''
        if bombs[0] > 0 and bombs[1] > 0:
            return True
        else:
            return False

    # initialize counter
    steps = 0
    # initialize starting step
    generation = [int(M),int(F)]
    
    while is_possible(generation):
        if generation[0] == 1 or generation[1] == 1:
            return str(steps + max(generation)-1)
        else:
            big = max(generation)
            little = min(generation)
            multiplier = big//little
            generation = [little, big - little * multiplier] # order doesn't matter
            steps += multiplier
    return "impossible"

#print answer("2","1")
#print answer("4","7")
