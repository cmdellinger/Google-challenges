"""
Google Problem 4: Find the Access Codes
Written by cmdellinger
    
Usage:
    import solution
    answer(l)
    
Returns the number of "lucky triples" contained in supplied list.
A lucky triple is a tuples (x,y,x) where:
1.  y % x = 0
2.  z % y = 0
3.  indices of x < y < z
"""

def answer(l = []): # -> int
    ''' returns number of "lucky triples" (x,y,z) where y%x=0, z%y=0, indices of x<y<z '''
    # create an index map containing index of divisors for each index
    index_map = {}
    for index in xrange(len(l)):
        divisor_indices = [divisor for divisor in xrange(index) if l[index] % l[divisor] == 0]
        index_map[index] = divisor_indices
    # return a count of second tier divisors for each index
    return sum([len(index_map[next_key]) for key in index_map for next_key in index_map[key]])
