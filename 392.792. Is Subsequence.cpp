#include <unordered_map>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while (i < s.size() && j < t.size()) {
            if (s[i] == t[j]) ++i;
            ++j;
        }
        
        return i == s.size();
    }
};

class SolutionBinary {
public:
	bool isSubsequence(string s, string t) {
		auto map = preProcess(t);
		int j = 0;
		for (int i = 0; i < s.size(); ++i) {
			char c = s[i];
			if (map[c].size() == 0) return false; // no char exist
			int pos = leftBound(map[c], j);
			if (pos == map[c].size()) return false; // no char exist after j
			j = map[c][pos] + 1;
		}	
		return true;
	}
	int numMatchingSubseq(string S, vector<string>& words) {
        int res = 0;
        for (auto word : words) {
            if (isSubsequence(word, S)) ++res;
        }
        return res;
    }
private:
	// look for left bound using binary search
	int leftBound(vector<int> arr, int target) {
		int low = 0, high = arr.size();
		while (low < high) {
			int mid = (low + high) / 2;
			if (arr[mid] < target) low = mid + 1;
			else high = mid;
		}	
		return low;
	}

	vector<vector<int>> preProcess(string t) {
		vector<vector<int>> map(256, vector<int>());
		if (t.empty()) return map;

		for (int i = 0; i < t.size(); ++i) {
			map[t[i]].push_back(i);
		}
		return map;
	}
};
int main() {
	string s = "abc", t = "ahbgdc";
	assert(Solution().isSubsequence(s, t) == true);
	assert(SolutionBinary().isSubsequence(s, t) == true);
	
	s = "axc", t = "ahbgdc";
	assert(Solution().isSubsequence(s, t) == false);
	assert(SolutionBinary().isSubsequence(s, t) == false);

	string S = "abcde";
	vector<string> words = {"a", "bb", "acd", "ace"};
	assert(SolutionBinary().numMatchingSubseq(S, words) == 3);
	cout << "Tests passed!" << endl;
	return 0;	

}
