"""
Google Problem 6: Queue To Do
Written by cmdellinger
    
Usage:
    import solution
    answer(start, length)
    
Returns the hash code made from xor'ed values of a series starting at "start" broken
into lines of passed length, "length". A decreasing amount of values from the series
are passed to xor hash sequence per row.

Rules for the xor sequence:
1. Each line is the same length
2. The first line passes all values to the xor sequence.
3. Each successive row passes one less value to the xor sequence
4. The hash is generated when zero length is reached

Example:
    start = 0
    length = 3

    0 1 2 /
    3 4 / 5
    6 / 7 8

    XOR hash: 0^1^2^3^4^6 == 2
"""
from operator import xor

def answer(start = 0, length = 0): # -> int
    ''' returns the hash generated from IDs in sequence starting with "start"
        and line lengths of passed length, "length". '''
    
    def f(n = 0): #-> int
        ''' returns the xor of [0,n] which is a repeating sequence of n,1,n+1,0 '''
        switch = {0: n, 1: 1, 2: n+1, 3: 0}
        return switch[n%4]
    
    def xor_sequence(seq_start = 0, seq_end = 0): # -> int
        ''' return the xor of seq_start to seq_end.
            essentially xor-ing with f(seq_start-1) negates all below seq_start '''
        return f(seq_end) ^ f(seq_start-1)
    
    xor_total = 0
    for row in xrange(length):
        xor_total ^= xor_sequence(start+row*length, start+row*length+(length-row)-1)
    return xor_total

print "answer(0,3)"
print answer(0,3)
print "answer(17,4)"
print answer(17,4)
