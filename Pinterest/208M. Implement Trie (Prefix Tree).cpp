/*
208M. Implement Trie (Prefix Tree)
Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store 
and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), 
and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that 
has the prefix prefix, and false otherwise.


Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.


Simliar Questions:
Design Add and Search Words Data Structure - Medium
Design Search Autocomplete System - Hard
Replace Words - Medium
Implement Magic Dictionary - Medium
Implement Trie II (Prefix Tree) - Medium
*/

/*
Solution: We first need to define a struct of TrieNode which is similar to what we define a TreeNode.
          We can define next as an array or a hashmap.
          Note: when we must initialize the array like next[26]={}. Hence, there are 26 0s in the array.
*/
class Trie {
private:
    struct TrieNode{
        // Using array
        TrieNode* next[26] = {};
      
        // Using hashmap
        map<int, TrieNode*> next;
      
        bool is_word;
        TrieNode(){
            is_word = false;
            // for(auto n:next){
            //     n = nullptr;
            // }
        }
    };
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* node = root;
        for(auto ch:word){
            int i = ch - 'a';
            if(!node->next[i]){node->next[i]=new TrieNode();}
          
            // Using hashmap, this way also works
            // if(!node->next.count(i){node->next[i]=new TrieNode();}
            node = node->next[i];
        }
        node->is_word = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* node = root;
        for(auto ch:word){
            int i = ch - 'a';
            if(!node->next[i]){return false;}
            node = node->next[i];
        }
        return node->is_word;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for(auto ch:prefix){
            int i = ch - 'a';
            if(!node->next[i]){return false;}
            node = node->next[i];
        }
        return true;
    }

};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
