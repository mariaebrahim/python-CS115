'''
Created on october 11, 2022
@author:   Maria Ebrahim
Pledge:    I pledge my honor that I have abided by the stevens honor system.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#code takes a while to load while you run it when checking the code just let curser blink for a while
def giveChange(amount, coins):
    '''return the least amount of coins neede to make up the "amount" and a list of the coins that were used'''
    return [change(amount, coins), listy(amount, coins)]


def change(amount, coins):
    '''returns the least amount of coins needed to make up the "amount"'''
    if amount==0:
        return 0
    elif coins==[]:
        return float("inf")
    elif coins[0]>amount:
        return change(amount, coins[1:])
    else:
        loseit=change(amount, coins[1:])
        useit=1+change(amount-coins[0], coins)
        return min(useit, loseit)

def listy(amount, coins):
    '''returns a list of the leats amount of coins used to make up "amount"'''
    if amount==0:
        return []
    elif coins==[]:
        return []
    elif coins[0]>amount:
        return listy(amount, coins[1:])
    else:
        use=[coins[0]]+listy(amount-coins[0], coins)
        lose=listy(amount, coins[1:])
        if change(amount, use)<change(amount, lose):
            return use
        else:
            return lose
                    

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct==[] or scores==[]:
        return []
    else:
        return [[dct[0], wordScore(dct[0], scores)]]+wordsWithScore(dct[1:], scores)


def letterScore(letter, scorelist):
    '''takes a letter and returns the score of that letter from a score list'''
    if letter=='':
        return 0
    elif scorelist==[]:
        return 0
    elif letter==scorelist[0][0]:
        return scorelist[0][-1]
    else:
        return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    '''takes a word and returns the score of that word by adding up all the values of the indovidual letters from a score list'''
    if S=='':
        return 0
    else:
        return letterScore(S[0], scorelist)+wordScore(S[1:], scorelist)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n==0:
        return []
    else:
        return [L[0]]+take(n-1, L[1:])



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n==0:
        return L
    else:
        return drop(n-1, L[1:])


