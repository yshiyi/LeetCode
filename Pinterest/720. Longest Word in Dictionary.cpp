/*
720. Longest Word in Dictionary

Description:
Given an array of strings words representing an English Dictionary, 
return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order. 
If there is no answer, return the empty string.
 

Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. 
             However, "apple" is lexicographically smaller than "apply".

Example 3:
Input: words = ["wo","wor","worl","world"]
Output: ""
Explanation: "w" is not in the dictionary.

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.
*/

/*
Method: Using Trie to build a dictionary
        If a word is valid, then each letter in this word must be saved in the trie.
        Hence, before we compare the length of each input words, we need to make sure they are valid.
*/

class Solution {
private:
    struct TrieNode{
        map<char, TrieNode*> children;
        bool is_word;
        TrieNode(){is_word = false;}
    };
    TrieNode* root;
public:
    void insertTrie(string word){
        TrieNode* node = root;
        for(auto letter:word){
            if(!node->children[letter]){
                node->children[letter] = new TrieNode();
            }
            node = node->children[letter];
        }
        node->is_word = true;
    }
    
    // Check if the word is a valid word.
    bool inTrie(string word){
        TrieNode* node = root;
        for(auto letter:word){
            node = node->children[letter];
            // For each letter, we check if it is saved in trie.
            if(!node->is_word){
                return false;
            }
        }
        return node->is_word;
    }
    
    string longestWord(vector<string>& words) {
        root = new TrieNode();
        for(auto word:words){
            insertTrie(word);
        }
        
        set<string> s_str;
        int max_len = 0;
        for(auto word:words){
            if(inTrie(word)){
                // If the length of current word is greater than the maximum,
                // we should clear out the set and insert this new word.
                if(word.size()>max_len){
                    s_str.clear();
                    max_len = word.size();
                    s_str.insert(word);
                }
                if(word.size()==max_len){
                    s_str.insert(word);
                }
            }
        }
        // Just in case if there is no valid word.
        if(!s_str.size()){
            return {};
        }else{
            return *s_str.begin();
        }
    }
};
