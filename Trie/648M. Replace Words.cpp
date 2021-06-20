/*
648M. Replace Words

Description:
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. 
For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. 
If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.
 

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"

Example 3:
Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"

Example 4:
Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 5:
Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"

Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Each two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
*/

class Solution {
private:
    struct TrieNode{
        map<int, TrieNode*> next;
        
        // Use is_word to denote that the subtree is a prefix
        bool is_word;
        TrieNode(){is_word = false;};
    };
    TrieNode* root = new TrieNode();
public:
    void createTrie(string word){
        TrieNode* node = root;
        for(auto letter:word){
            int i = letter - 'a';
            if(!node->next[i]){node->next[i] = new TrieNode();}
            node = node->next[i];
        }
        node->is_word = true;
    }
    
    string searchPrefix(string word){
        TrieNode* node = root;
        string res = "";
        for(auto letter:word){
            int i = letter - 'a';
            // If letter is not in the trie, we break out the loop and return word
            if(!node->next[i]){break;}
            res.push_back(letter);
            node = node->next[i];
            // Check is_word. When it is true, it measn the current word contains a full prefix 
            if(node->is_word){return res;}
        }
        return word;
    }
    
    string replaceWords(vector<string>& dictionary, string sentence) {
        for(auto word:dictionary){
            createTrie(word);
        }
        istringstream iss(sentence);
        string res = "", w="";
        while(iss >> w){
            if(!res.empty()){res += " ";}
            res += searchPrefix(w);
        }
        return res;
    }
};
