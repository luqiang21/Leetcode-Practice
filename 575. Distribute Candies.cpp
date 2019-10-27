#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <vector>

using namespace std;

class SolutionMap {
public:
    int distributeCandies(vector<int>& candies) {
        unordered_map<int, int> map;
        for (int candy : candies) {
            if (map.find(candy) != map.end()) map[candy]++;
            else map[candy] = 1;
        }
        
        int candyCount = 0;
        for (pair<int, int> kv : map) {
            ++candyCount;
        }
        return min(candyCount, (int)candies.size() / 2);
    }
};

class SolutionSet {
public:
    int distributeCandies(vector<int>& candies) {
        return min(unordered_set<int>(candies.begin(), candies.end()).size(), candies.size() / 2);
    }
};


class SolutionBitSet {
public:
    int distributeCandies(vector<int>& candies) {
        bitset<200001> h; // [-100,000, 100,000].
        for (int candy : candies) {
            h.set(candy + 100000);
        }
        return min(h.count(), candies.size() / 2);
    }
};

int main() {
	vector<int> candies = {1,1,2,2,3,3};
	vector<int> candies2 = {1,1,2,3};

	assert(SolutionMap().distributeCandies(candies) == 3);
	assert(SolutionMap().distributeCandies(candies2) == 2);
	assert(SolutionSet().distributeCandies(candies) == 3);
	assert(SolutionSet().distributeCandies(candies2) == 2);
	assert(SolutionBitSet().distributeCandies(candies) == 3);
	assert(SolutionBitSet().distributeCandies(candies2) == 2);
	cout << "Test passed" << endl;
}
