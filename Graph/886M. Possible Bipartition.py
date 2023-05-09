"""
886M. Possible Bipartition.py

Description:
We want to split a group of n people (labeled from 1 to n) into two groups of any size. 
Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person 
labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.

Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= ai < bi <= n
All the pairs of dislikes are unique.
"""

"""
Method: Create the graph first!
"""
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = self.buildGraph(n, dislikes)
        self.ok = True
        self.visited = [0] * n
        self.color = [0] * n

        for i in range(n):
            if not self.visited[i]:
                self.helper(graph, i)
                if not self.ok:
                    return False
        return self.ok

    
    def buildGraph(self, n, dislikes):
        graph = [[] for _ in range(n)]
        for pair in dislikes:
            p1, p2 = pair[0], pair[1]
            graph[p1-1].append(p2-1)
            graph[p2-1].append(p1-1)
        return graph
    
    def helper(self, graph, i):
        if not self.ok:
            return
        self.visited[i] = 1
        for j in graph[i]:
            if not self.visited[j]:
                self.color[j] = 1 - self.color[i]
                self.helper(graph, j)
            else:
                if self.color[i] == self.color[j]:
                    self.ok = False
                    return
