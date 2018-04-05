"""
Google Problem: Bunny Prisoner Locating
Written by cmdellinger
Python version: 2.7
    
Problem:
Returns the prisoner ID number corresponding to the (x,y) location of a prison block.
Prison blocks are stacked in a triangular shape.
    
Example:
| 7
| 4 8
| 2 5 9
| 1 3 6 10
    
x starts at the wall and increments away from the wall.
y starts at the base and increments up.
both x and y indices start at 1.

Write a function answer(x, y) which returns the prisoner ID of the bunny at
location (x, y). Each value of x and y will be at least 1 and no greater than
100,000. Since the prisoner ID can be very large, return your answer as a string
representation of the number.
"""

def range_sum(number):
    ''' calculates the sum of the range with max of passed number '''
    # formula for convergence of arithmatic sum
    return number*(number+1)/2

def prisoner_ID(x, y):
    ''' calculates the prisoner_ID at (x,y).'''
    # reduced formula of: range_sum(x) + (range_sum(y-1+x-1) - range_sum(x-1))
    return x + range_sum(y-1+x-1)

def answer(x, y):
    ''' finds the ID for a prisoner at location x,y (assumes x AND y >= 1).
        
        Args:
            x (int): x coordinate of the prisoner's cell
            y (int): y coordinate of the prisoner's cell
        Returns:
            The prisoner_ID number contained in the cell (x,y) as a string.
    '''
    return str(prisoner_ID(x,y))

if __name__ == "__main__":
    print "test1: answer(3,2) = \"9\""
    print "output:", answer(3,2)
    print "test2: answer(5,10) = \"96\""
    print "output:", answer(5,10)
