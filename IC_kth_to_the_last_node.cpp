#include <iostream>
using namespace std;

/**
Write a function kthToLastNode() that takes an integer kk and the headNode of
a singly-linked list, and returns the kkth to last node in the list.
*/
struct LinkedListNode {
  int value_;
  struct LinkedListNode* next_;
  LinkedListNode(int value): value_(value), next_(nullptr) {}
};

LinkedListNode* kthToLastNode(size_t k, LinkedListNode* head) {
    if(k < 1) throw invalid_argument("Impossible to find!");

    LinkedListNode* leftNode = head;
    LinkedListNode* rightNode = head;

    // move right to the kth node
    for(size_t i = 0; i < k - 1; ++i) {
        if(!rightNode -> next_) throw invalid_argument("k is larger than the length of the list");

        rightNode = rightNode -> next_;
    }

    // move both nodes, until rightNode hits the end of the list
    while(rightNode -> next_) {
        leftNode = leftNode -> next_;
        rightNode = rightNode -> next_;
    }

    return leftNode;
}

int main() {
  LinkedListNode* a = new LinkedListNode(1);
  LinkedListNode* b = new LinkedListNode(2);
  LinkedListNode* c = new LinkedListNode(3);
  LinkedListNode* d = new LinkedListNode(4);
  LinkedListNode* e = new LinkedListNode(5);

  a->next_ = b;
  b->next_ = c;
  c->next_ = d;
  d->next_ = e;

  LinkedListNode* ans = kthToLastNode(2, a);
  cout << ans -> value_ << endl;

  delete a;
  delete b;
  delete c;
  delete d;
  delete e;
  return 0;
}
