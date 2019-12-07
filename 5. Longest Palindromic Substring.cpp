#include <iostream>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return s;
        string res;
        for (int i = 0; i < s.size(); ++ i) {
            // centered by s[i]
            string s1 = longestPalindrome(s, i, i);
            // centered by s[i], s[i+1]
            string s2 = longestPalindrome(s, i, i+1);
            
            res = res.size() > s1.size() ? res : s1;
            res = res.size() > s2.size() ? res : s2;
        }
        
        return res;
    }
    
private:
    string longestPalindrome(string s, int l, int r) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            --l;
            ++r;
        }
        
        return s.substr(l + 1, r - l - 1);
    }
};

int main() {
	string s1 = "babad", ans1 = "aba";
	string s2 = "cbbd", ans2 = "bb";
	cout << s1 << "  " << Solution().longestPalindrome(s1) << endl;
	assert(Solution().longestPalindrome(s1) == ans1);
	
	cout << s2 << "  " << Solution().longestPalindrome(s2) << endl;
	assert(Solution().longestPalindrome(s2) == ans2);
	cout << "Tests passed!" << endl;
	return 0;
}
