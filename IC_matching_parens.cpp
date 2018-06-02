#include <iostream>
#include "lest.hpp"
using namespace std;

/**
"Sometimes (when I nest them (my parentheticals) too much (like this (and this)))
they get confusing."

Write a function that, given a sentence like the one above, along with the position
of an opening parenthesis, finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of
the first parenthesis), the output should be 79 (position of the last parenthesis).
*/

size_t getClosingParen(const string& sentence, size_t openingParenIndex) {
    size_t openNestedParens = 0;

    for(size_t position = openingParenIndex + 1; position < sentence.length(); ++ position) {
        char c = sentence[position];

        if(c == '(') {
            ++ openNestedParens;
        }
        else if(c == ')') {
            if(openNestedParens == 0) {
                return position;
            }
            else {
                --openNestedParens;
            }
        }
    }

    throw invalid_argument("No closing parenthesis :(");
}


const lest::test tests[] = {
    CASE("Matching Parens test") {

        EXPECT(getClosingParen ("test( inp)ut", 4)  == 9);

    }
};
int main (int argc, char **argv)
{
    // run your function through some test cases here
    // remember: debugging is half the battle!
    return lest::run(tests, argc, argv);
}
