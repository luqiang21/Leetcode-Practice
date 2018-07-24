#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int min(int x, int y, int z) {
    return min(min(x, y), z);
}
class Solution {
public:


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
};

int main() {
    string str1 = "sunday";
    string str2 = "saturday";

    Solution sol;
    cout << sol.edit_distance( str1 , str2) << endl;
    return 0;
}
