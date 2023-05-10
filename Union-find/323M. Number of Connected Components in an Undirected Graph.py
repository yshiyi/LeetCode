"""
323M. Number of Connected Components in an Undirected Graph

Description:
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2

Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output: 1

Note: You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""


class UF(object):
     def __init__(self, n):
        # Count represents the number of groups.
        self.count = n
        # Record the parent node, or where the adjacent node.
        self.parent = [i for i in range(n)]
        # Record the number of child node. The root node has one child which is itself.
        self.size = [1] * n
     
     def find(self, p):
          while p != self.parent[p]:
               # Reduce the height of the tree. Optimize the time complexity of find() operation.
               self.parent[p] = self.parent[self.parent[p]]
               p = self.parent[p]
          return p 
     
     def union(self, p, q):
          rootP, rootQ = self.find(p), self.find(q)
          if rootP == rootQ:
               return
          # Maintain the balance of the tree. 
          if self.size[rootP] < self.size[rootQ]:
               self.parent[rootP] = rootQ
               self.size[rootQ] += self.size[rootP]
          else:
               self.parent[rootQ] = rootP
               self.parent[rootP] += self.parent[rootQ]
          self.count -= 1

class Solution(UF):
     def countComponents(self, n, edges):
          super(Solution, self).__init__(n)
          uf = UF(n)
          for edge in edges:
               uf.union(edge[0], edge[1])
          return uf.count

n = 5
edges = [[0, 1], [1, 2], [3, 4]]
obj = Solution(n)
print(obj.countComponents(n, edges))
          
n = 5 
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
obj = Solution(n)
print(obj.countComponents(n, edges))
