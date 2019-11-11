from tools import timing

# recursively
@timing
def knapSack1(W, wt, val, n):
    if W == 0 or n == 0:
        return 0
    # if nth value is greater than W, then it cannot be included
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)

    else:
        # return maximum of include or not include
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                        knapSack(W, wt, val, n-1))


# Dynamic programming
# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
@timing
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

@timing
def knapSackOneList(W, wt, val, n):
    dp = [0 for _ in range(W+1)]
    # Build table K[][] in bottom up manner
    for i in range(1, n):
        for w in range(W, -1, -1):
            if (wt[i] <= w):
                dp[w] = max(dp[w], dp[w-wt[i]] + val[i])
            
    return dp[-1]



# To test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack1(W , wt , val , n))
print(knapSack(W , wt , val , n))
print(knapSackOneList(W , wt , val , n))
