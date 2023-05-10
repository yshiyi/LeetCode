"""
261M. Graph Valid Tree

Description:
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges 
where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
Return true if the edges of the given graph make up a valid tree, and false otherwise.
 

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
 

Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""

"""
Method: Use union-find method to connect all the nodes and check if there is a loop in the tree.
        If two nodes have the same root, then there is a loop. 
        2 and 3 have the same root. If there is an edge between them, there is a loop.
            1
          /   \
         2  -  3
        If two nodes have different root, there is no loop.
        2's root is 1 and 3's root is 3 itself. They can be connected.
            1
          /   
         2     3
"""

class UF(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    
    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, p, q):
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.count -= 1
        
    def connect(self, p, q):
        return self.find(p) == self.find(q)

class Solution(UF):
    def validTree(self, n, edges):
        # super().__init__(n)
        uf = UF(n)
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            if uf.connect(node1, node2):
                return False
            else:
                uf.union(node1, node2)
        return uf.count == 1


n = 5 
edges = [[0,1],[0,2],[0,3],[1,4]]
obj = Solution(n)
print(obj.validTree(n, edges))

n = 5 
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
obj = Solution(n)
print(obj.validTree(n, edges))
