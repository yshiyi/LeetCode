"""
130M. Surrounded Regions

Description:
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""

"""
Method: Same as 1254. Number of Closed Islands.
        In this question, we need to record the coordinates of the islands that are on the boundary.
        At the end of the code, we need to flip those cells from 'X' back to 'O'.
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, col = len(board), len(board[0])
        self.boundary = []
        for i in range(row):
            if board[i][0] == 'O':
                self.helper(board, i, 0, 1)
            if board[i][col-1] == 'O':
                self.helper(board, i, col-1, 1)

        for j in range(col):
            if board[0][j] == 'O':
                self.helper(board, 0, j, 1)
            if board[row-1][j] == 'O':
                self.helper(board, row-1, j, 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    self.helper(board, i, j, 0)

        for pos in self.boundary:
            board[pos[0]][pos[1]] = 'O'

        return
    
    def helper(self, board, i, j, boundary):
        q = collections.deque()
        q.append((i, j))
        board[i][j] = 'X'
        while len(q):
            x, y = q.popleft()
            if boundary:
                self.boundary.append((x, y))
            for dir in self.dirs:
                newX, newY = x + dir[0], y + dir[1]
                if newX>0 and newY>0 and newX<len(board) and newY<len(board[0]) and board[newX][newY] == 'O':
                    board[newX][newY] = 'X'
                    q.append((newX, newY))
