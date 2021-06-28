/*
1293H. Shortest Path in a Grid with Obstacles Elimination

Decription:
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). 
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) 
given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.


Example 1:
Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. 
Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:
Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.


Constraints:
grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0

Similar Question:
Shortest Path to Get Food - Medium
*/

/*
Method: BFS
        This is a typical question to apply BFS.
        We need to create an extra array to record the value of k.
        The larger k the cell has, the more possible that cell is on the optimal path.
        In other words, if we have a larger k, then we have more options to eliminate obstacles in the future.
        Time complexity: O(m*n*k)
        Space complexity: O(m*n*k)
*/
class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) {
        int row = grid.size(), col = grid[0].size();
        // These are four possible directions to move.
        vector<vector<int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        // This 2D array is to record the value of remaining k in each cell. 
        vector<vector<int>> seen(row, vector<int>(col, -1));
        // There are three elements in the queue, row, col and value of remaining k.
        queue<vector<int>> q;
        q.push({0, 0, k});
        int steps=0;
        while(!q.empty()){
            int s = q.size();
            while(s!=0){
                auto cell = q.front(); q.pop();
                int cr = cell[0], cc = cell[1], co = cell[2];
                // If we reach the bottom right corner, then return steps.
                if(cr==row-1 && cc==col-1){return steps;}
                for(int i=0; i<dirs.size(); ++i){
                    int nr = cr + dirs[i][0];
                    int nc = cc + dirs[i][1];
                    // Check if the next step is out of the board.
                    if(nr<0 || nr>=row || nc<0 || nc>=col){continue;}
                    int no = co - grid[nr][nc];
                    // Compare the new k with the previous k.
                    // The larger k, the better
                    if(no <= seen[nr][nc] || no < 0){continue;}
                    // Record the new k
                    seen[nr][nc] = no;
                    q.push({nr, nc, no});
                }
                --s;
            }
            ++steps;
        }
        return -1;
    }
};
