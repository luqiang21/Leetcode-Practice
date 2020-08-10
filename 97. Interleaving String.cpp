class Solution {
public:
    // brute force, 2^(m+n)
    bool isInterleave1(string s1, string s2, string s3) {
        return isInterleave(s1, 0, s2, 0, "", s3);
    }
    
private:
    bool isInterleave(string s1, int i, string s2, int j, string res, string& s3) {
        if (res == s3 && i == s1.length() && j == s2.length()) return true;
        if (i + j > 0 && res[i + j - 1] != s3[i + j - 1]) return false;
        
        bool ans = false;
        if (i < s1.length()) {
            ans |= isInterleave(s1, i+1, s2, j, res + s1[i], s3);
        }
        
        if (j < s2.length()) {
            ans |= isInterleave(s1, i, s2, j+1, res + s2[j], s3);
        }
        
        return ans;
    }
    
public:
    // recursion with memoization
    bool isInterleave2(string s1, string s2, string s3) {
        vector<vector<int>> memo(s1.length(), vector<int>(s2.length(), -1));
        return isInterleave(s1, 0, s2, 0, s3, 0, memo);
    }
    
private:
    bool isInterleave(string& s1, int i, string& s2, int j, string& s3, int k, vector<vector<int>>& memo) {
        if (i == s1.length()) return s2.substr(j) == s3.substr(k);
        
        if (j == s2.length()) return s1.substr(i) == s3.substr(k);
        
        if (memo[i][j] >= 0) return memo[i][j] == 1 ? true : false;
        
        bool ans = false;
        if ((s3[k] == s1[i] && isInterleave(s1, i+1, s2, j, s3, k+1, memo))
           || (s3[k] == s2[j] && isInterleave(s1, i, s2, j+1, s3, k+1, memo))) ans = true;
        
        memo[i][j] = ans ? 1 : 0;
        return ans;
    }
    
public:
    // 2d dp
    bool isInterleave3(string s1, string s2, string s3) {
        if (s3.length() != s1.length() + s2.length()) return false;
        
        vector<vector<bool>> dp(s1.length() + 1, vector<bool>(s2.length() + 1, false));
        for (int i = 0; i <= s1.length(); ++i) {
            for (int j = 0; j <= s2.length(); ++j) {
                if (i == 0 && j == 0) dp[i][j] = true;
                else if (i == 0) dp[i][j] = dp[i][j-1] && s2[j-1] == s3[i+j-1];
                else if (j == 0) dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1];
                else {
                    dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1])
                            || (dp[i][j-1] && s2[j-1] == s3[i+j-1]);
                }
            }
        }
        return dp[s1.length()][s2.length()];
    }
    
 // 1d dp
    bool isInterleave4(string s1, string s2, string s3) {
        if (s3.length() != s1.length() + s2.length()) return false;
        
        vector<bool> dp(s2.length() + 1, false), dp2 = dp;
        for (int i = 0; i <= s1.length(); ++i) {
            
            for (int j = 0; j <= s2.length(); ++j) {
                if (i == 0 && j == 0) dp2[j] = true;
                else if (i == 0) dp2[j] = dp2[j-1] && s2[j-1] == s3[i+j-1];
                else if (j == 0) dp2[j] = dp[j] && s1[i-1] == s3[i+j-1];
                else {
                    dp2[j] = (dp[j] && s1[i-1] == s3[i+j-1])
                            || (dp2[j-1] && s2[j-1] == s3[i+j-1]);
                }
            }
            dp = dp2;
        }
        return dp[s2.length()];
    }
    
     // 1d dp
    bool isInterleave(string s1, string s2, string s3) {
        if (s3.length() != s1.length() + s2.length()) return false;
        
        vector<bool> dp(s2.length() + 1, false);
        for (int i = 0; i <= s1.length(); ++i) {
            
            for (int j = 0; j <= s2.length(); ++j) {
                if (i == 0 && j == 0) dp[j] = true;
                else if (i == 0) dp[j] = dp[j-1] && s2[j-1] == s3[i+j-1];
                else if (j == 0) dp[j] = dp[j] && s1[i-1] == s3[i+j-1];
                else {
                    dp[j] = (dp[j] && s1[i-1] == s3[i+j-1])
                            || (dp[j-1] && s2[j-1] == s3[i+j-1]);
                }
            }
        }
        return dp[s2.length()];
    }
};
