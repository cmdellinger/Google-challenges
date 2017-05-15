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
    goal = {M: int(M), F: int(F)}
    
    def step(counter = (0,0,0)): # -> int
        ''' description '''
        def gen_M(counter = ()): # -> int
            gen_counter = (counter[0]+1, counter[1]+counter[2], counter[2])
            return step(gen_counter)
                 
        def gen_F(counter = ()): # -> int
            gen_counter = (counter[0]+1, counter[1], counter[1]+counter[2])
            return step(gen_counter)
        
        if counter[1] == goal[M] and counter[2] == goal[F]:
            return counter[0]
        elif counter[1] > goal[M] or counter[2] > goal[F]:
            return -1
        else:
            return max(gen_M(counter), gen_F(counter))

    steps = step((0,1,1))
    if steps == -1:
        return "impossible"
    else:
        return str(steps)

#print answer("2","1")
#print answer("4","7")
