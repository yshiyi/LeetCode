"""
1584M. Min Cost to Connect All Points.py

Description:
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""

"""
Method: Use Kruskal approach.
        In this problem, we need to convert all points to edges first.
        We can use the index of each point in the list to represent them.
"""
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        class UF():
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

        edges = []
        for i in range(len(points)):
            for j in range(1, len(points)):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]
                edges.append((i, j, abs(xi-xj)+abs(yi-yj)))
        uf = UF(len(edges))
        edges.sort(key=self.func)
        min_cost = 0
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            if uf.connect(node1, node2):
                continue
            min_cost += edge[2]
            uf.union(node1, node2)
        return min_cost
    
    @staticmethod
    def func(num):
        return num[2]


