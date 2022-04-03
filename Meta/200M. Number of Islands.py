"""
200. Number of Islands

Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
 

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

# Solution:
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        visited = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='0' or (i, j) in visited:
                    continue
                res += 1
                q = collections.deque()
                q.append((i, j))
                while len(q):
                    x, y = q.popleft()
                    for dir in dirs:
                        new_x = x + dir[0]
                        new_y = y + dir[1]
                        if new_x<0 or new_x>=r or new_y<0 or new_y>=c or grid[new_x][new_y]=='0' or (new_x, new_y) in visited:
                            continue
                        q.append((new_x, new_y))
                        visited.add((new_x, new_y))
        return res
