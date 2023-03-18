'''
Created on 11/2/2022
@author:   Maria Ebrahim and Christian Hulson-Vogelmann
Pledge:    I pledge my honor that I have abided by the Stevens honor system

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def helper(s):
    '''returns number of 1s and 0s in a row'''
    if s=='':
        return 0
    elif len(s)==1:
        return 1
    elif s[0]==s[1]:
        return 1+helper(s[1:])
    else:
        return 1

def pad(n):
    '''padded binary string'''
    st=numToBinary(n)
    return '0'*(COMPRESSED_BLOCK_SIZE-len(st))+st

def comphelp(s,b):
    '''returns runlength encoded'''
    if s=='':
        return ''
    elif int(s[0])!=b:
        return pad(0)+comphelp(s,1-b)
    else:
        length=min(helper(s), MAX_RUN_LENGTH)
        return pad(length) + comphelp(s[length:], 1-b)
def uncomphelp(s, b):
    '''undoes runlength encoded'''
    if s=='':
        return ''
    else:
        n=binaryToNum(s[:COMPRESSED_BLOCK_SIZE])
        return str(b)*n+uncomphelp(s[COMPRESSED_BLOCK_SIZE:], 1-b)

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2)+'1'
    else:
        return numToBinary(n//2)+'0'

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    elif s[0]=='0':
        return binaryToNum(s[1:])
    else:
        return 2**(len(s)-1)+binaryToNum(s[1:])

def compress(s):
    '''calls comphelp'''
    return comphelp(s, 0)
def uncompress(s):
    '''calls uncomphelp'''
    return uncomphelp(s, 0)
def compression(s):
    '''find the ratio of compress to the length of s'''
    return len(compress(s))/len(s)
