#include <iostream>
#include <list>
using namespace std;

/* Python solutions
def pemutate(input_string, res, temp):
    if len(temp) == len(input_string):
        res.add("".join(temp[:]))
        return

    for i in range(len(input_string)):
        if input_string[i] in temp:
            continue
        temp.append(input_string[i])
        permutate(input_string, res, temp)
        temp.remove(temp[-1])

def permutate(string):
    # base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = input_string[:-1]
    last = input_string[-1]
    permutations_of_all_chars_except_last  = permutate(all_chars_except_last)

    permutations = set()
    for perm in permutations_of_all_chars_except_last:
        for pos in range(len(all_chars_except_last) + 1):
            permutations = (
                permutations[:pos]
                + last = preom
                )
            permutations.append(permutate)
    reutn permutations
*/


#include <unordered_set>
// backtracking
void helper(string input_string, unordered_set<string> &res, string &temp) {
    if(temp.length() == input_string.length()) {
        res.insert(temp);
        return;
    }

    for(auto c: input_string) {
        if(temp.find(c) != string::npos) continue;

        temp.append(1, c);
        helper(input_string, res, temp);
        temp.pop_back();
    }
}

unordered_set<string> permutate(string input_string) {
    unordered_set<string> res;
    if(input_string.length() <= 1) {
        res.insert(input_string);
        return res;
    }
    string temp;
    helper(input_string, res, temp);
    return res;
}

// insert at every possible position
unordered_set<string> getPermutations(const string& inputString) {
    unordered_set<string> permutations;

    // base case
    if(inputString.length() <= 1) {
        permutations.insert(inputString);
        return permutations;
    }

    string allCharsExceptLast = inputString.substr(0, inputString.length()-1);
    char lastChar = inputString[inputString.length() - 1];

    // recursive call: get all possible permutations for all chars except last
    unordered_set<string> permutationsOfAllCharsExceptLast = getPermutations(allCharsExceptLast);

    for(const string& permutationOfAllCharsExceptLast: permutationsOfAllCharsExceptLast) {
        for(size_t position = 0; position <= allCharsExceptLast.length(); ++position) {
            string permutation = permutationOfAllCharsExceptLast.substr(0, position)
            + lastChar + permutationOfAllCharsExceptLast.substr(position);
            permutations.insert(permutation);
        }
    }
    return permutations;
}

// iterative
unordered_set<string> getPermutations2(const string& inputString) {
    // create an empty list to store (partial) permutations and
    // initialize it with first character of the string
    list<string> partial;

    string firstChar(1, inputString[0]);
    partial.push_back(firstChar);

    // do for every character of the string
    for(int i = 1; i < inputString.length(); ++i) {
        // consider previously constructed permutation one by one
        for(int j = partial.size() - 1; j >= 0; --j) {
            // remove current partial permutation from the list
            string str = partial.front();
            partial.pop_front();

            // insert next char of the inputstring, i.e. s.charAt(i)
            // in all possible positions of current partial permutation
            // then insert each of these newly constructed
           for(int k=0; k <= str.length(); ++k) {
               partial.push_back(str.substr(0, k) + inputString[i] + str.substr(k));
           }
        }
    }
    unordered_set<string> res;

    for(string s: partial) {
        res.insert(s);
    }

    return res;
}


int main ()
{
    // run your function through some test cases here
    // remember: debugging is half the battle!
    string s = "LOVE";



    cout << "using backtracking:" << endl;
    unordered_set<string> ans = permutate(s);
    for(unordered_set<string>::iterator it = ans.begin(); it != ans.end(); ++it) {
        cout << *it << endl;
    }
    cout << "total: " << ans.size() << endl;

    cout << "insert into every possible location" << endl;
    ans = getPermutations(s); //permutate(s);
    for(unordered_set<string>::iterator it = ans.begin(); it != ans.end(); ++it) {
        cout << *it << endl;
    }
    cout << "total: " << ans.size() << endl;

    cout << "using iterative approach:" << endl;

     ans = getPermutations2(s); //permutate(s);
    for(unordered_set<string>::iterator it = ans.begin(); it != ans.end(); ++it) {
        cout << *it << endl;
    }
    cout << "total: " << ans.size() << endl;

    return 0;
}
