/*
Description:
3.	bad_phrases = [
    "i like violence",
    "i like violence too",
    "gore",
    "world war i",
    "world war ii"
]

query_str
is_bad_phrase("foo i like violence bar", bad_phrases) -> True
is_bad_phrase("i like pie", bad_phrases) -> False
is_bad_phrase("like violence i", bad_phrases) -> False
is_bad_phrase("world war is bad", bad_phrases) -> False (3)
*/

/*
 * Method:
 * Build a trie structure to hold all bad phrases
 *
 * Check phase:
 * For checking the test phrase, we traverse the word
 * until we find a letter which appears on the second level of trie.
 * Then we traverse the trie and check if the full subtree is in the test phrase.
 *
 */
#include <iostream>
#include <vector>
#include <map>
#include <string>
using namespace std;

class detectBadPhrase{
private:
    struct TrieNode{
        map<char, TrieNode*> children;
        bool is_word;
        TrieNode(){is_word = false;}
    };
    TrieNode* root;
public:
    detectBadPhrase(vector<string>& bad_phrase){
        root = new TrieNode();
        for(auto& word:bad_phrase){
            add(word);
        }
    }

    void add(string word){
        TrieNode* node = root;
        for(auto &letter:word){
            if(!node->children[letter]){
                node->children[letter] = new TrieNode();
            }
            node = node->children[letter];
        }
        node->is_word = true;
    }

    bool is_bad_phrase(string &word){
        TrieNode* node = root;
        for(int i=0; i<word.size(); ++i){
            if(node->children[word[i]]){
                node = node->children[word[i]];
            }else{
                // If it is not a full bad phrase, we move our pointer back to the root.
                node = root;
            }
            if(node->is_word){
                // This part is to make sure the test word contains a full bad phrase
                // Two conditions: 1. reach the end of phrase 2. next letter is a space (world war is)
                if(i==word.size()-1 || word[i+1]==' '){
                    return node->is_word;
                }else{
                    node = root;
                }
            }
        }
        return false;
    }
};

int main(){
    vector<string> bad_phrase = {"i like violence", "i like violence too",
                                 "gore", "world war i", "world war ii"};
    detectBadPhrase *obj = new detectBadPhrase(bad_phrase);
    vector<string> test_phrase = {"foo i like violence bar", "i like pie",
                                  "like violence i", "world war is bad", "i think you like violence"};

    for(auto word:test_phrase){
        cout << obj->is_bad_phrase(word) << endl;
    }

}

