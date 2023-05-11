"""
743M. Network Delay Time

Description:
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.


Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

"""
Method: Dijkstra. It is used to find a path that has minimum/maximum weight.
        There are a couple of steps to implement this method:
        1. Create a graph, each entry contains the index and weight.
        2. Use a heap queue to record the nodes.
        3. Use BFS to traverse all the nodes.
"""
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for edge in times:
            node1, node2, weight = edge[0]-1, edge[1]-1, edge[2]
            graph[node1].append((node2, weight))
        distTo = self.dijkstra(k-1, graph)
        print(distTo)
        ans = 0
        for dis in distTo:
            if dis == float('inf'):
                return -1
            ans = max(ans, dis)
        return ans
    
    def dijkstra(self, start, graph):
        # If we looking for the minimum weighted path, initial values are float('inf').
        dist_to = [float('inf')] * len(graph)
        dist_to[start] = 0

        q = []
        heapq.heapify(q)
        
        # We put the total weight in the front, so the top entry always has the minimum weight.
        heapq.heappush(q, (0, start))
        while len(q):
            cur_dist_from_start, cur_node_id = heapq.heappop(q)
            
            # If the distance is greater than the one recorded on the table, we proceed to the next one.
            if cur_dist_from_start > dist_to[cur_node_id]:
                continue
            
            for neighbor in graph[cur_node_id]:
                next_node_id = neighbor[0]
                dist_to_next_node = neighbor[1] + dist_to[cur_node_id]
                
                # If the new distance is less than the one recorded on the table, we update that entry.
                if dist_to[next_node_id] > dist_to_next_node:
                    dist_to[next_node_id] = dist_to_next_node
                    heapq.heappush(q, (dist_to_next_node, next_node_id))
        return dist_to

