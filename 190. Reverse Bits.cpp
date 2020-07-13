class Solution {
public:
    // Bit by bit
    uint32_t reverseBitsMine(uint32_t n) {
        uint32_t res = 0;
        if (n == 0) return res;
        
        int i = 0;
        while (n > 0) {
            i++;
            res <<= 1;
            res += n & 1;
            n >>= 1;
        }
        
        res <<= 32 - i;
        return res;
    }
    
    // Byte by Byte with Memoization
    uint32_t reverseBitsByte(uint32_t n) {
        int res = 0, power = 24;
        while (n > 0) {
            int byte = n & 0xff;
            res += reverseByte(byte) << power;
            n >>= 8;
            power -= 8;
        }
        
        return res;
    }
    
    // Mask and shift, Divide and conquer
    uint32_t reverseBits(uint32_t n) {
        // n = ((n & 0xffff0000) >> 16 | (n & 0x0000ffff) << 16); OR
        n = (n >> 16 | n << 16);
        n = ((n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8);
        n = ((n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4);
        n = ((n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2);
        n = ((n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1);
        
        return n;
    }
private:
    unordered_map<uint32_t, uint32_t> memo;
    uint32_t reverseByte(uint32_t byte) {
        if (memo.count(byte)) return memo[byte];
        uint32_t rev = (byte * 0x0202020202 & 0x010884422010) % 1023;
        memo.emplace(byte, rev);
        return rev;
    }
};
