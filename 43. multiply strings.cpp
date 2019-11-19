#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        int n = num1.length(), m = num2.length();
        vector<int> res(n + m, 0);
        
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                // compute positions
                int p1 = i + j, p2 = i + j + 1;
                int sum = mul + res[p2]; // add to value at p2
                res[p1] += sum / 10;
                res[p2] = sum % 10;
            }
        }
        
        // prefix 0
        int i = 0;
        while (i < res.size() && res[i] == 0) ++i;
        
        string str;
        for (; i < res.size(); ++i) str.push_back(res[i] + '0');
        
        return str.size() == 0 ? "0" : str;
    }
};

int main() {
	cout << Solution().multiply("123", "456") << endl;
	return 0;

}
