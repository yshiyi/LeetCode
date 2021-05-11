/*

Hash Table, Backtracking

Description:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
*/

/*
Solution: The backtracking function needs to return a boolean value so as to determine if the solution is correct.
          1. The base case is when we reach to the end of the board (i.e., row==board.size()).
             This means we have obtained a valid solution, then return true.
          2. Check if the current cell has been filled. If so, move to next cell.
          3. If the current cell is empty, we try to fill in with number 1 - 9.
             After filling in each number, we check the next cell via the recursion function.
*/

// Method 1: Using vector<set<char>>, runtime is about 60 - 76 ms.
class Solution {
public:
    vector<set<char>> v_row, v_col, v_box; 
    void solveSudoku(vector<vector<char>>& board) {
        v_row.resize(9);
        v_col.resize(9);
        v_box.resize(9);
        for(int i=0; i<board.size();i++){
            for(int j=0; j<board[0].size(); j++){
                if(board[i][j]!='.'){
                    int box_index = i/3 * 3 + j/3;
                    // int num = board[i][j] - '0';
                    char num = board[i][j];
                    v_row[i].insert(num);
                    v_col[j].insert(num);
                    v_box[box_index].insert(num);
                }
            }
        }
        backtrack(board, 0, 0);
    }
    bool backtrack(vector<vector<char>>& board, int row, int col){
        if(row==board.size()){
            return true;
        }
        
        // Get the next column number, which varies between 0 - 8
        int col_n = (col + 1) % 9;
        // When col == 0, it means we move to the next row. Then we increase row by 1.
        int row_n = (col_n==0) ? row+1 : row;
        if(board[row][col]!='.'){
            return backtrack(board, row_n, col_n);
        }
        
        for(char i='1'; i<='9'; i++){
            int box_index = row/3*3+col/3;
            if(v_row[row].find(i)==v_row[row].end() && v_col[col].find(i)==v_col[col].end() && v_box[box_index].find(i)==v_box[box_index].end()){
                v_row[row].insert(i);
                v_col[col].insert(i);
                v_box[box_index].insert(i);
                board[row][col] = i;
                if(backtrack(board, row_n, col_n)){
                    return true;
                }
                board[row][col] = '.';
                v_box[box_index].erase(i);
                v_col[col].erase(i);
                v_row[row].erase(i);
            }
        }
        return false;
    }    
};


/* 
Method 2: Using vector<vector<int>>, positions represent the value. 0 means not appeared, and 1 means appeared.
          Runtime is about 3 - 4 ms.
*/
class Solution {
public:
    vector<vector<int>> v_row, v_col, v_box; 
    void solveSudoku(vector<vector<char>>& board) {
        // The size of each sub-vector is 10, because it includes 0 - 9.
        v_row = vector<vector<int>>(9, vector<int>(10));
        v_col = vector<vector<int>>(9, vector<int>(10));
        v_box = vector<vector<int>>(9, vector<int>(10));
        for(int i=0; i<board.size();i++){
            for(int j=0; j<board[0].size(); j++){
                if(board[i][j]!='.'){
                    int box_index = i/3 * 3 + j/3;
                    int num = board[i][j] - '0';
                    v_row[i][num] = 1;
                    v_col[j][num] = 1;
                    v_box[box_index][num] = 1;
                }
            }
        }
        backtrack(board, 0, 0);
    }
    bool backtrack(vector<vector<char>>& board, int row, int col){
        if(row==board.size()){
            return true;
        }
        
        int col_n = (col + 1) % 9;
        int row_n = (col_n==0) ? row+1 : row;
        if(board[row][col]!='.'){
            return backtrack(board, row_n, col_n);
        }
        
        for(char i='1'; i<='9'; i++){
            int box_index = row/3*3+col/3;
            int num = i - '0';
            if(v_row[row][num]==0 && v_col[col][num]==0 && v_box[box_index][num]==0){
                v_row[row][num] = 1;
                v_col[col][num] = 1;
                v_box[box_index][num] = 1;
                board[row][col] = i;
                if(backtrack(board, row_n, col_n)){
                    return true;
                }
                board[row][col] = '.';
                v_row[row][num] = 0;
                v_col[col][num] = 0;
                v_box[box_index][num] = 0;
            }
        }
        return false;
    }    
};





