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
    xor_total = 0
    for row in xrange(length):
        for value in xrange(start+row*length, start+row*length+(length-row)):
            xor_total ^= value
    return xor_total

print answer(0,3)
print answer(17,4)
