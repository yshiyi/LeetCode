/*
677M. Map Sum Pairs
Trie

Description:
Implement the MapSum class:
1. MapSum() Initializes the MapSum object.
2. void insert(String key, int val) Inserts the key-val pair into the map. 
   If the key already existed, the original key-value pair will be overridden to the new one.
3. int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:
1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
*/

class MapSum {
private:
    struct TrieNode{
        map<int, TrieNode*> next;
        int score;
        TrieNode(){score = 0;};
    };
    TrieNode* root;
    map<string, int> m;
public:
    /** Initialize your data structure here. */
    MapSum() {
        root = new TrieNode();
    }
    
    void insert(string key, int val) {
        int delta = 0;
        if(m[key]){delta = val - m[key];}
        m[key] = val;
        
        TrieNode* node = root;
        for(auto letter:key){
            int i = letter - 'a';
            if(!node->next[i]){node->next[i]=new TrieNode();}
            node = node->next[i];
            if(!delta){
                node->score = node->score + val;
            }else{
                node->score = node->score + delta;
            }            
        }
    }
    
    int sum(string prefix) {
        TrieNode* node = root;
        for(auto letter:prefix){
            int i = letter - 'a';
            if(!node->next[i]){return 0;}
            node = node->next[i];
        }
        return node->score;
    }
};

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum* obj = new MapSum();
 * obj->insert(key,val);
 * int param_2 = obj->sum(prefix);
 */
