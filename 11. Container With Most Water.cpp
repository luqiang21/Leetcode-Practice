/*
Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

*/

#include <iostream>
#include <vector>
#include <assert.h>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        if(height.size() <= 1) return 0;

        int left = 0, right = height.size() - 1;
        int max_water = 0;

        while(left < right) {
            int current = (right - left) * min(height[left], height[right]);
            if(current > max_water) max_water = current;

            if(height[left] < height[right])
                ++left;
            else
                --right;

        }
        return max_water;
    }

};

int main() {
  Solution sol;
  vector<int> height {1, 8, 2, 5, 3, 4, 8, 5, 7};
  cout << sol.maxArea(height) << endl;
  assert(sol.maxArea(height) == 49);
  return 0;
}
