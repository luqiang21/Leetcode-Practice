class Solution {
public:
    int mincostTicketsFromOther(vector<int>& days, vector<int>& costs) {
        vector<int> dp(days.size() + 1);
        int pWeek = days.size() - 1, pMonth = pWeek;
        dp.back() = 0;
        
        for (int cur = days.size() - 1; cur >= 0; --cur) {
            while (days[pWeek] - days[cur] >= 7) pWeek--;
            while (days[pMonth] - days[cur] >= 30) pMonth--;
            
            dp[cur] = min(costs[0] + dp[cur + 1],
                         min(costs[1] + dp[pWeek + 1],
                            costs[2] + dp[pMonth + 1]));
        }
        
        return dp[0];
    }
    
    int mincostTicketsForward(vector<int>& days, vector<int>& costs) {
        vector<int> dp(days.size() + 1);
        int pWeek = 1, pMonth = 1;
        dp[0] = 0;
        for (int i = 1; i <= days.size(); ++i) {
            while (days[i-1] - days[pWeek-1] >= 7) pWeek++;
            while (days[i-1] - days[pMonth-1] >= 30) pMonth++;
            
            dp[i] = min(costs[0] + dp[i-1],
                       min(costs[1] + dp[pWeek-1],
                           costs[2] + dp[pMonth-1]));
        }
        return dp.back();
    }
    
    // buy tickets for 7/30 every travel day. Use earliest to compare
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        int cost = 0;
        queue<pair<int, int>> last7, last30;
        
        for (auto& day : days) {
            while (!last7.empty() && last7.front().first + 7 <= day) last7.pop();
            while (!last30.empty() && last30.front().first + 30 <= day) last30.pop();
            
            last7.push({day, cost + costs[1]});
            last30.push({day, cost + costs[2]});
            cost = min(cost + costs[0], min(last7.front().second,
                                            last30.front().second));
        }
        
        return cost;
    }
};
