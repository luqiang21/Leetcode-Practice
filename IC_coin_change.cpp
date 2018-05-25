#include <iostream>
#include <vector>
#include <map>
using namespace std;

// recursive
int helper1(vector<int> denominations, int m, int amount) {
    // if n is 0, then 1 solution exists
    if(amount == 0) return 1;
    // if n is less than 0, no solution
    if(amount < 0) return 0;
    // if no coins and n is greater than 0, no solution
    if(m <= 0 and amount >= 1) return 0;

    // final answer is the sum of 1.including denominations[m-1], 2. excluding denominations[m-1]
    return helper1(denominations, m-1, amount) + helper1(denominations, m, amount - denominations[m-1]);
}

int dp1(int amount, vector<int> denominations) {
    return helper1(denominations, denominations.size(), amount);
}


// recursive with memory
typedef vector<int>::iterator vec_iter;
int helper2(int amount, vec_iter it_begin, vec_iter it_end ) {
    if(amount == 0) return 1;

    if(amount < 0) return 0;

    int num_ways = 0;
    map<int, bool> memo;
    vec_iter it;
    for(it = it_begin; it != it_end; ++it) {
        int coin = *it;
        if(memo.find(amount - coin) == memo.end() ) {
            num_ways += helper2(amount - coin, it, it_end);
            memo[amount - coin] = true;
        }
    }
    return num_ways;
}
int dp2(int amount, vector<int> denominations) {
    int num_ways = helper2(amount, denominations.begin(), denominations.end());

    return num_ways;
}

// dp method, 2D
int dp3(int amount, vector<int> denominations) {
    vector< vector<int> > memo(amount+1, vector<int>(denominations.size(), 0));

    // 1 way for 0 amount
    for(size_t i = 0; i < denominations.size(); ++i) {
        memo[0][i] = 1;
    }
    cout << "memo matrix is:" << endl;
    for(size_t i = 1; i < amount + 1; ++i) {
        int x, y;
        for(size_t j = 0; j < denominations.size(); ++j) {
            int coin = denominations[j];
            // include coin
            x = (i >= coin) ? memo[i-coin][j] : 0;
            // not include coin
            y = (j >= 1) ? memo[i][j-1] : 0;
            memo[i][j] = x + y;
            cout << memo[i][j] << "  ";
        }
       cout << endl;
        }

    return memo[amount][denominations.size()-1];
}

// dp method, 1D
int dp4(int amount, vector<int> denominations) {
    vector<int> memo(amount + 1, 0);
    memo[0] = 1; // 1 way for 0 amount
    for(size_t i = 0; i < denominations.size(); ++i) {
        int coin = denominations[i];
        for(size_t j = coin; j < amount + 1; ++j) {
            memo[j] += memo[j-coin];
            cout << j << "  " << coin <<"-" << (j-coin) <<"   " << memo[j-coin] << "   " <<  memo[j] << endl;
        }
    }

    return memo[amount];
}

int main() {
    int amount = 4;
    vector<int> denominations = {1, 2, 3};
    int n = dp1(amount, denominations);
    cout << "Recursive Way:\n   number of ways is " << n << endl;
    n = dp2(amount, denominations);
    cout << "Recursive Way with Memory:\n   number of ways is " << n << endl << endl;
    n = dp3(amount, denominations);
    cout << "Dynamic Programming:\n   number of ways is " << n << endl << endl;
    n = dp4(amount, denominations);
    cout << "Dynamic Programming:\n   number of ways is " << n << endl;


  std::cout << "Hello World!\n" << endl;
}
