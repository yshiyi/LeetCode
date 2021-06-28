/*
529M. Minesweeper

Description:
Let's play the minesweeper game!
You are given an m x n char matrix board representing the game board where:

1. 'M' represents an unrevealed mine,
2. 'E' represents an unrevealed empty square,
3. 'B' represents a revealed blank square that has no adjacent mines 
   (i.e., above, below, left, right, and all 4 diagonals),
4. digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
5. 'X' represents a revealed mine.

You are also given an integer array click where click = [clickr, clickc] represents the next click position 
among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

1. If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
2. If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' 
   and all of its adjacent unrevealed squares should be revealed recursively.
3. If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') 
   representing the number of adjacent mines.
4. Return the board when no more squares will be revealed.
 

Example 1:


Input: board = [["E","E","E","E","E"],
                ["E","E","M","E","E"],
                ["E","E","E","E","E"],
                ["E","E","E","E","E"]], 
       click = [3,0]
Output: [["B","1","E","1","B"],
         ["B","1","M","1","B"],
         ["B","1","1","1","B"],
         ["B","B","B","B","B"]]


Example 2:
Input: board = [["B","1","E","1","B"],
                ["B","1","M","1","B"],
                ["B","1","1","1","B"],
                ["B","B","B","B","B"]], 
       click = [1,2]
Output: [["B","1","E","1","B"],
         ["B","1","X","1","B"],
         ["B","1","1","1","B"],
         ["B","B","B","B","B"]]
 

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.
*/

/*
Method: BFS
        Create a queue to save the coordinate of the cells.
        Check the cell itself and its neighbors. If any of its neighbors is not mine, then put it into the queue.
*/
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        // If the click cell is a mine, then mark it as 'X' and return the board.
        if(board[click[0]][click[1]]=='M'){
            board[click[0]][click[1]] = 'X';
            return board;
        }
        
        int m = board.size(), n = board[0].size();
        
        // Create a queue to hold all the cells that are not mine.
        queue<pair<int, int>> q;
        q.push(make_pair(click[0], click[1]));
        while(!q.empty()){
            // This is the center cell.
            auto cell = q.front(); q.pop();
            int row = cell.first, col = cell.second;
            int mines = 0;
            
            // Create an array to hold all the neighbors of the center cell that are not mine.
            vector<pair<int, int>> empty_neighbor;
            
            // Iterate all the neighbors of the center cell and itself
            for(int i=-1; i<2; ++i){
                for(int j=-1; j<2; ++j){
                    int new_row = row + i, new_col = col + j;
                    if(new_row<0 || new_row>=m || new_col<0 || new_col>=n){
                        continue;
                    }
                    
                    // If there is a mine in the neighbors, count the number.
                    // If the neighbor is not a mine, put it the empty_neighbor. We wil check it in the next iteration.
                    if(board[new_row][new_col]=='M'){++mines;}
                    else if(board[new_row][new_col]=='E'){
                        empty_neighbor.push_back(make_pair(new_row, new_col));
                    }
                }
            }
            
            // As the rules of the game, if there are mines around the center cell, 
            // we simply mark the cell as the number of mines.
            if(mines){
                board[row][col] = mines + '0';
            }else{
                // If the center cell is empty, in other words, there are no mines around.
                // We can then puch all the empty neighbors into the queue and check them in the next iteration.
                for(auto neighbor:empty_neighbor){
                    board[neighbor.first][neighbor.second] = 'B';
                    q.push(neighbor);
                }
            }
        }
        
        return board;
    }
};
