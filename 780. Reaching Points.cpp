/**
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].

*/
#include <iostream>
using namespace std;

class Solution {

public:
    bool reachingPoints(int sx, int sy, int tx, int ty) {
        while (sx < tx && sy < ty) {
            if (tx > ty) tx %= ty;
            else ty %= tx;
        }

        if (sx == tx) return (ty - sy) % sx == 0;
        if (sy == ty) return (tx - sx) % sy == 0;

        return false;
    }


};

int main() {
    int sx = 1, sy = 1, tx = 3, ty = 5;
    Solution sol;
    sol.reachingPoints(sx, sy, tx, ty) ? cout << "Yes" : cout << "No";
    cout << endl;

    return 0;
}
