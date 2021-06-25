/*
79M. Word Search

Description:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
 

Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 
       word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 
       word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 
       word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
*/

/*
Method: 
*/
/*
Method: Backtracking
        Create a boolean table to track the path, if a cell has been visited, put 1. Otherwise is 0.
        In the main function, we need to traverse all the elements 
        and treat each of them as the start char in the search.
        
        In the search function, if the value of count is equal to word.size(), then we return true.
        For each cell, we need to check if it is in the board, ifit has been visited 
        and if it is on the correct position in the word.
*/

class Solution {
public:
    // vector<vector<int>> dir={{0,1}, {1,0}, {0,-1}, {-1,0}};
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<int>> visit(board.size(), vector<int>(board[0].size(), 0));
        for(int i=0; i<board.size(); ++i){
            for(int j=0; j<board[0].size(); ++j){
                if(search(board, visit, word, i, j, 0)){
                    return true;
                }
            }
        }
        return false;
    }
    
    bool search(vector<vector<char>> &board, vector<vector<int>> &visit, string &word, int row, int col, int count){
        
        if(count==word.size()){return true;}
        
        if(row<0 || row>=board.size() || col<0 || col>=board[0].size() 
           || visit[row][col] || board[row][col]!=word[count]){
            return false;
        }
        visit[row][col] = 1;
        // This approach will exceed time limitation.
        // bool res = false;
        // for(auto move:dir){
        //     int new_row = row + move[0];
        //     int new_col = col + move[1];
        //     res = res || search(board, visit, word, new_row, new_col, count+1);
        // }
        bool res = search(board, visit, word, row, col+1, count+1) 
                 || search(board, visit, word, row+1, col, count+1)
                 || search(board, visit, word, row, col-1, count+1)
                 || search(board, visit, word, row-1, col, count+1);
        visit[row][col] = 0;
        return res;
    }
};

