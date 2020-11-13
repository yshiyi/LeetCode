'''
36. Valid Sudoku
Hash Table

Description:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Similar Question:
Sudoku Solver - Hard
'''

# Solution:
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        '''
        Method: The basic idea is to look for the duplicates in each row, each column and each box.
                To increase the searching speed, we should use hash table (i.e., dictionary).
                At first, we create three lists, and each list contains nine empty dictionaries.
                We then move along the board. Check if the element has been seen before.
                If yes, return false. If no, we save this value to the corresponding lists.
                Return true, if there are no duplicates in the borad.
                It is tricky to determine the box index.
        '''
        
        # Initiate 3 lists, each list contains 9 dictionaries
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        # Starting from each row
        for i in range(9):
            # Sweep each column
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3 ) * 3 + j // 3
                    
                    if num not in rows[i] and num not in columns[j] and num not in boxes[box_index]:
                        rows[i][num] = i
                        columns[j][num] = j
                        boxes[box_index][num] = box_index
                    else:
                        return False
        
        return True


