"""
Determine whether an integer is a palindrome. Do this without extra space.


Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem
"Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

from tools import timing

class Solution:
    @timing
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        mid = len(x_str) // 2
        for l in range(mid):
            if x_str[l] != x_str[len(x_str) - l - 1]:
                return False
        return True

    @timing
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

    @timing
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # construct the reversed number.
        original = x
        compare = 0
        while x > 0:
            compare = compare * 10 + x % 10
            x = x // 10
        return original == compare


sol = Solution()
x = -2147483648

assert sol.isPalindrome1(x) == False
assert sol.isPalindrome2(x) == False
assert sol.isPalindrome(x) == False
print()
x = 121

assert sol.isPalindrome1(x) == True
assert sol.isPalindrome2(x) == True
assert sol.isPalindrome(x) == True
print()
x = -222

assert sol.isPalindrome1(x) == False
assert sol.isPalindrome2(x) == False
assert sol.isPalindrome(x) == False

print ("Test passed.")
