/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElementsMine(ListNode* head, int val) {
        ListNode *dummy = new ListNode(0, head), *cur = head, *pre = dummy;
        while (cur) {
            if (cur -> val == val) {
                pre -> next = cur -> next;
                cur = cur -> next;
                continue;
            }
            pre = cur;
            cur = cur -> next;
        }
        
        return dummy -> next;
    }
    
    ListNode* removeElementsWithoutDummy(ListNode* head, int val) {
        while (head != NULL && head -> val == val) head = head -> next;
        
        ListNode* cur = head;
        while (cur != NULL && cur -> next != NULL) {
            if (cur -> next -> val == val) cur -> next = cur -> next -> next;
            else cur = cur -> next;
        }
        
        return head;
    }
    
    ListNode* removeElements(ListNode* head, int val) {
        if (head == NULL) return NULL;
        head -> next = removeElements(head -> next, val);
        return head -> val == val ? head -> next : head;
    }
};
