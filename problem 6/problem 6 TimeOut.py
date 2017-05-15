"""
Google Problem 6: Queue To Do
Written by cmdellinger
    
Usage:
    import solution
    answer(start, length)
    

"""
from operator import xor

def answer(start = 0, length = 0): # -> int
    ''' asdf '''
    ID_list = []
    for row in xrange(length):
        ID_list.append(reduce(xor,xrange(start+row*length, start+row*length+(length-row))))
    hash = reduce(xor,ID_list)
    return hash

print answer(0,3)
print answer(17,4)
