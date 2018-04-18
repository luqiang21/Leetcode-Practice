"""
Given a collection of intervals, merge all overlapping intervals.

Example:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

"""

from tools import timing
# good answer from others

class Solution1:
    def merge(self, intervals):
      new_intervals = []
      for interval in sorted(intervals, key=lambda i: i.start):
        if new_intervals and interval.start <= new_intervals[-1].end:
          new_intervals[-1].end = max(new_intervals[-1].end, interval.end)
        else:
          new_intervals.append(interval)
      return new_intervals


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    @timing
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return []
        res = []
        intervals.sort(key=lambda x:x.start)
        lb, ub = intervals[0].start, intervals[0].end


        for interval in intervals:
            if interval.start > ub:
                res.append([lb, ub])
                lb, ub = interval.start, interval.end
            else:
                ub = max(ub, interval.end)

        if not res or lb != res[-1][0]:
            res.append([lb, ub])
        return res

i1 = Interval(1, 3)
i2 = Interval(2, 6)
i3 = Interval(8, 10)
i4 = Interval(15, 18)
intervals = [i1, i2, i3, i4]
assert Solution().merge(intervals) == [[1,6],[8,10],[15,18]]
