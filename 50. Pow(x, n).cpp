class Solution {
public:
    // stackOverflow ....
    double myPowFailed(double x, int n) {
        if (n == 0) return 1;
        if (n == 1) return x;
        if (n < 0) return 1 / myPow(x, -n);
        return x * myPow(x, n-1);
    }
    
    double myPowRec(double x, int n) {
        if (n == 0 || x == 1) return 1;
        if (n == 1) return x;
        if (n < 0) return 1 / myPow(x, -(n+1)) / x;
        double half = myPow(x, n/2);
        if (n%2 == 0) return half * half;
        return half * half * x;
    }
    
    double myPow(double x, int n) {
        long l = n;
        if (l < 0) l = -l;
        
        double res = 1;
        double cur = x;
        while (l > 0) {
            if ((l & 1) == 1) res *= cur;
            cur *= cur;
            l >>= 1;
        }
        
        return n < 0 ? 1 / res : res;
    }
};
