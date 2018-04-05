"""
Google Problem: Dodge the Lasers!
Written by cmdellinger
Python version: 2.7

Problem:
Write a function answer(str_n) which, given the string representation of an
integer n, returns the sum of
    (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2)))
as a string. That is, for every number i in the range 1 to n, it adds up all of
the integer portions of i*sqrt(2).

For example, if str_n was "5", the answer would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive.
    
See README for problem details and specifications.
"""

""" Notes about Beatty sequences and calculation:
This sequence is a specific type of sequence called a Beatty sequence.
A Beatty sequence is an sequence in the form floor(r*n) where r is any
irrational number. Beatty sequences have an interesting property where there
are complementary sequences where 1/r + 1/s = 1, which means the sequence for
r and s make up all integers.

From the problem hint, what isn't there could be the s sequence or
2+sqrt(2), but calculating the s sequence and subtracting the sum from the
converged arithmatic sequence sum was still too slow.

This solution uses the recurrence formula of this specific Beatty sequence,
which was found on the Math StackExchange at https://goo.gl/qoHf7A . The comment
on the formula says it reduces the calculations because it is the equivalent of
calculating powers of sqrt(2)-1. Exponentially decreasing arguments results in
much fewer calculation steps than loop iteration of either r or s sequence.
"""

# use decimal library for increased precision due to possiblity of large values
from decimal import Decimal, ROUND_FLOOR, getcontext
getcontext().prec = 200
# values for equation readability of recursive calculation
one = Decimal(1)
two = Decimal(2)
sqrt_2 = Decimal(2).sqrt()

def S(n):
    """ Calculates the sum of floor(i*sqrt(2)) from 1 to n.
    
    This function uses the recurrence formula of this specific Beatty sequence,
    which was found on the Math StackExchange at https://goo.gl/qoHf7A . This
    method reduces the complexity versus sequence calculating with iteration by
    requiring exponentially decreasing Args.
    
    Args:
        n (Decimal): max index as a number stored in a Decimal class instance.
    Returns:
        The sum of the Beatty sequence from 1 to n as a Decimal instance.
    """
    assert type(n) == Decimal, "Function expects a number in Decimal class form"
    if n == 1: return 1
    if n < 1: return 0
    # find n' or floor(sqrt(2)-1) in this case
    n_prime = ((sqrt_2-one)*n).to_integral(rounding=ROUND_FLOOR)
    # reccurance formula for this Beatty sequence
    return (n*n_prime+n*(n+one)/two
            -n_prime*(n_prime+one)/two
            -S(n_prime)
            ).to_integral(rounding=ROUND_FLOOR)

def answer(str_n):
    """ Calculates the sum of floor(i*sqrt(2)) from 1 to n.
       
    This function does input/output conversion and starts the recursive
    calculation of the Beatty sequence.
       
    Args:
        str_n (string): max index as a number stored in a string.
    Returns:
        The sum of the Beatty sequence from 1 to n as a string.
    """
    return str(S(Decimal(str_n)))
