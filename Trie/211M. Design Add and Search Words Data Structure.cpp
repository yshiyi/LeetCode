/*
211M. Design Add and Search Words Data Structure

Description:
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
1. WordDictionary() Initializes the object.
2. void addWord(word) Adds word to the data structure, it can be matched later.
3. bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
   word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:
1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

Similar Questions:
Prefix and Suffix Search - Hard
*/

/*
Method: We can design a trie using the standard method.
        If there is a '.', we have to check all possible subtrees.
*/
class WordDictionary {
private:
    struct TrieNode{
        map<int, TrieNode*> next;
        bool is_word;
        TrieNode(){is_word = false;};
    };
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* node = root;
        for(auto letter:word){
            int i = letter - 'a';
            if(!node->next[i]){node->next[i] = new TrieNode();}
            node = node->next[i];
        }
        node->is_word = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        return searchTrie(root, word, 0);
    }
    
    bool searchTrie(TrieNode* node, string& word, int i){
        if(i==word.size()){return node->is_word;}
        if(word[i]!='.'){
            int j = word[i] - 'a';
            if(!node->next[j]){return false;}
            return searchTrie(node->next[j], word, i+1);
        }else{
            for(auto kv:node->next){
                // If node->next is not null and it is the same as word[i+1], then return true.
                if(kv.second && searchTrie(kv.second, word, i+1)){
                    return true;
                }
            }
            // return false;
        }
        return false;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
