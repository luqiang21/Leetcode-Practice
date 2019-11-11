#include <iostream>
#include <vector>

using namespace std;

class Knapsack {
public:

  int solveKnapsack(const vector<int>& values, const vector<int>& weights, int capacity) {
	if (values.size()== 0 || values.size() != weights.size() || capacity < 1) return 0; 		

	int n = values.size();
	vector<int> dp(capacity + 1);
	for (int c = 0; c < capacity + 1; ++c) {
		if (weights[0] <= c) dp[c] = values[0];
	}
	for (int i = 1; i < n; ++i) {
		for (int c = capacity; c >= 0; --c) {
			if (weights[i] <= c) dp[c] = max(dp[c], values[i] + dp[c - weights[i]]);
		}
	}

	return dp.back();
  }
};


int main() {
	vector<int> values = {1, 6, 10, 16}, weights = {1, 2, 3, 5};
    int	capacity = 7;
	cout << Knapsack().solveKnapsack(values, weights, capacity) << endl;
	assert(Knapsack().solveKnapsack(values, weights, capacity) == 22);
	return 0;
}
