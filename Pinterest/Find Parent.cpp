/*
 * Input is {{1,4}, {1,5},{2,5},{3,6},{6,7},{8,2},{8,3}}
 * Q1: Find the nodes which have no parent nodes or only 1 parent node
 * Q2: Determine if two nodes have common parent node
 * Q3: Find the furthest parent node.
 *     e.g. for node 5, there are two furthest parent nodes 1,2, we only need to output one of them
 * */

/*
 * Algorithm:
 * S1. We need to build a map. The key of this map is the value of node, the corresponding value is the
 *     its parent nodes.
 *     e.g., for a pair of nodes {1, 4}, m1[4].insert(1).
 * S2. Create another map, the key is the node value, the values are its children.
 *     e.g., for a pair of nodes {1, 4}, m2[1].insert(4).
 * S3. For every pair of values, we need to check if the parent node has any parents and if the child node has
 *     any children.
 *
 * */
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution{
public:
    // In this hashmap, the key is the node value, and the corresponding values are its parents
    unordered_map<int, unordered_set<int>> m1;
    // In this hashmap, the key is the node value, and the corresponding values are its children
    unordered_map<int, unordered_set<int>> m2;
    vector<int> oneOrnoParent(vector<vector<int>> vec){
        for(auto v:vec){
            // Insert parent v[0] to v[1]
            m1[v[1]].insert(v[0]);
            // Check if v[0] has any parents. If it has, insert all v[0]'s parents to v[1]
            if(m1[v[0]].size()){
                m1[v[1]].insert(m1[v[0]].begin(), m1[v[0]].end());
            }
            // Check if v[1] has any children. If it has, insert v[1]'s parents to its children
            if(m2[v[1]].size()){
                for(auto val:m2[v[1]]){
                    m1[val].insert(m1[v[1]].begin(), m1[v[1]].end());
                }
            }

            // Insert child
            m2[v[0]].insert(v[1]);
            // Check if v[1] has any children. If it has, insert all v[1]'s children to v[0]
            if(m2[v[1]].size()){
                m2[v[0]].insert(m2[v[1]].begin(), m2[v[1]].end());
            }
            // Check if v[0] has any parents, if it has, insert v[0]'s children to its parents
            if(m1[v[0]].size()){
                for(auto val:m1[v[0]]){
                    m2[val].insert(m2[v[0]].begin(), m2[v[1]].end());
                }
            }

        }
        // Iterate over the keys in the map, and check the number of parents
        vector<int> res;
        for(auto key:m1){
            if(key.second.size()<2){
                res.push_back(key.first);
            }
        }
        return res;
    }

    int find_common_parent(int i1, int i2){
        for(auto val:m1[i1]){
            if(m1[i2].count(val)!=0){
                return val;
            }
        }
        return -1;
    }

    int find_furthest_parent(int i){
        // For each parent of i, check the number of parents that it has
        for(auto val:m1[i]){
            if(m1[val].size()==1){
                return *m1[val].begin();
            }
        }
    }
};

int main(){
    vector<vector<int>> vec = {{1,4}, {1,5},{2,5},{3,6},{6,7}, {5,9}, {8,2}, {8,3}};
    Solution *obj = new Solution();

    vector<int> res = obj->oneOrnoParent(vec);
    cout << obj->find_common_parent(7, 9) << endl;
    cout << obj->find_furthest_parent(9) << endl;
}

