/**
Implement a queue ↴ with 2 stacks. ↴ Your queue should have an enqueue and a
dequeue method and it should be "first in first out" (FIFO).
*/

/*def my_function(arg):
    # write the body of your function here
    return 'running with %s' % arg

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function('test input')

class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            # move items from in_stack to out_stack, reverse order
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue")


        return self.out_stack.pop()

*/
#include <iostream>
#include <stack>

// C++11 lest unit testing framework
#include "lest.hpp"

using namespace std;

// fill in the definitions for enqueue() and dequeue()


class QueueTwoStacks
{
private:
    stack<int> inStack_;
    stack<int> outStack_;

public:
    void enqueue(int item)
    {
        inStack_.push(item);
    }

    int dequeue()
    {
        if(outStack_.empty()) {
            while(!inStack_.empty()) {
                outStack_.push(inStack_.top());
                inStack_.pop();
            }

            if(outStack_.empty()) {
                throw runtime_error("can't dequeue from empty queue!");
            }
        }
        int top = outStack_.top();
        outStack_.pop();
        return top;
    }
};







// tests

const lest::test tests[] = {
    CASE("QueueTwoStacks test") {
        QueueTwoStacks q;
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        EXPECT(q.dequeue() == 1);
        EXPECT(q.dequeue() == 2);
        q.enqueue(4);
        EXPECT(q.dequeue() == 3);
        EXPECT(q.dequeue() == 4);
        EXPECT_THROWS(q.dequeue());
    }
};

int main(int argc, char** argv)
{
    return lest::run(tests, argc, argv);
}
