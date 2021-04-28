# Graph
<!-- GFM-TOC -->
* [Leetcode Graph](#Graph)
   * [1. Introduction to Graph](#1-Introduction-to-Graph)
     * [1.1 Structure of Graph](#11-Structure-of-Graph)
     * [1.2 Traverse a graph](#12-Traverse-a-graph)
     * [797M. All Paths From Source to Target](#797M-All-Paths-From-Source-to-Target)
<!-- GFM-TOC -->

# 1. Introduction to Graph
## 1.1 Structure of Graph
A graph is a type of data structure which is consisted of multiple vertexes. Each vertex can be defined as:
```
class Vertex {
    int id;
    Vertex[] neighbors;
}
```
As we can see, each vertex can also be considered as a treenode with multiple children/subtrees.
```
class TreeNode {
    int val;
    TreeNode[] children;
}
```
For an example, consider the following graph:\
<pre>
          0  ->   1
        /   \   /   \
       ''    ''      ''
       4  <-  3  <-  2
</pre>
This graph can be represented as a chart:
```
0: [1, 3, 4]
1: [2, 3, 4]
2: [3]
3: [4]
4: []
```
or a matrix:
```
   0  1  2  3  4
0  f  t  f  t  t
1  f  f  t  t  t
2  f  f  f  t  f
3  f  f  f  f  t
4  f  f  f  f  f

```
The advantage of using chart to represent a graph is that we can easily inquire the childern of a particular vertex. However, it requires more space to store the data.\
The advantage of using a matrix is that it is fast to check if two vertexes are connected to each other. It is also space efficient.\
If there exist different weights on each edge between two vertexes, we can replace t/f with the corresponding value of weights.

## 1.2 Traverse a graph
The basic way to traverse a graph recursively is:
```
void traverse(TreeNode root) {
    if (root == null) return;

    for (TreeNode child : root.children)
        traverse(child);
}
```
**Note:** the most important difference between a binary tree and a graph is that there may exist a circle in a graph.\
Therefore, if there exist a circle in the graph, we need a vector ro check if we have entered this vertex before.
```
Graph graph;
boolean[] visited;

void traverse(Graph graph, int s) {
    if (visited[s]) return;
    // enter s
    visited[s] = true;
    for (TreeNode neighbor : graph.neighbors(s))
        traverse(neighbor);
    // leave s
    visited[s] = false;   
}
```
There are two ways to visit the vertex: outside of for loop:
```
void traverse(TreeNode root) {
    if (root == null) return;
    System.out.println("enter: " + root.val);
    for (TreeNode child : root.children) {
        traverse(child);
    }
    System.out.println("leave: " + root.val);
}

enter: 0
enter: 1
enter: 2
enter: 3
enter: 4
leave: 4
leave: 3
leave: 2
enter: 3
enter: 4
leave: 4
leave: 3
enter: 4
leave: 4
leave: 1
enter: 3
enter: 4
leave: 4
leave: 3
enter: 4
leave: 4
leave: 0
```
or inside of for loop:
```
void traverse(TreeNode root) {
    if (root == null) return;
    for (TreeNode child : root.children) {
        System.out.println("enter: " + child.val);
        traverse(child);
        System.out.println("leave: " + child.val);
    }
}

enter: 1
enter: 2
enter: 3
enter: 4
leave: 4
leave: 3
leave: 2
enter: 3
enter: 4
leave: 4
leave: 3
enter: 4
leave: 4
leave: 1
enter: 3
enter: 4
leave: 4
leave: 3
enter: 4
leave: 4
```
Using the first way, we can visit all vertexes. On the other hand, we will miss the root vertex by using the second method.\
Therefore, to traverse a graph, we should use the first method.\


## 797. All Paths From Source to Target
**Description:**\
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.\
The graph is given as follows: graph\[i\] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph\[i\]\[j\]).\
**Method:**\
Traverse the graph and save each path.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/797M.%20All%20Paths%20From%20Source%20to%20Target.cpp)
```
class Solution {
public:
    vector<vector<int>> res;
    map<int, bool> m;
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
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Tree/797M.%20All%20Paths%20From%20Source%20to%20Target.py)
```
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        self.res = []
        path = []
        self.traverse(graph, 0, path)
        return self.res
    
    def traverse(self, graph, s, path):
        path.append(s)
        if s==(len(graph)-1):
            self.res.append(deepcopy(path))
            path.pop()
            return
        for node in graph[s]:
            self.traverse(graph, node, path)
        path.pop()
```
