class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        board = [list('.'*n) for i in range(n)]
        def isValid(board, row, col):
            for i in range(len(board)):
                if board[i][col]=='Q':
                    return False
            i, j = row-1, col+1
            while i>=0 and j<len(board):
                if board[i][j]=='Q':
                    return False
                i -= 1
                j += 1
            i, j = row-1, col-1
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i -= 1
                j -= 1
            return True
        
        def backtrack(board, row):
            if row == len(board):
                self.res += 1
                return
            for col in range(len(board[0])):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        
        backtrack(board, 0)
        return self.res
