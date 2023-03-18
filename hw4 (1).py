#maria ebrahim
#Pledge: I pledge my honor that I have abided by the stevens honor system

def pascal_row(n):
    ''''returns the list of numbers from pascal row n and the first row starts from 0'''
    if n==0:
        return [1]
    if n == 1:
        return [1,1]
    else:
        return [1]+coe(pascal_row(n-1))+[1]
    
def coe(h):
    '''adds first and second integer of a list, and second and third integer of a list, etc..''' 
    if h == []:
        return []
    if h==[1]:
        return []
    else:
        return [h[0]+h[1]] + coe(h[1:])

def pascal_triangle(z):
    '''takes as input a single integer n and returns a 
    list of lists containing the values of the all the rows up to and including row n'''
    if z==0:
        return [[1]]
    else:
        return pascal_triangle(z-1)+[pascal_row(z)]

def test_pascal_row():
    '''test to check if pascal_row function is returning the correct output'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1, 1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(4) == [1, 4, 6, 4, 1]

def test_pascal_triangle():
    '''test to check if pascal_triangle function is returning the correct output'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
