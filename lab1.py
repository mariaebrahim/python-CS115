############################################################
# Name: Maria Ebrahim
# Pledge:I pledge my Honor that I have abided by the Stevens Honor System
# CS115 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    '''takes a umber "x" as input and returns its reciprocal'''
    return 1.0/x

def sum(x, y):
    '''returns the sum of x and y'''
    return x + y

def e(n):
    '''takes "n" as an input and returns the sum of the range and its reciprocal factorially'''
    list=range(1,n+1)
    list=map(factorial,list)
    return 1+ reduce(sum, map(inverse,list))





