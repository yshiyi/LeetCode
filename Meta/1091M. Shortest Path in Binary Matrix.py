"""
1091. Shortest Path in Binary Matrix

Description:
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) 
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected 
(i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:
0 1
1 0
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
0 0 0
1 1 0
1 1 0
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
1 0 0
1 1 0
1 1 0
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""


# Solution:
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0]==1:
            return -1
        n = len(grid)
        step = 1
        q = collections.deque()
        q.append((0, 0))
        visited = set()
        visited.add((0, 0))
        dirs = [[0, 1], [1, 1], [1, 0], [1, -1],
                [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        while len(q):
            size = len(q)
            for _ in range(size):
                curx, cury = q.popleft()
                if curx==n-1 and cury==n-1:
                    return step
                for d in dirs:
                    newx = curx + d[0]
                    newy = cury + d[1]
                    if newx<0 or newx>=n or newy<0 or newy>=n or (newx, newy) in visited or grid[newx][newy]==1:
                        continue
                    visited.add((newx, newy))
                    q.append((newx, newy))
            step += 1
        return -1
