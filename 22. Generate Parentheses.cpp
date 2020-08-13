class Solution {
public:
    vector<string> generateParenthesis1(int n) {
        vector<string> combinations;
        generate("", n, combinations);
        return combinations;
    }
private:
    void generate(string temp, int n, vector<string>& combinations) {
        if (temp.length() == 2*n) {
            if (valid(temp)) combinations.push_back(temp);
        }
        else {
            temp.push_back('(');
            generate(temp, n, combinations);
            temp.pop_back();
            temp.push_back(')');
            generate(temp, n, combinations);
        }
    }
    bool valid(string cur) {
        int bal = 0;
        for (char& c : cur) {
            if (c == '(') bal++;
            else bal--;
            
            if (bal < 0) return false;
        }
        return bal == 0;
    }
    
public:
    vector<string> generateParenthesis2(int n) {
        vector<string> combinations;
        backtrack(combinations, "", 0, 0, n);
        return combinations;
    }
    
    void backtrack(vector<string>& combinations, string cur, int open, int close, int max) {
        if (cur.length() == 2 * max) {
            combinations.push_back(cur);
            return;
        }
        
        if (open < max) {
            backtrack(combinations, cur + '(', open + 1, close, max);
        }
        if (close < open) {
            backtrack(combinations, cur + ')', open, close + 1, max);
        }
    }
    
    vector<string> generateParenthesis3(int n) {
        vector<string> combinations;
        if (n == 0) return {""};
        for (int c = 0; c < n; ++c) {
            for (const auto& left : generateParenthesis(c)) {
                for (const auto& right : generateParenthesis(n-1-c)) {
                    combinations.push_back("(" + left + ")" + right);
                }
            }
        }
        return combinations;
    }
    
    
    
    /*这种方法的思想是找左括号，每找到一个左括号，就在其后面加一个完整的括号，最后再在开头加一个 ()，就形成了所有的情况，需要注意的是，有时候会出现重复的情况，所以用set数据结构，好处是如果遇到重复项，不会加入到结果中，最后我们再把set转为vector即可，参见代码如下：：

n＝1:    ()

n=2:    (())    ()()

n=3:    (()())    ((()))    ()(())    (())()    ()()()
*/
    vector<string> generateParenthesis(int n) {
        if (n == 0) return {""};
        unordered_set<string> st;
        vector<string> pre = generateParenthesis(n-1);
        for (auto a : pre) {
            for (int i = 0; i < a.size(); ++i) {
                if (a[i] == '(') {
                    a.insert(a.begin() + i + 1, '(');
                    a.insert(a.begin() + i + 2, ')');
                    st.insert(a);
                    a.erase(a.begin() + i + 1, a.begin() + i + 3);
                }
            }
            st.insert("()" + a);
        }
        return vector<string>(st.begin(), st.end());
    }
};








