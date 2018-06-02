#include <iostream>
#include <stack>

// C++11 lest unit testing framework
#include "lest.hpp"

using namespace std;

// fill in the definitions for push(), pop(), and getMax()


class MaxStack
{
    stack<int> stack_;
    stack<int> maxes_;

public:
    void push(int item)
    {   // deal with empty and duplicates
        if(maxes_.empty() || item >= maxes_.top()) {

            maxes_.push(item);
        }
        stack_.push(item);
    }

    int pop()
    {
        int top = stack_.top();
        stack_.pop();
        int top_max = maxes_.top();
        if(top_max == top) {
            maxes_.pop();
        }
        return top;
    }

    int getMax() const
    {
        return maxes_.top();
    }
};




// tests

const lest::test tests[] = {
    CASE("MaxStack test") {
        MaxStack s;
        s.push(5);
        EXPECT(s.getMax() == 5);
        s.push(4);
        s.push(7);
        s.push(7);
        s.push(8);
        EXPECT(s.getMax() == 8);
        EXPECT(s.pop() == 8);
        EXPECT(s.getMax() == 7);
        EXPECT(s.pop() == 7);
        EXPECT(s.getMax() == 7);
        EXPECT(s.pop() == 7);
        EXPECT(s.getMax() == 5);
        EXPECT(s.pop() == 4);
        EXPECT(s.getMax() == 5);
    }

};

int main(int argc, char** argv)
{
    return lest::run(tests, argc, argv);
}
