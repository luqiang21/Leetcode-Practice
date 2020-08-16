/*
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

*/


class Solution {
public:
    int maxProfit1(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int>(5));
        // 5 states, initial, 1st buy, 1st sell, 2nd buy, 2nd sell
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        dp[0][2] = 0;
        dp[0][3] = -INT_MAX; // not happened yet, so negative inf
        dp[0][4] = 0;
        
        for (int i = 1; i < n; ++i) {
            dp[i][0] = 0;
            // first transaction
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]);
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i]);
            
            // second transaction
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i]);
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]);
        }
        
        return max(dp[n-1][0], max(dp[n-1][2], dp[n-1][4]));
    }
    
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        
        int n = prices.size();
        // 5 states, initial, 1st buy, 1st sell, 2nd buy, 2nd sell
        int s1, s2, s3, s4, s5;
        s1 = 0;
        s2 = -prices[0];
        s3 = 0;
        s4 = -INT_MAX;
        s5 = 0;
        
        for (int i = 1; i < n; ++i) {
            s1 = 0;
            // first transaction
            s2 = max(s2, s1 - prices[i]);
            s3 = max(s3, s2 + prices[i]);
            
            // second transaction
            s4 = max(s4, s3 - prices[i]);
            s5 = max(s5, s4 + prices[i]);
        }
        
        return max(s1, max(s3, s5));
    }
};
