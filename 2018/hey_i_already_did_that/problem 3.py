"""
Google Problem 3: Hey, I Already Did That!
Written by cmdellinger
    
Usage:
    import solution
    answer(n, b)
    
Take the starting minion ID and returns the length of the loop until the minion ID repeats.

Minions are assigned to tasked based on their minion ID using the following rules:
1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2
"""

def answer(n = '', b = 0): # -> int
    ''' returns the length until repeat for the supplied minion '''

    k = len(n)

    def str_list_to_num(strings = []): # -> int
        ''' returns the integer value of the concatenated number from the digits in the supplied string'''
        return int(''.join(strings),base=b)

    def num_to_str(number = 0): # -> str
        ''' returns a string of the number converted to base b '''
        number_base = ''
        for power in xrange(k-1,-1,-1):
            number_base += str(number // b**power)
            number %= b**power
        return number_base

    def z(n = ''): # -> str
        ''' returns the next n value maintaining string length k'''
        n = list(n)
        y = sorted(n)
        x = sorted(n, reverse=True)
        return num_to_str(str_list_to_num(x) - str_list_to_num(y)).zfill(k)

    minions = [n]
    next_minion = z(minions[0])
    while next_minion not in minions:
        minions.append(next_minion)
        next_minion = z(minions[-1])
    return len(minions[minions.index(next_minion):])
