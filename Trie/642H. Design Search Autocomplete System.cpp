/*
642H. Design Search Autocomplete System

Description:
Design a search autocomplete system for a search engine. 
Users may input a sentence (at least one word and end with a special character '#'). 
For each character they type except '#', you need to return the top 3historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
3. If less than 3 hot sentences exist, then just return as many as you can.
4. When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.


Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2]) 
The system have already tracked down the following sentences and their corresponding times: 
"i love you" : 5 times 
"island" : 3 times 
"ironman" : 2 times 
"i love leetcode" : 2 times 
Now, the user begins another search: 

Operation: input('i') 
Output: ["i love you", "island","i love leetcode"] 
Explanation: 
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored. 

Operation: input(' ') 
Output: ["i love you","i love leetcode"] 
Explanation: 
There are only two sentences that have prefix "i ". 

Operation: input('a') 
Output: [] 
Explanation: 
There are no sentences that have prefix "i a". 

Operation: input('#') 
Output: [] 
Explanation: 
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search. 



Note:
The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.
*/

//
// Created by Shiyi Yang on 2021-06-20.
//
#include <iostream>
#include <string>
#include <list>
#include <map>
#include <vector>
#include <queue>
using namespace std;

class AutocompleteSystem{
private:
    // Define a trienode
    struct TrieNode{
        map<char, TrieNode*> children;
        bool is_word;
        int counts;
        string str;
        TrieNode(){is_word = false; counts = 0; str = "";}
    };
    
    // Overload operator () for priority_queue
    // Reverse the order of priority_queue
    // Compare counts. If counts are equal, compare string 
    struct cmp{
        bool operator()(pair<string, int>& p1, pair<string, int>& p2){
            return p1.second < p2.second || (p1.second==p2.second && p1.first > p2.first);
        }
    };

    TrieNode* root;
    // Declare a string to hold the inputs
    string rec;
    // Declare a priority_queue to hold recommended strings
    // Remember, this is the default structure of a priority_queue with a user-defined operator
    priority_queue<pair<string, int>, vector<pair<string, int>>, cmp> q;
public:
    
    AutocompleteSystem(vector<string> sentences, vector<int> times){
        root = new TrieNode();
        for(int i=0; i<sentences.size(); ++i){
            add(sentences[i], times[i]);
        }
        rec = "";
    }
    
    // Add sentences to a trie
    void add(string sentence, int times){
        TrieNode* node = root;
        for(auto letter:sentence){
            if(!node->children[letter]){
                node->children[letter] = new TrieNode();
            }
            node = node->children[letter];
        }
        node->is_word = true;
        node->str = sentence;
        node->counts += times;
    }

    vector<string> input(char c){
        // If the input is #, it means the user has finished sending the input
        // We need to add the saved string to the trie
        // Clear rec and return {}
        if(c=='#'){
            add(rec, 1);
            rec.clear();
            return {};
        }
        
        // Add the new input to rec
        rec += c;
        TrieNode* node = root;
        
        // Search the trie until the last input character
        for(auto letter:rec){
            node = node->children[letter];
            if(!node){return {};}
        }
        
        // Use dfs to search each single subtree
        search(node);
        vector<string> res;
        int n = 3;
        while(n>0 && !q.empty()){
            res.push_back(q.top().first);
            q.pop();
            --n;
        }
        
        // Keep in mind, we need to clear the queue after each input
        // Otherwise, it will keep the recommended string from last run
        while(!q.empty()){q.pop();}
        return res;


    }
    
    // This is an implementation of dfs
    void search(TrieNode* node){
        // When we reach the end of a subtree, 
        // we push the string and counts that are saved at the end trienode to queue
        if(node->is_word){
            q.push(make_pair(node->str, node->counts));
        }
        // Search each single child node
        for(auto child:node->children){
            search(child.second);
        }
    }
};

int main(){
    AutocompleteSystem *obj = new AutocompleteSystem({"i love you", "island","ironman", "i love leetcode"}, {5,3,2,2});
    vector<string> param_1 = obj->input('i');
    for(auto str:param_1){
        cout << str << endl;
    }
    cout << "==========" << endl;
    vector<string> param_2 = obj->input(' ');
    for(auto str:param_2){
        cout << str << endl;
    }
    cout << "==========" << endl;
    vector<string> param_3 = obj->input('#');
    for(auto str:param_3){
        cout << str << endl;
    }
}

/*
Output:
i love you
island
i love leetcode
==========
i love you
i love leetcode
==========
*/
