/**
Write an efficient function that tells us whether or not an input string's
openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return true
"{ [ ( ] ) }" should return false
"{ [ }" should return false

*/

#include <iostream>
#include <stack>
#include <unordered_map>
#include "lest.hpp"
using namespace std;

bool bracketValidator(const string& sent) {
    stack<char> brackets;
    unordered_map<char, char> pairs {{')', '('},
                                     {'}', '{'},
                                     {']', '['}};


    for(size_t i = 0; i < sent.length(); ++i) {
        char c = sent[i];
        if(c == '(' || c == '{' || c == '[') {
            brackets.push(c);
        }
        else if(c == ')' || c == '}' || c == ']') {
            if(brackets.top() == pairs[c]) brackets.pop();
            else return false;
        }
    }
    return brackets.empty();
}
const lest::test tests[] = {
    CASE("Matching Parens test") {

        EXPECT(bracketValidator("[[]]()")  == true);
        EXPECT(bracketValidator("[[]](})")  == false);
    }
};

int main (int argc, char **argv)
{
    // run your function through some test cases here
    // remember: debugging is half the battle!
    return lest::run(tests, argc, argv);
}
