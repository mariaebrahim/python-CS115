'''
Created on 10/20/22
@author:   _Maria Ebrahim
Pledge:    _I pledge my honor that I have abided by the stevens honor system
CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2)+"1"
    else:
        return numToBinary(n//2)+"0"

#42 base-2 is 101010
#If you are given an odd base number 10 the least sgnificant bit in base two will be 1 because the number can not all be factors of two and needs 1 to be taken out if it so that it can be factored by two. However, if you are given an even base 10 number the least significant figure will be 0 because the number can be factored into two.
#If you remove the rightmost digit the number will become smaller because they are shifting the number to the right which will cause all the digits to go back by a smaller factor.
#Given n and n/2=y you can find the base-2 number of n given the base-2 of y if n is even by adding a zero to the end of the base-2 of the base-2 of y. However, if n is odd you add 1 at the end of the base-2 number of y to find n.


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif s[0]=="0":
        return binaryToNum(s[1:])
    else:
        return 2**(len(s)-1)+binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    answer=numToBinary(int(binaryToNum(s))+1)
    if len(answer)<8:
        return str('0'*(8-len(answer)))+answer
    if len(answer)>8:
        return answer[1:]
    else:
        return answer



def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==0:
        print(s)
    else:
        print(s)
        count(increment(s), n-1)

#The base-3 number of 59 is 2012. It is 2012 because there are two intgers that make the number indivisable by 3. There are then 1 "3's" and 2 "27's".

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif n%3==0:
        return numToTernary(n//3)+"0"
    elif n%3==1:
        return numToTernary(n//3)+"1"
    else:
        return numToTernary(n//3)+"2"

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif s[0]=="0":
        return ternaryToNum(s[1:])
    else:
        return (3**(len(s)-1)*int(s[0]))+ternaryToNum(s[1:])
