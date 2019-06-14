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

def answer(l = []): # -> int
    ''' returns number of "lucky triples" (x,y,z) where x<y<z, y%x=0, and z%y=0 '''

    l = sorted(l)
    index_map = {}
    for index in xrange(len(l)):
        indices = [next_index for next_index in xrange(index+1,len(l)) if l[next_index] % l[index] == 0 and index + 1 != len(l)-1]
        try:
            index_map[l[index]].extend(indices)
        except KeyError:
            index_map[l[index]] = indices
    #print index_map

    lucky_triples = []
    for key in index_map:
        lucky_triples.extend([[key, l[i], l[j]] for i in index_map[key] for j in index_map[l[i]] if j > i])
    #print lucky_triples
    return len(lucky_triples)

print answer([1, 1, 1])
print answer([1, 2, 3, 4, 5, 6])
