"""
694. Number of Distinct Islands
Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Count the number of distinct islands. 
An island is considered to be the same as another if and only if one island can be translated 
(and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3

Constraints:
Note: The length of each dimension in the given grid does not exceed 50.
"""

"""
Method: We need a set to record all the island.
        The problem is how we represent each island.
        The answer is to encode each island with the direction of each movement associated with it.
        Don't forget to record the direction of the backward.
"""
class Solution(object):
    def numDistinctIslands(self, grid):
        self.dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.r, self.c = len(grid), len(grid[0])
        ans = set()
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 1:
                    self.island = ''
                    self.helper(grid, i, j, 6)
                    ans.add(self.island)
        return len(ans)
    
    def helper(self, grid, i, j, d):
        if i<0 or j<0 or i>=self.r or j>=self.c or grid[i][j]==0:
            return
        self.island += str(d)
        grid[i][j] = 0
        for idx, dir in enumerate(self.dirs):
            newX, newY = i+dir[0], j+dir[1]
            self.helper(grid, newX, newY, idx)
        self.island += str(-d)
        


grid = [[1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1]]
obj = Solution()
print(obj.numDistinctIslands(grid))

