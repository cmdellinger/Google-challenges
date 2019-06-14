"""
Google Problem 2: Bunny Prisoner Locating
Written by cmdellinger
    
Usage:
    import solution
    answer(x,y)
    
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
"""

def triangle_value(number = 0): # -> int
    ''' returns the triangle sequence value [x + (x-1) + (x-2) + ... + 1] at index of input number '''
    try:
        return sum(xrange(number,0,-1))
    except:
        return 0

def prisoner_ID(x = 0, y = 0): # -> int
    ''' returns the prisoner_ID at (x,y) using a combination of triangle numbers '''
    return triangle_value(x) + (triangle_value(y-1+x-1) - triangle_value(x-1))

def answer(x = 0, y = 0): # -> int
    ''' finds the ID for a prisoner at location x,y; assumes x AND y >= 1 '''
    return prisoner_ID(x,y)
