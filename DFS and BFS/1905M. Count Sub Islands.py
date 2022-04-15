"""
1905. Count Sub Islands

Description:
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) 
and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). 
Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells 
that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.
 

Example 1:
Input: grid1 = [[1,1,1,0,0],
                [0,1,1,1,1],
                [0,0,0,0,0],
                [1,0,0,0,0],
                [1,1,0,1,1]], 
       grid2 = [[1,1,1,0,0],
                [0,0,1,1,1],
                [0,1,0,0,0],
                [1,0,1,1,0],
                [0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.


Example 2:
Input: grid1 = [[1,0,1,0,1],
                [1,1,1,1,1],
                [0,0,0,0,0],
                [1,1,1,1,1],
                [1,0,1,0,1]], 
       grid2 = [[0,0,0,0,0],
                [1,1,1,1,1],
                [0,1,0,1,0],
                [0,1,0,1,0],
                [1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:
m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""


# Solution:
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        r, c = len(grid1), len(grid1[0])
        for i in range(r):
            for j in range(c):
                if grid1[i][j]==0 and grid2[i][j]==1:
                    self.helper(grid2, i, j, r, c)
        
        res = 0
        for i in range(r):
            for j in range(c):
                if grid2[i][j]==0:
                    continue
                res += 1
                self.helper(grid2, i, j, r, c)
                
        return res
    
    def helper(self, grid, i, j, r, c):
        q = collections.deque()
        q.append((i, j))
        grid[i][j]=0
        while len(q):
            x, y = q.popleft()
            for dir in self.dirs:
                new_x = x + dir[0]
                new_y = y + dir[1]
                if new_x<0 or new_x>=r or new_y<0 or new_y>=c or grid[new_x][new_y]==0:
                    continue
                grid[new_x][new_y]=0
                q.append((new_x, new_y))
