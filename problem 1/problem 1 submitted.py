"""
Google Problem 1: Re-ID
Written by cmdellinger
    
Usage:
    import solution
    answer(n)
    
Answer outputs a 5 character string from a string of concatenated prime numbers
starting at the index of the input number.
"""

def is_prime(number = 0): # -> boolean
    ''' returns whether input is a prime number '''
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
    ''' returns a 5 character string from a concatenated prime string
        starting at index of input '''
    prime_string = ''
    i = 0
    while len(prime_string) < (n+5):
        i += 1
        if is_prime(i):
            prime_string += str(i)
    return prime_string[n:n+5]

def answer(n = 0): # -> string
    ''' returns a 5 character string from a concatenated prime string
        starting at index of input '''
    return prime_number_string(n)
