/*
63M. Unique Paths II

Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.
 

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.

Similar Questions:
Unique Paths - Medium
Unique Paths III - Hard
*/

/*
Method: Similar to 62M. Unique Paths
        There are a couple of things we need to notice:
        1. When we fill in the last row and the last column, 
           if there is an obstacle, then the value in all the cell on its left or that in those above it should be 0.
           Because there is only one path along the last row or the last column. 
           If there is an obstacle, then there is no way to reach the target.
        2. For the final calculation, 
           if there is an obstacle in the cell, then the # of paths in that cell is 0.
*/
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int row = obstacleGrid.size(), col = obstacleGrid[0].size();
        if(obstacleGrid[row-1][col-1]){
            return 0;
        }
        
        vector<vector<long>> opt(row, vector<long>(col, 0));
        // Fill in the last row
        for(int i=col-1; i>=0; --i){
            if(!obstacleGrid[row-1][i]){
                opt[row-1][i] = 1;
            }else{
                for(int j=i; j>=0; --j){
                    opt[row-1][j] = 0;
                }
                break;
            }
        }
        
        // Fill in the last col
        for(int i=row-1; i>=0; --i){
            if(!obstacleGrid[i][col-1]){
                opt[i][col-1] = 1;
            }else{
                for(int j=i; j>=0; --j){
                    opt[j][col-1] = 0;
                }
                break;
            }
        }
        
        // Start the calculation from grid[row-2][col-2]
        for(int i=row-2; i>=0; --i){
            for(int j=col-2; j>=0; --j){
                if(obstacleGrid[i][j]){
                    opt[i][j] = 0;
                }else{
                    opt[i][j] = opt[i][j+1] + opt[i+1][j];
                }
            }
        }
        return opt[0][0];
    }
};
