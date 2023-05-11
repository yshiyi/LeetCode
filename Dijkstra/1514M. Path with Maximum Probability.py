"""
1514M. Path with Maximum Probability

Description:
You are given an undirected weighted graph of n nodes (0-indexed), 
represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability 
of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end 
and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 

Constraints:
2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""

"""
Method: Use Dijkstra.
        As this is an undirected weight map, we need to record both node when creating the graph.
        Since we looking for the maximum weighted path, we need to initialize prob_to with float('-inf').
        To keep the node with maximum probability on the top of heap, we need to save -prob.
"""
class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            node1, node2 = edges[i][0], edges[i][1]
            prob = succProb[i]
            graph[node1].append((node2, prob))
            graph[node2].append((node1, prob))
        prob_to = self.helper(start, graph)
        print(graph)
        print(prob_to)
        return prob_to[end] if prob_to[end]!=float('-inf') else 0
    
    def helper(self, start, graph):
        prob_to = [float('-inf') for _ in range(len(graph))]
        prob_to[start] = 1.0

        q = []
        heapq.heapify(q)
        heapq.heappush(q, (-1.0, start))
        while len(q):
            prob_from_start, cur_id = heapq.heappop(q)
            prob_from_start *= -1
            if prob_from_start < prob_to[cur_id]:
                continue
            for neighbor in graph[cur_id]:
                next_id = neighbor[0]
                prob_to_next_id = neighbor[1] * prob_from_start
                if prob_to_next_id > prob_to[next_id]:
                    prob_to[next_id] = prob_to_next_id
                    heapq.heappush(q, (-prob_to_next_id, next_id))
        return prob_to
