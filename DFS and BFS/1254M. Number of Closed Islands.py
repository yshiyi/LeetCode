"""
1254. Number of Closed Islands

Description:
Given a 2D grid consists of 0s (land) and 1s (water).  
An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally 
(all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.
 

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],
               [1,0,0,0,0,1,1,0],
               [1,0,1,0,1,1,1,0],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],
               [0,1,0,1,0],
               [0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""

# Solution:
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_res = 0
        b_res = 0
        r, c = len(grid), len(grid[0])
        self.dirs = [[0,1], [0,-1], [1,0],[-1,0]]
        
        # Count the islands on the top and bottom boundaries
        for i in range(c):
            if grid[0][i]==0:
                b_res += 1
                self.helper(grid, 0, i, r, c)
    
            if grid[r-1][i]==0:
                b_res += 1
                self.helper(grid, r-1, i, r, c)

        # Count the islands on the left and right boundaries
        for i in range(r):
            if grid[i][0]==0:
                b_res += 1
                self.helper(grid, i, 0, r, c)
            
            if grid[i][c-1]==0:
                b_res += 1
                self.helper(grid, i, c-1, r, c)

        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    continue
                total_res += 1
                self.helper(grid, i, j, r, c)
        return total_res
                    
    
    def helper(self, grid, oldx, oldy, r, c):
        q = collections.deque()
        q.append((oldx, oldy))
        # change the visited cell to 1
        grid[oldx][oldy]=1
        while len(q):
            x, y = q.popleft()
            for d in self.dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x<0 or new_x>=r or new_y<0 or new_y>=c or grid[new_x][new_y]==1:
                    continue
                # change the visited cell to 1
                grid[new_x][new_y]=1
                q.append((new_x, new_y))
                
                
