#include <iostream>
#include <vector>
using namespace std;


class SolutionNL {
public:
    int numMusicPlaylists(int N, int L, int K) {
        vector<vector<long>> dp(L + 1, vector<long>(N + 1, 0));
        // dp[i][j], i songs, j songs are different.
        int M = 1e9 + 7;
        dp[0][0] = 1;
        for (int i = 1; i <= L; ++i) {
            for ( int j = 1; j <= N; ++j) {
                dp[i][j] = dp[i-1][j-1] * (N - (j - 1)) % M;
                if (j > K) dp[i][j] += dp[i-1][j] * (j - K) % M;
                dp[i][j] %= M;
            }
        }
        
        return dp[L][N];
    }
};
class SolutionN {
public:
    int numMusicPlaylists(int N, int L, int K) {
        vector<long> dp1(N + 1, 0);
        vector<long> dp2(N + 1, 0);
        // dp[i][j], i songs, j songs are different.
        int M = 1e9 + 7;
        dp1[0] = 1;
        for (int i = 1; i <= L; ++i) {
            for ( int j = 1; j <= N; ++j) {
                dp2[j] = dp1[j-1] * (N - (j - 1)) % M;
                if (j > K) dp2[j] += dp1[j] * (j - K) % M;
                dp2[j] %= M;
            }
			dp1 = dp2;
        }
        
        return dp2[N];
    }
};


int main() {

	assert(SolutionNL().numMusicPlaylists(16, 16, 4) == 789741546);
	assert(SolutionN().numMusicPlaylists(16, 16, 4) == 789741546);
	cout << "Test passed" << endl;
	return 0;
}
