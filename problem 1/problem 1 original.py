# -*- coding: UTF-8 -*-

"""
Google Problem 1: Re-ID
Written by cmdellinger

Usage:
  solution.py <int n value>


"""

## ------
## solution
## ------

import sys

def is_prime(number = 0): # -> boolean
    ''' returns whether input number is prime '''
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for factor in xrange(3, int(number**0.5+1), 2):
        if number % factor == 0:
            return False
    return True

def prime_number_string(n = 0): # -> string
    ''' returns a 5 character string from the concatenated prime string '''
    prime_string = ""
    i = 0
    while len(prime_string) < (n + 5):
        i += 1
        if is_prime(i):
            prime_string += str(i)
    return prime_string[n:n+5]

if len(sys.argv) != 2:
    print __doc__
else:
    n = int(sys.argv[1])
    print str(prime_number_string(n))
