#maria ebrahim
#I pledge my honor that I have abided by the Stevens Honor System.

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
        useit=1+change(amount-coins[0], coins[0:])
        return min(useit, loseit)
