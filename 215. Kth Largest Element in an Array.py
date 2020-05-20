class Solution(object):
    def findKthLargestHeap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        
        for n in nums:
            heapq.heappush(q, n)
            if len(q) > k:
                heapq.heappop(q)
                    
        return heapq.heappop(q)
    
    # quick select
    def findKthLargest(self, nums, k):
        def partition(left, right):
            pivot = nums[right]
            final_pos = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[final_pos] = nums[final_pos], nums[i]
                    final_pos += 1
            # move back to final position
            nums[final_pos], nums[right] = nums[right], nums[final_pos]
            return final_pos
        
        def select(left, right, k):
            if left == right:
                return nums[left]
            
            pivot_idx = partition(left, right)
            if k == pivot_idx:
                return nums[pivot_idx]
            elif k < pivot_idx:
                return select(left, pivot_idx-1, k)
            else:
                return select(pivot_idx+1, right, k)
            
        return select(0, len(nums)-1, len(nums)-k)
