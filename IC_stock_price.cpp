#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int get_max_profit1(const vector<int>& stock_prices) {
    if(stock_prices.size() <= 1) {
        throw invalid_argument("Getting a profit requires at least 2 prices.");
    }

    int max_profit = numeric_limits<int>::min();
    int min_so_far = stock_prices[0];
    int profit;

    for(size_t i=1; i < stock_prices.size(); ++i) {
        profit = stock_prices[i] - min_so_far;
        min_so_far = min(min_so_far, stock_prices[i]);
        max_profit = max(profit, max_profit);
    }

    return max_profit;
}

int get_max_profit(const vector<int>& stock_prices) {
    // compute difference
    vector<int> differences;
    int difference;
    for(size_t i=1; i < stock_prices.size(); ++i) {
        difference = stock_prices[i] - stock_prices[i-1];
        differences.push_back(difference);
    }

    int max_ending_here = differences[0];
    int res = numeric_limits<int>::min();

    for(size_t i = 1; i < differences.size(); ++ i) {
        max_ending_here = max(max_ending_here, max_ending_here + differences[i]);
        max_ending_here = max(max_ending_here, differences[i]);

        res = max(max_ending_here, res);
    }
    return res;
}

int main() {
    vector<int> stock_prices = {10, 7, 5, 8, 11, 9};
    // stock_prices = {1, 2};

    cout << get_max_profit1(stock_prices) << endl
    << get_max_profit(stock_prices) << endl;
    return 0;
}
