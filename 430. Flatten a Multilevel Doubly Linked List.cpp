/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flattenRecNeat(Node* head, Node* rest=nullptr) {
        if (!head) return rest;
        
        head -> next = flattenRecNeat(head -> child, flattenRecNeat(head -> next, rest));
        if (head -> next) head -> next -> prev = head;
        head -> child = nullptr;
        
        return head;
    }
    
    Node* flattenRec(Node* head) {
        if (!head) return head;
        helper(head);
        return head;
    }
    
    Node* flatten(Node* head) {
        if (head == NULL) return head;
        
        stack<Node*> sta;
        sta.push(head);
        Node* prev = new Node(0);
        
        while (sta.size()) {
            auto root = sta.top();
            sta.pop();
            
            root -> prev = prev;
            prev -> next = root;
            
            prev = root;
            
            if (root -> next) {
                sta.push(root -> next);
            }
            
            if (root -> child) {
                sta.push(root -> child);
                root -> child = NULL;
            }
        }
        
        head -> prev = NULL;
        return head;
    }

private:
    Node* helper(Node* head) {
        
    // Five situations:
    // 1. null - no need to flatten, just return it
    // 2. no child, no next - no need to flatten, it is the last element, just return it
    // 3. no child, next - no need to flatten, go next
    // 4. child, no next - flatten the child and done
    // 5. child, next - flatten the child, connect it with the next, go next
        if (head == NULL) return head;
        
        if (head -> child == NULL) {
            if (head -> next == NULL) {
                return head;
            }
            return helper(head -> next);
        }
        
        else {
            auto next = head -> next;
            auto child = head -> child;
            head -> child = NULL;
            auto childTail = helper(child);
            head -> next = child;
            child -> prev = head;
            
            if (next != NULL) {
                childTail -> next = next;
                next -> prev = childTail;
                return helper(next);
            }
            
            return childTail;
        }
    }    
};
