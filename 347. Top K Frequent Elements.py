"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from tools import timing

class Solution:
    @timing
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}

        ans = []
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for count in sorted(d.values(), reverse=True)[:k]:
            for key in d.keys():
                if d[key] == count and key not in ans:
                    ans.append(key)
                    break
        return ans
    @timing
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [x[0] for x in Counter(nums).most_common(k)]

nums = [1,1,1,2,2,3]
k = 2
ans = [1,2]
assert Solution().topKFrequent1(nums, k) == ans

assert Solution().topKFrequent(nums, k) == ans
