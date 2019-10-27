#include <iostream>
#include <queue>
#include <vector>
using namespace std;
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
	~ListNode()
	{
		delete next;
	}
};

class MyComparison {
    public:
    bool operator() (const ListNode* lhs, const ListNode* rhs)const {
        return lhs -> val > rhs -> val;
    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {

        priority_queue<ListNode*, vector<ListNode*>, MyComparison> minHeap;
        
        for (int i = 0; i < lists.size(); ++i) {
            if (lists[i]) minHeap.push(lists[i]);
        }
        
        if (minHeap.empty()) return NULL;
        ListNode* ans = minHeap.top();
        minHeap.pop();
        if (ans -> next) minHeap.push(ans -> next);
        ListNode* cur = ans;
        while (!minHeap.empty()) {
            ListNode* top = minHeap.top();
            minHeap.pop();
            
            cur -> next = top;
            cur = cur -> next;
            if (cur -> next != NULL) minHeap.push(cur -> next);
        }
        
        return ans;
    }
};

int main() {
//Input:
//[
//  1->4->5,
//  1->3->4,
//  2->6
//]
//Output: 1->1->2->3->4->4->5->6
	ListNode* a = new ListNode(1);
	a -> next = new ListNode(4);
	a -> next -> next = new ListNode(5);
	ListNode* b = new ListNode(1);
	ListNode* c = new ListNode(2);
	b -> next = new ListNode(3);
	b -> next -> next = new ListNode(4);
	c -> next = new ListNode(6);
	
	vector<ListNode*> lists = {a, b, c};
	ListNode* ans = Solution().mergeKLists(lists);
	while (ans) {
		cout << ans -> val << endl;
		ans = ans -> next;
	}

	delete a;
	return 0;
}


