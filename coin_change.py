#!/bin/python3

import sys

from tools import timing

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(S, m, n ):

    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <=0 and n >= 1):
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] );
@timing
def make_change1(coins, n):
    m = len(coins)
    return count(coins, m, n)


@timing
def make_change2(coins, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    num_ways = 0
    dic_ways = {}
    for i in range(len(coins)):
        coin = coins[i]
        if n-coin not in dic_ways:
            num_ways += make_change(coins[i:], n - coin)
            dic_ways[n-coin] = True
    return num_ways

@timing
def make_change(coins, n):
    dp = [0] * (n+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, n+1):
            dp[i] += dp[i-coin]
    return dp[n]
n,m = 4, 3
coins = [1,2,3]
print(make_change1(coins, n))
print(make_change2(coins, n))
print(make_change(coins, n))

n, m = 10, 4
coins = [2,3,5,6]
print(make_change1(coins, n))
print(make_change2(coins, n))
print(make_change(coins, n))
