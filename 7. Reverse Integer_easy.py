"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold 
integers within the 32-bit signed integer range. For the purpose 
of this problem, assume that your function returns 0 when the reversed integer overflows.


"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        sign = x // abs(x)
        
        x = abs(x)
        ans = int(str(x)[::-1])
       
            
        ans = ans * sign
        if ans < -(2**31) or ans > 2**31-1:
            return 0
        return ans
        
   
sol = Solution()
a = 123
assert sol.reverse(a) == 321
assert sol.reverse(-123) == -321
print('Test passed')
