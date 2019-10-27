#include <iostream>
#include <ctype.h>

using namespace std;

class SolutionMy {
public:
    bool isPalindrome(string s) {
        string onlyLetters;
        for (char c : s) {
            if (isalnum(c)) {
                onlyLetters.push_back(tolower(c));
            }
        }    
        
        int n = onlyLetters.size();
        for (int i = 0; i < n / 2; ++i) {
            if (onlyLetters[i] != onlyLetters[n-i-1]) return false;
        }
        
        return true;
    }
};

class Solution {
public:
    bool isPalindrome(string s) {
       int l = 0, r = s.size() - 1;
        
        while (l < r) {
            if (!isalnum(s.at(l))) ++l;
            else if (!isalnum(s.at(r))) --r;
            else {
                if (tolower(s.at(l++)) != tolower(s.at(r--))) return false;
            }
        }
        
        return true;
    }
};

int main() {
	string test1 = "A man, a plan, a canal: Panama";
	string test2 = "1P";
	cout << boolalpha << SolutionMy().isPalindrome(test1) << "  " << Solution().isPalindrome(test1) << endl;
	cout << boolalpha << SolutionMy().isPalindrome(test2) << "  " << Solution().isPalindrome(test2) << endl;

	return 0;
}

