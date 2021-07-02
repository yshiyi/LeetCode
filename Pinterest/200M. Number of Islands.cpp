/*
200M. Number of Islands
BFS, DFS

Description:
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.


Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Similar Questions:
Surrounded Regions - Medium
Walls and Gates - Medium
Number of Islands II - Hard
Number of Connected Components in an Undirected Graph - Medium
Number of Distinct Islands - Medium
Max Area of Island - Medium
Count Sub Islands - Medium
*/

/*
Method: BFS
        Linearly scan the 2D grid map.
        If a node contains a '1' and it is not visited, then triggers a BFS.
        Put it into a queue and mark it as visited. Then iteratively search its neighbors until the queue becomes empty.
        
        Time complexity: O(mn), where m and n are the size of the grid map
        Space complexity: O(min(m,n)), the worst case is then the grid map is filled with '1'.
*/
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> visited(m, vector<int>(n, 0));
        vector<vector<int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        
        int res = 0;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                // If this cell is '0' or it is visited, then continue.
                if(grid[i][j]=='0'||visited[i][j]){continue;}
                // Otherwise, there is a new island.
                ++res;
                // We save the x and y coordinate in the queue.
                queue<pair<int,int>> q;
                q.push(make_pair(i, j));
                while(q.size()){
                    auto p = q.front(); q.pop();
                    for(auto d:dirs){
                        int x = p.first + d[0], y = p.second + d[1];
                        // Check if the new cell satisfies all constraints
                        if(x<0 || x>=m || y<0 || y>=n || visited[x][y] ||grid[x][y]=='0'){continue;}
                        visited[x][y] = 1;
                        q.push(make_pair(x, y));
                    }
                }
            }
        }
        return res;
    }
};
