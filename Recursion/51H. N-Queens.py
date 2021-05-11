'''
Method:
1. Create a board. board = [list('.'*n) for i in range(n)]
   Note: we convert a string to a list, because the string doesn't support item assignment in Python.
2. Save a valid solution.
   Res = []
   for r in board:
       Res.append(''.join(deepcopy(r)))
   res.append(Res)
   Note: need to first deepcopy the result, otherwise it will be kept modifying the element values
         also need to convert the list back to the string. Using ''.join(list).
'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
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
                Res = []
                for r in board:
                    Res.append(''.join(deepcopy(r)))
                res.append(Res)
                return
            for col in range(len(board[0])):
                if isValid(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'
        
        backtrack(board, 0)
        return res
