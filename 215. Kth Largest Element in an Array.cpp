#include <iostream>
#include <vector>
#include <queue>
#include <assert.h>

using namespace std;

class Solution {
public:
    /**
    * @brief find the kth largest number in an array
    * @param nums the array of integers
    * @param k given k
    * @return the kth largest number
    */
    int findKthLargest2(vector<int>& nums, int k) {
        priority_queue<int> pq(nums.begin(), nums.end());
        for (int i = 1; i < k; ++i ){
            pq.pop();
        }

        return pq.top();
    }

private:
    int heap_size;

public:
    // implement heapsort
    inline int left(int idx) {return (idx << 1) + 1;}
    inline int right(int idx) {return (idx << 1) + 2;}
    inline int parent(int idx) {return (idx - 1) / 2;}

    void max_heapify(vector<int>& nums, int idx) {
        int largest = idx;
        int l = left(idx), r = right(idx);
        if(l < heap_size && nums[l] > nums[largest]) largest = l;
        if(r < heap_size && nums[r] > nums[largest]) largest = r;

        if(largest != idx) {
            swap(nums[idx], nums[largest]);
            max_heapify(nums, largest);
        }

    }

    void build_max_heap(vector<int>& nums) {
        heap_size = nums.size();

        for(int i = (heap_size >> 1) - 1; i >= 0; i --) {
            max_heapify(nums, i);
        }
    }

    int findKthLargestHeapSort(vector<int>& nums, int k) {
        build_max_heap(nums);

        for(int i = 0; i < k; i++) {
            swap(nums[0], nums[heap_size - 1]);
            heap_size --;
            max_heapify(nums, 0);
        }
        return nums[heap_size];
    }
	int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int> > min_heap;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (min_heap.size() < k) {
                min_heap.push(nums[i]);
            }
            else {
                if (nums[i] > min_heap.top()) {
                    min_heap.pop();
                    min_heap.push(nums[i]);
                }
            }
        }
        
        return min_heap.top();
    }
};

int main() {
    Solution sol;
    vector<int> nums{3,2,3,1,2,4,5,5,6};
    int k = 4;

    assert(sol.findKthLargest2(nums, k) == 4);
    assert(sol.findKthLargestHeapSort(nums, k) == 4);
    assert(sol.findKthLargest(nums, k) == 4);

    cout << "tests passed!" << endl;
}
