"""
785M. Is Graph Bipartite.py

Description:
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. 
You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. 
More formally, for each v in graph[u], there is an undirected edge between node u and node v. 
The graph has the following properties:

- There are no self-edges (graph[u] does not contain u).
- There are no parallel edges (graph[u] does not contain duplicate values).
- If v is in graph[u], then u is in graph[v] (the graph is undirected).
- The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge 
in the graph connects a node in set A and a node in set B.
Return true if and only if it is bipartite.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

Constraints:
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""

"""
Method: DFS to traverse the whole graph. Use 0 and 1 to represent two colors, and check if the colors of adjacent nodes are the same.
        
"""
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.visited = [0] * len(graph)
        self.color = [0] * len(graph)
        self.ok = True

        for i in range(len(graph)):
            if not self.visited[i]:
                self.helper(graph, i)
                if not self.ok:
                    break
        return self.ok
    
    def helper(self, graph, i):
        if not self.ok:
            return 

        self.visited[i] = 1
        for j in graph[i]:
            # If haven't visited this node, color this node and enter this node.
            if not self.visited[j]:
                self.color[j] = 1 - self.color[i]
                self.helper(graph, j)
            # If have visited this node, check its color.
            else:
                if self.color[j] == self.color[i]:
                    self.ok = False
                    return
