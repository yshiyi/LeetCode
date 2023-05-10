"""
547M. Number of Provinces.py

Description:
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, 
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

"""
Method: When we see the inputs include edges, and we need to consider the connections between nodes, we should consider using union-find method.
"""
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        class UF():
            def __init__(self, n):
                self.parent = [i for i in range(n)]
                self.size = [1] * n
                self.count = n
            
            def find(self, p):
                while p!=self.parent[p]:
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
        
        uf = UF(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected)):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count

