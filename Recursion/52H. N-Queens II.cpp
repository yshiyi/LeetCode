/*
52H. N-Queens II
Backtracking

Description:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9

Similar Question:
N-Queens - Hard
*/

// Method: similar to 50H. N-Queens
class Solution {
public:
    int res=0;
    int totalNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        backtrack(board, 0);
        return res;
    }
    void backtrack(vector<string>& board, int row){
        if(row==board.size()){
            ++res;
            return;
        }
        for(int col=0; col<board[0].size(); col++){
            if(isValid(board, row, col)){
                board[row][col] = 'Q';
                backtrack(board, row+1);
                board[row][col] = '.';
            }
        }
    }
    bool isValid(vector<string>& board, int row, int col){
        for(int i=0; i<board.size(); i++){
            if(board[i][col]=='Q'){
                return false;
            }
        }
        for(int i=row-1, j=col+1; i>=0 && j<board.size(); i--, j++){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        for(int i=row-1, j=col-1; i>=0 && j>=0; i--, j--){
            if(board[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
};
