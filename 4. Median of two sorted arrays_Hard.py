'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
from tools import timing

class Solution:
    # used merge sort, complexity O(m+n)
    @timing
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j, k = 0, 0, 0
        combined = []
        mid = (len(nums1) + len(nums2)) // 2
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1
            k += 1
            if k > mid:
                break
        if k <= mid:
            if i < len(nums1):
                combined.extend(nums1[i:])
            else:
                combined.extend(nums2[j:])

        if (len(nums1) + len(nums2))%2 == 0:
            return (combined[mid] + combined[mid-1]) / 2
        else:
            return combined[mid]

    # sort will use complexity of O(nlog(n))
    @timing
    def findMedianSortedArrays2(self, nums1, nums2) :
        nums1.extend(nums2)
        tmp = sorted(nums1)
        if len(tmp)%2 == 0:
            return (tmp[len(tmp)//2] + tmp[len(tmp)//2 - 1])/2
        else:
            return tmp[len(tmp)//2]

    # from leetcode solution, not yet fully understand it.
    @timing
    # from leetcode solution, not yet fully understand it.
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A = nums1
        B = nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

nums1 = [1, 3]
nums2 = [2]
ans = 2
sol = Solution()
assert sol.findMedianSortedArrays1(nums1, nums2) == ans
assert sol.findMedianSortedArrays2(nums1, nums2) == ans
# assert sol.findMedianSortedArrays(nums1, nums2) == ans, sol.findMedianSortedArrays(nums1, nums2)

nums1 = [1, 2]
nums2 = [3, 4]
ans = 2.5
assert sol.findMedianSortedArrays1(nums1, nums2) == ans
assert sol.findMedianSortedArrays2(nums1, nums2) == ans
# assert sol.findMedianSortedArrays(nums1, nums2) == ans, sol.findMedianSortedArrays(nums1, nums2)

print('tests passed.')
