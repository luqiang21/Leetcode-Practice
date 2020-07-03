class Solution {
public:
    vector<int> prisonAfterNDaysMine(vector<int>& cells, int N) {
        vector<string> unique;
        while (N > 0) {
            N--;
            
            vector<int> newCells(cells.size(), 0);
            string str = getString(cells);
            unique.push_back(str);
            for (int i = 1; i < cells.size() - 1; ++i) {
                if (cells[i-1] == cells[i+1]) newCells[i] = 1;
                else newCells[i] = 0;
            }
            
            auto it = find(unique.begin(), unique.end(), getString(newCells));
            if (it != unique.end()) {
                int loop = unique.end() - it;
                int idx = N%loop;
                return getVector(*(it + idx));
            }
        
            cells = newCells;
        }
        
        return cells;
    }
    
private:
    string getString(vector<int>& cells) {
        string res;
        for (auto& c : cells) {
            res += to_string(c);
        }
        return res;
    }
    
    vector<int> getVector(string& str) {
        vector<int> res;
        for (auto& ch : str) {
            res.push_back(ch - '0');
        }
        return res;
    }
    
public:
    vector<int> prisonAfterNDaysLeetCode(vector<int>& cells, int N) {
        unordered_map<int, int> seen;
        bool isFastForward = false;
        
        while (N > 0) {
            if (!isFastForward) {
                int bitMap = cellsToBitmap(cells);
                if (seen.find(bitMap) != seen.end()) {
                    N %= seen[bitMap] - N;
                    isFastForward = true;
                }
                else seen[bitMap] = N;
            }
            
            if (N > 0) {
                N -= 1;
                cells = nextDay(cells);
            }
        }
        
        return cells;
    }
    
    // bitMap
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        unordered_map<int, int> seen;
        bool isFastForward = false;
        
        int stateBitMap = 0x0;
        for (int& cell : cells) {
            stateBitMap <<= 1;
            stateBitMap |= cell;
        }
        
        while (N > 0) {
            if (!isFastForward) {
                if (seen.find(stateBitMap) != seen.end()) {
                    N %= seen[stateBitMap] - N;
                    isFastForward = true;
                }
                else seen[stateBitMap] = N;
            }
            
            if (N > 0) {
                N --;
                stateBitMap = nextDay(stateBitMap);
            }
        }
        
        vector<int> res(cells.size(), 0);
        for (int i = cells.size() - 1; i >= 0; --i) {
            res[i] = stateBitMap & 0x1;
            stateBitMap >>= 1;
        }
        
        return res;
    }
    
private:
    int nextDay(int bitMap) {
        bitMap = ~(bitMap << 1) ^ (bitMap >> 1);
        bitMap &= 0x7e;
        return bitMap;
    }
    vector<int> nextDay(vector<int>& cells) {
        vector<int> newCells(cells.size(), 0);
        for (int i = 1; i < cells.size() - 1; ++i) {
            newCells[i] = (cells[i-1] == cells[i+1]) ? 1 : 0;
        }
        
        return newCells;
    }
    
    int cellsToBitmap(vector<int>& cells) {
        int bitMap = 0;
        for (int& cell : cells) {
            bitMap <<= 1;
            bitMap |= cell;
        }
        
        return bitMap;
    }
};
