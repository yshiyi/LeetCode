"""
1020. Number of Enclaves

Description:
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell 
or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:
Input: grid = [[0,0,0,0],
               [1,0,1,0],
               [0,1,1,0],
               [0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.


Example 2:
Input: grid = [[0,1,1,0], 
               [0,0,1,0],
               [0,0,1,0],
               [0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""


# Solution:
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        self.res = 0
        self.dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(c):
            if grid[0][i]==1:
                self.helper(grid, 0, i, r, c, 0)
            if grid[r-1][i]==1:
                self.helper(grid, r-1, i, r, c, 0)
        for i in range(r):
            if grid[i][0]==1:
                self.helper(grid, i, 0, r, c, 0)
            if grid[i][c-1]==1:
                self.helper(grid, i, c-1, r, c, 0)
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    self.helper(grid, i, j, r, c, 1)
        return self.res
    
    def helper(self, grid, i, j, r, c, count):
        q = collections.deque()
        q.append((i, j))
        grid[i][j]=0
        while len(q):
            if count:
                self.res += 1
            x, y = q.popleft()
            for d in self.dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x<0 or new_x>=r or new_y<0 or new_y>=c or grid[new_x][new_y]==0:
                    continue
                grid[new_x][new_y]=0
                q.append((new_x, new_y))
