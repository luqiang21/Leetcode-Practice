"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""
from tools import timing
class Solution:
    @timing
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letter = [" ", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if digits == None or len(digits) == 0:
            return []
        res = []
        temp = []
        self.backtracking(res, digits, temp, letter, 0)
        return res

    def backtracking(self, res, digits, temp, letter, start):
        if len(temp) == len(digits):
            res.append("".join(temp[:]))

        for i in range(start, len(digits)):
            index = int(digits[i])
            for j in range(len(letter[index])):
                temp.append(letter[index][j])
                self.backtracking(res, digits, temp, letter, i+1)
                temp.pop()

assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
