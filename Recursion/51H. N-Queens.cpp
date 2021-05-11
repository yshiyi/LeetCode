/*
51H. N-Queens
Backtracking

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

Similar Questions:
N-Queens II - Hard
Grid Illumination - Hard
*/

/*
Method: Create a vector<string> to hold the layout of the board.
        Then we check the board row by row.
        In each row, we also check each column and also check if the cell is a valid position to place the queen.
        Once we place the queen, then we call the recursion to check the following rows.
        Once it is done, we take out the queen from the current cell and move to the next one.
*/
class Solution {
public:
    vector<vector<string>> res;
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        backtrack(board, 0);
        return res;
    }
    void backtrack(vector<string>& board, int row){
        if(row == board.size()){
            res.push_back(board);
            return;
        }
        int n = board.size();
        for(int col=0; col < n; col++){
            if(is_valid(board, row, col)){
                board[row][col] = 'Q';
                backtrack(board, row+1);
                board[row][col] = '.';
            }
        }
    }
    bool is_valid(vector<string>& board, int row, int col){
        // Check if there is queen in the same column
        for(int i=0; i<board.size(); i++){
            if(board[i][col]=='Q'){
                return false;
            }
        }
        // Check upper right side
        for(int i=row-1, j=col+1; i>=0 && j<board.size(); i--, j++){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        // Check upper left side
        for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
};
