'''
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return
2 because 13 = 4 + 9.
'''
from tools import timing
import math
class Solution:
    @timing
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        dp = [i for i in range(n+1)]
        dp[0] = 0
        for i in range(1,n+1):
            # print(i, dp[i])
            for j in range(1,int(math.sqrt(i))+1):
                if i >= j*j:
                    dp[i] = min(dp[i-j*j] + 1, dp[i])
                else:
                    break
            # print(i, dp[i])
        return dp[n]

    @timing
    def numSquares(self, n):
        sn = [i*i for i in range(1, int(math.sqrt(n)) + 1)] # square numbers <= n
        level = 0  #BFS level
        current_level = [0] # list of numbers in BFS level l

        while True:
            next_level = []
            for a in current_level:
                for b in sn:

                    if a + b == n :
                        return level + 1
                    if a + b < n:
                        next_level.append(a + b)
            current_level = list(set(next_level))
            level += 1


sol = Solution()
print(sol.numSquares1(23))
print(sol.numSquares(23))
print(sol.numSquares1(4703))
print(sol.numSquares(4703))

print(sol.numSquares1(6704))
print(sol.numSquares(6704))
