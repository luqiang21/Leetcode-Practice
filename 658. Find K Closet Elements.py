#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
'''


"""
策略:我们需要首先定位给定元素和给定数组的相对位置关系，给元素是否在数组中，如果在数组中，
或者给定的元素的值能否在给定的数组区间中，那么我们需要找到该元素的位置，或者最佳插入位置，
对于在一个有序数组中位置查找的方法最快的是二分法；如果不在数组中，并且值也不在给定数组区间中，
我们需要确定该元素是在数组的最左侧还是最右侧。确定该元素和数组之间的相对位置之后，我们就有了选择策略。

如果该元素在数组中/值在数组区间中，我们找到了其所在位置index/插入index，那么我们的k个元素的选择策略就是冲该元素开始，
向两边方向进行元素选取，首先选择离该元素最近的左右两侧的元素，知道一共选取k个元素

如果该元素在数组的最左侧，并且不在数组之中，那么我们从数组的最左侧元素开始，一共选取k个元素

同理，如果该元素在数组最右侧，并且不在数组之中，那么我们从数组的最右侧开始选取，一共选取k个元素

改进：以上策略比较中庸，算法需要考虑诸多情况，并不是一个优化解决方案，我们看看如何优化解法。

思考角度：反向思考。因为正向思考我们需要考虑太多边界问题，那么我们尝试从反向思考，看看是否能够简化问题。
我们需要从数组中选取k个元素，那么我们的等价反向思考转化为同等问题：从数组中删除length - k个元素的问题。

新策略：由于数组是升序数组，那么如果我们要从数组中删除length - k个元素，那么这些元素一定是重端点两侧开始进行选取的，
不可能从中间某个元素开始。在这个分析的基础之上，我们的优化策略为比较数组两端的元素和给定元素x的绝对差值，
我们删除差值大的元素，然后再取出数组的两端元素，比较其和x的差值大小，再删除差值大的元素，然后依次循环，直到数组中只剩下k个元素，至此，问题得到完美解决。

作者：龙之力量V
链接：http://www.jianshu.com/p/c27e27907af2
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""

class Solution():
    """docstring for Solution."""
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        '''
        Analysis:
        - Reverse thinking: select k element = remove size - k elements
        - notice that the arr is already sorted, so if we need to remove any element,
          it's gonna be from the two ends first
        '''


        if not arr:
            return []
        arr1 = arr[:]
        while len(arr1) > k:
            # print arr1
            if abs(arr1[0] - x) > abs(arr1[-1] - x):
                arr1.pop(0)
            else:
                arr1.pop(-1)

        return arr1

sol = Solution()
arr = [1,2,3,4,5]
print('array is', arr)
print('k 4, x 3', sol.findClosestElements(arr, 4, 3))
print('k 4 x -1', sol.findClosestElements(arr, 4, -1))
print('k 2 x 3', sol.findClosestElements(arr, 2, 3))
print('k 2 x 7', sol.findClosestElements(arr, 2, 7))
