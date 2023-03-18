'''
Created on 10/25/22
@author:   Maria Ebrahim
Pledge:    I pledge my honor that I have abided by the stevens honor system

CS115 - Hw 5 
'''
memo={}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if (n) in memo:
        return memo[(n)]
    elif n == 0:
        memo[(n)]=2
        return 2
    elif n == 1:
        memo[(n)]=1
        return 1
    else:
        x=fast_lucas(n-1) + fast_lucas(n-2)
        memo[(n)]=x
        return x 


def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    coins=tuple(coins)
    if (amount, coins) in memo:
        return memo[(amount, coins)]
    if amount<=0:
        memo[(amount, coins)]= 0
        return 0
    elif coins==():
        memo[(amount, coins)]=float("inf")
        return float("inf")
    elif coins[0]>amount:
        memo[(amount, coins)]= fast_change(amount, coins[1:])
        return fast_change(amount, coins[1:])
    else:
        loseit=fast_change(amount, coins[1:])
        useit=1+fast_change(amount-coins[0], coins)
        x=min(useit, loseit)
        memo[(amount, coins)]=x
        return x
        
                           
        

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76

print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))


