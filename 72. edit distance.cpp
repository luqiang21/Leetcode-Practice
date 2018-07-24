#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
    int min(int x, int y, int z) {
        return std::min(std::min(x, y), z);
    }
    int edit_distance(string s1, string s2, int m, int n) {
        // if first string is empty, only option is insert all chars in s2.
        if (m == 0) return n;
        // if second string is empty, only option is remove all chars in s1.
        if (n == 0) return m;

        // if the last chars are equal, ignore them, remove the distance for
        // remaining strings
        if (s1[m-1] == s2[n-1]) {
            return edit_distance(s1, s2, m - 1, n - 1);
        }
        // If last characters are not same, consider all three
        // operations on last character of first string, recursively
        // compute minimum cost for all three operations and take
        // minimum of three values.
        return 1 + min(edit_distance(s1, s2, m, n - 1), // insert, so s1[m+1] == s2[n]
                       edit_distance(s1, s2, m - 1, n), // remove
                       edit_distance(s1, s2, m - 1, n - 1) // replace
                        );
    }
public:
    // return the minimum number of operations to convert s1 to s2
    int edit_distance(string s1, string s2) {
        return edit_distance(s1, s2, s1.length(), s2.length());
    }

    int edit_distance_dp(string s1, string s2) {
        int m = s1.length(), n = s2.length();
        vector< vector<int> > dp(m+1, vector<int>(n+1, 0));

        for (int i = 0; i < m + 1; ++i) {
            for (int j = 0; j < n + 1; ++j) {
                if (i == 0) {
                    // if no chars in s1, insert all chars of s2
                    dp[i][j] = j;
                }
                else if (j == 0) {
                    // if no chars in s2, remove all chars in s1
                    dp[i][j] = i;
                }
                else if (s1[i-1] == s2[j-1]) {
                    // if last chars are same, ignore them and recur for remaining
                    dp[i][j] = dp[i-1][j-1];
                }
                else {
                    // if not same, consider all possibilities and find min
                    dp[i][j] = 1 + min(dp[i][j-1], // insert
                                       dp[i-1][j], // remove
                                       dp[i-1][j-1] // replace
                                   );
                }
            }
        }

        return dp[m][n];
    }
};

int main() {
    string str1 = "sunday";
    string str2 = "saturday";

    Solution sol;
    cout << "The edit distance between " << str1 << " and " << str2 << " is " <<
    sol.edit_distance( str1 , str2) << endl;

    cout << "The edit distance between " << str1 << " and " << str2 << " is " <<
    sol.edit_distance_dp( str1 , str2) << endl;
    return 0;
}
