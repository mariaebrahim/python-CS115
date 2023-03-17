###################################################################################
#####Name: Maria Ebrahim
#####Pledge: I pledge my honor that I have abided by the Stevens Honor System
#####Date: 9/22/22
####################################################################

def dot(L,K):
    '''multiplies the same number array of the lists' L and K and then adds them together'''
    if L==[] or K==[]:
        return 0.0
    else:
        return L[0]*K[0]+ dot(L[1:],K[1:])
def explode(S):
    '''take a string S as input and returns a list of the characters (each of which is a string of length 1) in that string'''
    if S=="":
        return []
    else:
        return [S[0]]+explode(S[1:])

def ind(e,L):
    '''finds the index of e in the list L'''
    if L==[] or L=="":
        return 0
    elif e==L[0]:
        return 0
    else:
        return 1+ind(e,L[1:])


def removeALL(e,L):
    '''takes  e and a list L and returns another list that is identical to L except that all elements identical to e have been removed'''
    if L==[]:
        return []
    elif e!=L[0]:
        return [L[0]]+removeALL(e,L[1:])
    else:
        return removeALL(e,L[1:])


def myFilter(x,L):
    '''removes all values untrue of x in L list'''
    if L==[]:
        return[]
    elif x(L[0]):
        return [L[0]]+myFilter(x,L[1:])
    else:
        myFilter(x,L[1:])


def deepReverse(L):
    '''takes a list of elements where some of those elements may be lists  themselves and returns the reversal of the list where, additionally, any element that is a list is also reversed'''
    if L==[]:
        return []
    if isinstance(L[0],list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]
