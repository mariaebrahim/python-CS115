#maria ebrahim
#I pledge my honor that I have abided by the stevens honor system.

def value(capacity, itemList):
    '''Return ths max value of what you can get from the list without exceeding capacity'''
    if capacity==0 or itemList==[]:
        return 0
    elif capacity<0:
        return -float('inf')
    elif itemList[0][0]>capacity:
        return value(capacity, itemList[1:])
    else:
        use=itemList[0][-1]+value((capacity-itemList[0][0]), itemList[1:])
        lose=value(capacity, itemList[1:])
        return max(use, lose)

def listy(capacity, itemList):
    '''Returns the list of items with the maxium value without exceeding capacity'''
    if capacity==0 or itemList==[]:
        return []
    elif capacity<0:
        return [-float('inf')]
    elif itemList[0][0]>capacity:
        return listy(capacity, itemList[1:])
    use=[itemList[0]]+listy(capacity-itemList[0][0], itemList[1:])
    lose=listy(capacity, itemList[1:])
    if value(capacity, use)>value(capacity, lose):
        return use
    else:
        return lose

def knapsack(capacity, itemList):
    '''returns the maxiumum value without exceeding capacity and returns a list of the the lists that make up that value'''
    return [value(capacity, itemList), listy(capacity, itemList)]

