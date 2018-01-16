"""
Google Problem 6: Queue To Do
Written by cmdellinger
    
Usage:
    import solution
    answer(start, length)
    

"""
from operator import xor

def answer1(start = 0, length = 0): # -> int
    ''' asdf '''
    xor_total = 0
    for row in xrange(length):
        row_total = reduce(xor, [value for value in xrange(start+row*length, start+row*length+(length-row))])
        print row_total
        xor_total ^= row_total
    return xor_total

def answer2(start = 0, length = 0): # -> int
    ''' asdf '''
    def f(n = 0): #-> int
        ''' returns the xor of [0,n] which is a repeating sequence of n,1,n+1,0 '''
        switch = {0: n, 1: 1, 2: n+1, 3: 0}
        return switch[n%4]
    
    def xor_sequence(seq_start = 0, seq_end = 0):
        ''' return the xor of seq_start to seq_end.
            essentially xor-ing with f(seq_start-1) negates all below seq_start '''
        return f(seq_start) ^ f(seq_end-1)
    
    xor_total = 0
    for row in xrange(length):
        row_start = start+row*length
        row_end = start+row*length+(length-row)-1
        row_total = xor_sequence(row_start, row_end)
        print row_total
        xor_total ^= row_total
    return xor_total


print "answer1(0,3)"
print answer1(0,3)
print "answer2(0,3)"
print answer2(0,3)
print "answer1(17,4)"
print answer1(17,4)
print "answer2(17,4)"
print answer2(17,4)
