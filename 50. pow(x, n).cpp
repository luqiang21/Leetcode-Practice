#include <iostream>
using namespace std;


class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0) return 0.0;
        if (n == 0) return 1;
        if (n == 1) return x;
        
        if (n < 0)
        {
            if (n + 1 == - ((1 << 31) - 1)) return 1 / x / myPow(x, -1 * (n + 1));
            return 1 / myPow(x, -1 * n);
        }
        if (n % 2 == 0) return myPow(x * x, n / 2);
        return x * myPow(x * x, n / 2);
    }
};

int main() {
	double x = 2.0;
	int n = -(1 << 31);
	assert(Solution().myPow(x, n) == 0.0);
	x = 1.0;
	assert(Solution().myPow(x, n) == 1.0);
	x = 2.0;
	n = 10;
	assert(Solution().myPow(x, n) == 1024.0);
	x = 2.0;
	n = -2;
	assert(Solution().myPow(x, n) == 0.25);
	cout << "Tests passed. " << endl;
	return 0;	
}
