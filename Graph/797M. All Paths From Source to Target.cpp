/*
797M. All Paths From Source to Target
Backtracking, Depth-first Search, Tree

Description:
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
          0  ->   1
        /   \   /   \
       ''    ''      ''
       4  <-  3  <-  2

Example 3:
Input: graph = [[1],[]]
Output: [[0,1]]

Example 4:
Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]

Example 5:
Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
 

Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
The input graph is guaranteed to be a DAG.
*/


// Solution: traverse the graph and save each path
class Solution {
public:
    vector<vector<int>> res;
    map<int, bool> m;
    // We can also define a globle variable. In this case, we don't need to pass this variable every iteration.
    // vector<int> path; 
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<int> path;
        // traverse(graph, 0, path, m);
        traverse(graph, 0, path);
        return res;
    }
    void traverse(vector<vector<int>> graph, int s, vector<int> path){
        // if(m[s]==true){return;}
        
        // enter the node and save it to the path
        path.push_back(s);
        // m[s] = true;
        int n = graph.size();
        if(s==n-1){
            res.push_back(path);
            path.pop_back();
            return;
        }
        for(auto val:graph[s]){
            // traverse(graph, val, path, m);
            traverse(graph, val, path);
        }
        
        // Leave the node and remove it from the path
        path.pop_back();
        // m[s] = false;
    }
};
