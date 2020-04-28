#include <iostream>
#include <vector>
#include <list>
#include <unorderd_map>

class FirstUnique {
public:
    FirstUnique(vector<int>& nums) {
        for (auto n : nums) {
            add(n);
        }
    }
    
    int showFirstUnique() {
        if (q.empty()) {
            return -1;
        }
        else {
            return q.front();
        }
    }
    
    void add(int value) {
        if (map.find(value) == map.end()) {
            q.push_back(value);
            auto it = q.end();
            --it;
            map[value] = it;
        }
        else {
            auto it = map[value];
            if (it != q.end()) {
                q.erase(map[value]);
                map[value] = q.end();
            }
        }
    }
private:
    list<int> q;
    unordered_map<int, list<int>::iterator> map;
};

/**
 * Your FirstUnique object will be instantiated and called as such:
 * FirstUnique* obj = new FirstUnique(nums);
 * int param_1 = obj->showFirstUnique();
 * obj->add(value);
 */
