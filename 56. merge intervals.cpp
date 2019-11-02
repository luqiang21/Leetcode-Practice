#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() <= 1) return intervals;
        vector<vector<int>> mergedIntervals;
        sort(intervals.begin(), intervals.end(), [](vector<int> interval1, vector<int> interval2){return interval1.at(0) < interval2.at(0);});
        mergedIntervals.push_back(intervals.at(0));
        
        for (int i = 1; i < intervals.size(); ++i) {
            vector<int> interval = intervals.at(i);
            if (interval.at(0) <= mergedIntervals.back().at(1)) {
                mergedIntervals.back().at(1) = max(mergedIntervals.back().at(1), interval.at(1));
            }
            else {
                mergedIntervals.push_back(interval);
            }
        }
        
        return mergedIntervals;
    }
};

int main() {
	vector<vector<int>> intervals = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
	vector<vector<int>> answers = {{1, 6}, {8, 10}, {15, 18}};
	assert(Solution().merge(intervals) == answers);
	cout << "Test passed." << endl;
}

