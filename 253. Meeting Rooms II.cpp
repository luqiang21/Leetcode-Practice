/*
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

*/


class Solution {
public:
    int minMeetingRooms1(vector<vector<int>>& intervals) {
        if (intervals.size() < 1) return 0;
        sort(intervals.begin(), intervals.end());
        priority_queue<int, vector<int>, greater<int>> freeRooms;
        freeRooms.push(intervals[0][1]);
        
        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] >= freeRooms.top())
                freeRooms.pop();
            freeRooms.push(intervals[i][1]);
        }
        return freeRooms.size();
    }
    
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if (intervals.size() < 1) return 0;
        vector<int> starts, ends;
        for (const auto& inter : intervals) {
            starts.push_back(inter[0]);
            ends.push_back(inter[1]);
        }
        
        sort(starts.begin(), starts.end());
        sort(ends.begin(), ends.end());
        
        int pStart = 0, pEnd = 0;
        int usedRooms = 0;
        while (pStart < intervals.size()) {
            if (starts[pStart] >= ends[pEnd]) {
                usedRooms--;
                pEnd++;
            }
            
            pStart++;
            usedRooms++;
        }
        
        return usedRooms;
    }
};
