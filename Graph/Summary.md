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
