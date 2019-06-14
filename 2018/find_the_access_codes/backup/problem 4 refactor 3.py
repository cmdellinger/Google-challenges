"""
Google Problem 4: Find the Access Codes
Written by cmdellinger
    
Usage:
    import solution
    answer(l)
    
Returns a list of "lucky triples" using the elements in supplies list.
A lucky triple is a tuples (x,y,x) where:
1.  x < y < z
2.  y % x = 0
3.  z % y = 0
"""
from itertools import combinations

def answer(l = []): # -> int
    ''' returns number of "lucky triples" (x,y,z) where x<y<z, y%x=0, and z%y=0 '''
    return len([tuple for tuple in combinations(l,3) if tuple[1] % tuple[0] == 0 and tuple[2] % tuple[1] == 0])

    #    lucky_triples = [triple in combinations(l,3) if triple[1] % triple[0] == 0 and triple[2] % triple[1] == 0]
    #   print lucky_triples
    #   return len(lucky_triples)

    

print answer([1, 1, 1])
print answer([1, 2, 3, 4, 5, 6])
