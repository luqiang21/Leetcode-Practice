class WordDictionaryHashMap {
public:
    /** Initialize your data structure here. */
//     WordDictionary() {
        
//     }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        words[word.length()].push_back(word);
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        for (auto& str : words[word.size()]) if (isEqual(word, str)) return true;
        return false;
    }
    
private:
    unordered_map<int, vector<string>> words;
    bool isEqual(string& word1, string& word2) {
        for (int i = 0; i < word1.size(); ++i) {
            if (word1[i] == '.') continue;
            if (word1[i] != word2[i]) return false;
        }
        
        return true;
    }
};

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isWord = false;
    
    
    TrieNode* next[26];
    TrieNode(){
        memset(next, NULL, sizeof(next));
    }
};

class WordDictionaryTrieMap {
public:
    /** Initialize your data structure here. */
    // WordDictionaryMine() {
    // }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        auto cur = root;
        for (auto& ch : word) {
            if (!cur -> children.count(ch)) cur -> children[ch] = new TrieNode();
            cur = cur -> children[ch];
        }
        cur -> isWord = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return search(word, 0, root);
    }
    bool search(string word, int idx, TrieNode* node) {
        auto cur = node;
        for (int i = idx; i < word.length(); ++i) {
            auto& ch = word[i];
            if (ch == '.') {
                if (cur -> children.size() == 0) return false;
                for (auto child : cur -> children) {
                    if (search(word, i + 1, child.second)) return true;
                }
                return false;
            }
            else {
                if (!cur -> children.count(ch)) return false;
                cur = cur -> children[ch];
            }
        }
        
        return cur -> isWord == true;
    }
private:
    TrieNode* root = new TrieNode();;
    
};


// using array for children
class WordDictionary {
public:
    /** Initialize your data structure here. */
    // WordDictionary() {
    // }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        auto cur = root;
        for (auto& ch : word) {
            if (!cur -> next[ch - 'a']) cur -> next[ch - 'a'] = new TrieNode();
            cur = cur -> next[ch - 'a'];
        }
        cur -> isWord = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return search(word, root);
    }
    bool search(string word, TrieNode* node) {
        auto cur = node;
        for (int i = 0; i < word.length(); ++i) {
            auto ch = word[i];
            if (ch == '.') {
                for (auto child : cur -> next) {
                    if (child && search(word.substr(i+1), child)) return true;
                }
                return false;
            }
            else {
                if (!cur -> next[ch - 'a']) return false;
                cur = cur -> next[ch - 'a'];
            }
        }
        
        return cur -> isWord == true;
    }
private:
    TrieNode* root = new TrieNode();;
};


/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
