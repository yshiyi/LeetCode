"""
1135. Connecting Cities With Minimum Cost

Description:
There are n cities labeled from 1 to n. You are given the integer n and an array connections 
where connections[i] = [xi, yi, costi] indicates that the cost of connecting 
city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. 
If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.


Example 1:
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:
Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.
 

Constraints:
1 <= n <= 104
1 <= connections.length <= 104
connections[i].length == 3
1 <= xi, yi <= n
xi != yi
0 <= costi <= 105
"""

"""
Method: This approach is called Kruskal for solving for the Minimum Spanning Tree problems.
        This approach consists of two steps.
        1. Use union-find to check the connection between two nodes and if there is a loop, and to union two nodes.
        2. Use greedy method to add two nodes that have minimum cost first.
        Note, to use sort() with custom function.
        
        nums.sort(key=func)
        # In this case, nums will be sorted using the third element.
        def func(num):
            return num[2]
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
    def minCost(self, n, connections):
        uf = UF(n)
        connections.sort(key=self.cost)
        min_cost = 0
        for edge in connections:
            node1, node2 = edge[0]-1, edge[1]-1
            if uf.connect(node1, node2):
                continue
            min_cost += edge[2]
            uf.union(node1, node2)
        return min_cost if uf.count==1 else -1

    @staticmethod
    def cost(edge):
        return edge[2]


n = 3 
connections = [[1,2,5],[1,3,6],[2,3,1]]
obj = Solution(n)
print(obj.minCost(n, connections))

n = 4 
connections = [[1,2,3],[3,4,4]]
obj = Solution(n)
print(obj.minCost(n, connections))
