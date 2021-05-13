/*
489H. Robot Room Cleaner

Description:
Given a robot cleaner in a room modeled as a grid.
Each cell in the grid can be empty or blocked.
The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.
When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.
Design an algorithm to clean the entire room using only the 4 given APIs shown below.

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}


Example:
Input:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3
Explanation:
All grids in the room are marked by either 0 or 1.
0 means the cell is blocked, while 1 means the cell is accessible.
The robot initially starts at the position of row=1, col=3.
From the top left corner, its position is one row below and three columns right.

Notes:
The input is only given to initialize the room and the robot’s position internally. 
You must solve this problem “blindfolded”. 
In other words, you must control the robot using only the mentioned 4 APIs, 
without knowing the room layout and the initial robot’s position.
The robot’s initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
*/


/*
Solution: As usual, three things need to be concerned.
          1. The base case. In this case, we don't have the map, so we don't have any ending condition.
          2. The path. We need to mark the cell as visited when the robot passes by.
          3. Create four directions. For each direction, we try to move the robot.
             If the next cell has been visited or it is blocked/boundary, we try the next direction.
          Note: we need to move the robot back to the previous position after backtracking.
*/
class Solution {
public:
    // Define movements in four different directions: left, up, right and down
    // -1, 0, 1 represent the changes in the row or column
    vector<vector<int>> dirs{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    void cleanRoom(Robot& robot) {
        // Define a set to record the cells that are visited
        unordered_set<string> visited;
        backtrack(robot, 0, 0, 0, visited);
    }
    void backtrack(Robot& robot, int x, int y, int dir, unordered_set<string>& visited) {
        // When enter a cell, the robot cleans it
        robot.clean();
        // Record this cell and mark it as cleaned
        visited.insert(to_string(x) + "-" + to_string(y));
        // Try different four directions
        for (int i = 0; i < 4; ++i) {
            // This is a tricky part. The current the direction is the direction of the movement from the last cell.
            // In this solution, i=0 represent the current direction.
            int cur = (i + dir) % 4, newX = x + dirs[cur][0], newY = y + dirs[cur][1];
            
            // Use .count() to check if we have visited this cell
            // Use robot.move() to check if the next is open or an obstacle.
            if (!visited.count(to_string(newX) + "-" + to_string(newY)) && robot.move()) {
                backtrack(robot, newX, newY, cur, visited);
              
                // The following lines of command make the robot move back the last cell.
                robot.turnRight();
                robot.turnRight();
                robot.move();
                robot.turnLeft();
                robot.turnLeft();
            }
            // If the next cell has been visited or is an obstacle, the robot simply turns right and trys next direction.
            robot.turnRight();
        }
    }
};
