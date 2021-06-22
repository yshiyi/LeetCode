/*
1804M. Implement Trie II

Description:
A trie (pronounced as "try") or prefix tree is a tree data structure 
used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
1. Trie() Initializes the trie object.
2. void insert(String word) Inserts the string word into the trie.
3. int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
4. int countWordsStartingWith(String prefix) 
   Returns the number of strings in the trie that have the string prefix as a prefix.
5. void erase(String word) Erases the string word from the trie.
 

Example 1:
Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0
 

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, countWordsEqualTo, countWordsStartingWith, and erase.
It is guaranteed that for any function call to erase, the string word will exist in the trie.
*/

/*
Method:
 1. Create a TrieNode struct. It is composed of a map, a boolean var, an int.
 2. Add input word to Trie, and increase the value of count.
 3. If the word is in Trie, retrieve the value of count.
 4. Use depth-first search to sum up all possible counts.
 5. Remove TrieNode from Trie. We only need to reduce the value of count by 1.
*/

#include <iostream>
#include <map>
using namespace std;

class Trie{
private:
    struct TrieNode{
        map<char, TrieNode*> children;
        bool is_word;
        int count;
        TrieNode(){
            is_word = false;
            count = 0;
        }
    };
    TrieNode* root;
public:
    Trie(){
        root = new TrieNode();
    }

    void insertTrie(string word){
        TrieNode* node = root;
        for(auto letter:word){
            if(!node->children[letter]){
                node->children[letter] = new TrieNode();
            }
            node = node->children[letter];
        }
        node->is_word = true;
        ++node->count;
    }

    int countWordsEqualTo(string word){
        TrieNode* node = root;
        for(auto letter:word){
            if(!node->children[letter]){
                return 0;
            }
            node = node->children[letter];
        }

        return node->count;
    }

    int countWordsStartingWith(string prefix){
        TrieNode* node = root;
        for(auto letter:prefix){
            if(!node->children[letter]){
                cout << prefix << "#" << endl;
                return 0;
            }
            node = node->children[letter];
        }
        int total_num = 0;
        return search(node, total_num, prefix);
    }

    int search(TrieNode* node, int total_num, string prefix){
        if(node->is_word){
            return node->count;
        }
        for(auto child:node->children){
            total_num += search(child.second, total_num, prefix);
        }
        return total_num;
    }

    void erase(string word){
        TrieNode* node = root;
        for(auto letter:word){
            if(!node->children[letter]){
                return;
            }
            node = node->children[letter];
        }
        if(node->count>0){
            --node->count;
        }
    }
};

int main(){
    Trie* trie = new Trie();
    trie->insertTrie("apple");               // Inserts "apple".
    trie->insertTrie("apple");               // Inserts another "apple".
    cout << trie->countWordsEqualTo("apple") << endl;    // There are two instances of "apple" so return 2.
    cout << trie->countWordsStartingWith("app") << endl; // "app" is a prefix of "apple" so return 2.
    trie->erase("apple");                // Erases one "apple".
    cout << trie->countWordsEqualTo("apple") << endl;    // Now there is only one instance of "apple" so return 1.
    cout << trie->countWordsStartingWith("app") << endl; // return 1
    trie->erase("apple");                // Erases "apple". Now the trie is empty.
    cout << trie->countWordsStartingWith("app") << endl; // return 0

    return 0;
}
