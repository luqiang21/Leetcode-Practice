/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // iterative way
    ListNode* reverseList1(ListNode* head) {
        if(!head) return head;

        ListNode *prev = NULL, *current=NULL, *tmp=NULL;
        current = head;
        while(current != NULL) {
            tmp = current -> next;
            current -> next = prev;
            prev = current;
            current = tmp;
        }
        return prev;
    }


    // recursive way
    ListNode* helper(ListNode* cur, ListNode* prev) {
        if(!cur){
            return prev;
        }

        ListNode* rearHead = helper(cur->next, cur);
        cur -> next = prev;
        return rearHead;
    }
    ListNode* reverseList(ListNode* head) {
        if(!head) return head;
        return helper(head, NULL);
    }

};
