/*

Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

The subarray should contain at least one number

您在真实的面试中是否遇到过这个题？  
样例
Example 1:

Input:
[1, 3, -1, 2, -1, 2]
Output:
7
Explanation:
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2].
Example 2:

Input:
[5,4]
Output:
9
Explanation:
the two subarrays are [5] and [4].
挑战
Can you do it in time complexity O(n) ?
*/


class Solution {
public:
    /*
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    int maxTwoSubArrays(vector<int> &nums) {
        // write your code here
        int n = nums.size();
        vector<int> leftSums(n, 0);
        int preSum = 0;
        int minSum1 = 0, maxSum1 = INT_MIN;
        for (int i = 0; i < n; ++i) {
            preSum += nums[i];
            maxSum1 = max(maxSum1, preSum - minSum1);
            minSum1 = min(minSum1, preSum);
            leftSums[i] = maxSum1;
        }
        
        vector<int> rightSums(n, 0);
        preSum = 0;
        int minSum2 = 0, maxSum2 = INT_MIN;
        for (int i = n - 1; i >= 0; --i) {
            preSum += nums[i];
            maxSum2 = max(maxSum2, preSum - minSum2);
            minSum2 = min(minSum2, preSum);
            rightSums[i] = maxSum2;
        }
        
        int maxSum = INT_MIN;
        for (int k = 0; k < n - 1; ++k) {
            maxSum = max(maxSum, leftSums[k] + rightSums[k+1]);
        }
        
        return maxSum;
    }
};
