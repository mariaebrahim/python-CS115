'''
Created on _9/29/22
@author:   _maria ebrahim
Pledge:    i pledge my honor that I have abided by the stevens honor system
CS115 - Hw 2
'''
import sys
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1], 
["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8], ["k", 5], ["l", 1], 
["m", 3], ["n", 1], ["o", 1], ["p", 3], ["q", 10], ["r", 1], ["s", 1], 
["t", 1], ["u", 1], ["v", 4], ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]

Dictionary = ["a", "am", "at", "apple", "bat", "bar", "babble", "can", "foo", 
"spam", "spammy", "zzyzva"]

from functools import reduce

# Implement your functions here.

def letterScore(letter, scorelist):
    '''takes a letter and returns the score of that letter from a score list'''
    if letter=="":
        return 0
    elif scorelist==[]:
        return 0
    elif letter==scorelist[0][0]:
        return scorelist[0][-1]
    else:
        return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    '''takes a word and returns the score of that word by adding up all the values of the indovidual letters from a score list'''
    if S=="":
        return 0
    else:
        return letterScore(S[0], scorelist)+wordScore(S[1:], scorelist)

def scoreList(Rack):
    '''returns a set of words from the dictionary that can be made up by the letters provided in the Rack along with their scores''' 
    if Rack==[]:
        return []
    elif Rack[0]==Dictionary[0]:
        return

def bestWord(Rack):
    '''takes a set of letter and combine sthem to make a word from a dcitionary along with their alue and returns the word that can be made iwth the highest score'''
    if Rack==[]:
        return []
    elif Rack[0][0]==Dictionary[0][0]:
        return scoreList(Rack[0]) + [Rack[1:][0]]
    else:
        loseit=bestWord(Rack[1:])
        useit=Rack[0]+[bestWord(Rack[1:])]
        return max(useit, loseit)

def Dic(word, dicti):
    '''prints the letter/word in list form with the attached scorelist'''
    if dicti==[]:
        return []
    elif word==[]:
        return ""
    elif dicti[0][0]==word[0]:
        return [word[0]] + Dic(word[1:], dicti)
    else:
        return Dic(word[0], dicti[1:][0])
def Dic(letter, dicti):
    if letter=="" or letter==[]:
        return []
    elif letter==dicti[0]:
        return letter
    elif letter==dicti[1][0]:
        return letter
    else:
        return Dic(letter, dicti[2:][0])

def fil(x, y):
    '''filters if the letters in the Rcak are in the dictionary'''
    if x==y[0]:
        return x + fil(x[1:], y[0:])
    elif x=="":
        return 0
    elif y==[]:
        return []
    else:
        return fil(x[0], y[1:])



#creates a reduce funstion after to compress list
