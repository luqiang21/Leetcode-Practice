"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""
from tools import timing

class Solution:
    @timing
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        opens = ["(", "[", "{"]
        pairs = ["()", "[]", "{}"]
        for ch in s:
            if ch in opens:
                stack.append(ch)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last + ch not in pairs:
                    return False

        return len(stack) == 0
s = "{}"
assert Solution().isValid(s) == True
s = "{{{{{{{{[(]}}}}}}}}"
assert Solution().isValid(s) == False
