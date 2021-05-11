class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.v_row = [[0]*10 for i in range(9)]
        self.v_col = [[0]*10 for i in range(9)]
        self.v_box = [[0]*10 for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    box_i = i//3*3 + j//3
                    n = int(board[i][j])
                    self.v_row[i][n] = 1
                    self.v_col[j][n] = 1
                    self.v_box[box_i][n] = 1
        
        def backtrack(board, row, col):
            if row == len(board):
                return True
            col_n = (col + 1) % 9
            if col_n == 0:
                row_n = row + 1
            else:
                row_n = row
            
            if board[row][col] != '.':
                return backtrack(board, row_n, col_n)
            
            for i in range(1, 10):
                box_id = row//3 * 3 + col//3
                n = int(i)
                if self.v_row[row][n]==0 and self.v_col[col][n]==0 and self.v_box[box_id][n]==0:
                    self.v_row[row][n] = 1
                    self.v_col[col][n] = 1
                    self.v_box[box_id][n] = 1
                    board[row][col] = chr(i+48)
                    if backtrack(board, row_n, col_n):
                        return True
                    board[row][col] = '.'
                    self.v_row[row][n] = 0
                    self.v_col[col][n] = 0
                    self.v_box[box_id][n] = 0
            return False
        
        backtrack(board, 0, 0)
                
