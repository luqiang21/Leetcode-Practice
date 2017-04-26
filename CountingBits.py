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

'''
一个数 * 2 就是把它的二进制全部左移一位，也就是说 1的个数是相等的。
那么我们可以利用这个结论来做。
res[i /2] 然后看看最低位是否为1即可（上面*2一定是偶数，这边比如15和14除以2都是7，但是15时通过7左移一位并且+1得到，14则是直接左移）
所以res[i] = res[i >>1] + (i&1)

'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        List = [0] * (num + 1)
        for i in range(1, num + 1):
            List[i] = List[i >> 1] + i & 1

        return List

input = 2
cB = Solution()
print(cB.countBits(input))
