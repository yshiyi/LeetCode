/*
1268M. Search Suggestions System

Description:
Given an array of strings products and a string searchWord. 
We want to design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with the searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.
Return list of lists of the suggested products after each character of searchWord is typed. 


Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Example 3:
Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

Example 4:
Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]

Constraints:
1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
*/

/*
Build a trie. 
On each trienode, we define:
1. a map to hold possible subtrees
2. a boolean variable to determine if it is a full word
3. a string to hold full string from products

At the beginning, we save all strings in products to trie

In search process, we create two for loops.
The first for loop is for the number of input characters.
The second for loop is traverse the trie pointer to the desirec node.
Then use depth-first search to find all possible recommended strings.

*/

class Solution {
private:
    struct TrieNode{
        map<char, TrieNode*> children;
        bool is_word;
        string str;
        TrieNode(){is_word=false; str="";}
    };
    TrieNode* root;
    vector<vector<string>> rec;
    vector<string> temp;
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string searchWord) {
        root = new TrieNode();
        for(auto words:products){
            add(words);
        }
        
        bool flag = false;
        for(int i=0; i<searchWord.size(); i++){
            TrieNode* node = root;
            for(int j=0; j<i+1; j++){
                if(!node->children[searchWord[j]]){
                    // If there is no recommended strings,
                    // save the empty temp and break
                    rec.push_back(temp);
                    flag = true;
                    break;
                }
                node = node->children[searchWord[j]];
            }
            
            if(!flag){
                search(node);
                rec.push_back(temp);
                temp.clear();
            }
        }
        
        return rec;
    }
    
    void add(string &words){
        TrieNode* node = root;
        for(auto letter:words){
            if(!node->children[letter]){
                node->children[letter] = new TrieNode();
            }
            node = node->children[letter];
        }
        node->is_word = true;
        node->str = words;
    }
    
    void search(TrieNode* node){
        // Check the size of temp
        // If the size is equal to 3, then return
        if(temp.size()==3){
            return;
        }
        if(node->is_word){
            temp.push_back(node->str);
        }
        for(auto child:node->children){
            search(child.second);
        }
    }
    
};
