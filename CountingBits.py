# -*- coding: utf-8 -*-
'''
338. Counting Bits
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss?
Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        List = []
        computed = {}
        for i in range(num+1):
            n_one = 0
            while i > 0:
                if i in computed:
                    n_one += computed[i]
                    i = 0
                else:
                    if i % 2 == 1:
                        n_one += 1
                    i /= 2
            computed[i] = n_one
            List.append(n_one)

        return List    

input = 2
cB = Solution()
print(cB.countBits(input))
