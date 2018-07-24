#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isEditDistanceOne(string s1, string s2) {
        int m = s1.length(), n = s2.length();

        // if length difference is greater than 1
        if (abs(m - n) > 1) {
            return false;
        }

        int count = 0; // count of edits

        int i = 0, j = 0;
        while (i < m && j < n) {
            if (s1[i] != s2[j]) {
                if (count == 1) {
                    return false;
                }

                if (m > n) {
                    i ++;
                }
                else if (m < n) {
                    j ++;
                }
                else {
                    i ++;
                    j ++;
                }
                count ++;
            }
            else {
                i ++;
                j ++;
            }
        }

        if (i < m || j < n) {
            count ++;
        }

        return count == 1;
    }

};

int main() {
    string s1 = "abc";
    string s2 = "adc";
    Solution sol;
    sol.isEditDistanceOne(s1, s2) ? cout << "Yes" : cout << "No";
    cout << endl;
    s2 = "abc";
    sol.isEditDistanceOne(s1, s2) ? cout << "Yes" : cout << "No";
    cout << endl;

    return 0;
}
