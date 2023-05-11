"""
1631M. Path With Minimum Effort

Description:
You are a hiker preparing for an upcoming hike. 
You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). 
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). 
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.


Example 1:
Input: heights = [[1,2,2],
                  [3,8,2],
                  [5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],
                  [3,8,4],
                  [5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],
                  [1,2,1,2,1],
                  [1,2,1,2,1],
                  [1,2,1,2,1],
                  [1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""

"""
Method: Use Dijkstra.
        We flat the matrix to create a graph.
        At each cell, instead of summing up the total weight, we record the max, max(neighbor[1], dist_from_start).
"""
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        row, col = len(heights), len(heights[0])
        graph = [[] for _ in range(row*col)]
        for i in range(row):
            for j in range(col):
                for dir in dirs:
                    newX, newY = i+dir[0], j+dir[1]
                    if newX>=0 and newY>=0 and newX<row and newY<col:
                        cur_cell = i*col+j
                        next_cell = newX*col+newY
                        dis = abs(heights[i][j] - heights[newX][newY])
                        graph[cur_cell].append((next_cell, dis))
        
        dist_to = self.helper(0, graph)
        return dist_to[-1]
    
    def helper(self, start, graph):
        dist_to = [float('inf') for _ in range(len(graph))]
        dist_to[start] = 0

        q = []
        heapq.heapify(q)
        heapq.heappush(q, (0, start))
        while len(q):
            dist_from_start, cur_id = heapq.heappop(q)
            if dist_from_start > dist_to[cur_id]:
                continue
            for neighbor in graph[cur_id]:
                next_id = neighbor[0]
                dist_to_next_id = max(neighbor[1], dist_from_start)
                if dist_to_next_id < dist_to[next_id]:
                    dist_to[next_id] = dist_to_next_id
                    heapq.heappush(q, (dist_to_next_id, next_id))
        return dist_to
