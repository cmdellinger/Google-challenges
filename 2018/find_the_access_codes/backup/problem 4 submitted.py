"""
Google Problem 4: Find the Access Codes
Written by cmdellinger
    
Usage:
    import solution
    answer(l)
    
Returns a list of "lucky triples" using the elements in supplies list.
A lucky triple is a tuples (x,y,x) where:
1.  x < y < z
2.  y % x = 0
3.  z % y = 0
"""

def remove_duplicates(list = []): # - > []
    ''' returns the list without duplicates '''
    seen = []
    clean_list = []
    for item in list:
        if item not in seen:
            seen.append(item)
            clean_list.append(item)
    return clean_list

def answer(l = []): # -> int
    ''' returns number of "lucky triples" (x,y,z) where x<y<z, y%x=0, and z%y=0 '''

    def find_next_element(prior_element = 0): # -> []
        ''' returns a list of numbers in remainder of list divisible by the input element; assumes ascending sorted '''
        return [element for element in l[l.index(prior_element)+1:] if element % prior_element == 0]

    l = sorted(l)
    lucky_triples = []
    for element in l:
        lucky_triples.extend([[element, second_element, third_element] for second_element in find_next_element(element) for third_element in find_next_element(second_element)])
    return len(remove_duplicates(lucky_triples))

print answer([1, 1, 1])
print answer([1, 2, 3, 4, 5, 6])
