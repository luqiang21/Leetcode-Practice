// Given two strings s and t , write a function to determine if t is an anagram of s.
// 
// Example 1:
// 
// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:
// 
// Input: s = "rat", t = "car"
// Output: false
// Note:
// You may assume the string contains only lowercase alphabets.
// 
// Follow up:
// What if the inputs contain unicode characters? How would you adapt your solution to such case?
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution1 {
public:
    unordered_map<char, int> getMap(string s) {
        unordered_map<char, int> map;
        for (auto& c : s) {
            if (map.find(c) == map.end()) map[c] = 1;
            else map[c] += 1;
        }
        return map;
    }

    bool isAnagram(string s, string t) {
        unordered_map<char, int> map1, map2;
        map1 = getMap(s);
        map2 = getMap(t);
        for (auto& pair : map1) {
            char key = pair.first;
            int value = pair.second;
            if (map2.find(key) == map2.end() || map2[key] != value) {
                return false;
            }
        }

        for (auto& pair : map2) {
            char key = pair.first;
            int value = pair.second;
            if (map1.find(key) == map1.end() || map1[key] != value) {
                return false;
            }
        }

        return true;
    }
};
class Solution {
public:
    struct defaultValue {
        int value = 0;
    };
    unordered_map<char, defaultValue> getMap(string s) {
        unordered_map<char, defaultValue> map;
        for (auto& c : s) {
            map[c].value += 1;
        }
        return map;
    }
    
    bool isAnagram(string s, string t) {
        unordered_map<char, defaultValue> map1, map2;
        map1 = getMap(s);
        map2 = getMap(t);
        for (auto& pair : map1) {
            char key = pair.first;
            defaultValue value = pair.second;
            if (map2.find(key) == map2.end() || map2[key].value != value.value) {
                return false;
            }
        }
        
        for (auto& pair : map2) {
            char key = pair.first;
            defaultValue value = pair.second;
            if (map1.find(key) == map1.end() || map1[key].value != value.value) {
                return false;
            }
        }
        
        return true;
    }
};
class Solution2 {
public:

    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> map1;
        for (auto & c : s) {
            map1[c] ++;
        }
        
        for (auto & c : t) {
            map1[c] --;
        }
        
        for (auto & element : map1)
        {
            if (element.second != 0) return false;
        }
        
        return true;
    }   
};
int main() {
	Solution sol;
	Solution1 sol1;
	Solution1 sol2;
	string s = "anagram", t = "nagaram";
	cout << boolalpha << sol.isAnagram(s, t) << endl;
	cout << boolalpha << sol1.isAnagram(s, t) << endl;
	cout << boolalpha << sol2.isAnagram(s, t) << endl;
}

