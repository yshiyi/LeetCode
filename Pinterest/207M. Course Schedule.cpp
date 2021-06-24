/*
207M. Course Schedule
Topological sort, DFS, BFS

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
 

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

Similar Questions:
Course Schedule II - Medium
Graph Valid Tree - Medium
Minimum Height Trees - Medium
Course Schedule III - Hard
*/

/*
Method: Topological sort is an approach to solve the problems with Directed Acyclic Graph.
        For this question, we need to create two vectors.
        1. The index of the first vector is the course number (vertices), 
           the values saved in that cell are the children of that vertex.
           For example, [1, 0]. 0 is the index, and 1 is saved in vec[0]
        2. The second vector contains the number of parents.
           The index is the course number (vertex), the value is the number of parents.
           For example, [1, 0], [2, 0]
           vec[0] = 0, vec[1] = 1, vec[2] = 1
        
        We also need to create a queue, and put the vertices that don't have any parents into the queue.
        For each element in the queue, we reduce the value in the corresponding cell in the second vector.
        When there is a new cell has 0 parent, we then put it into the queue.
        
        Time complexity: O(m+n), m is the total number of edges, n is the total number of vertices.
        Space complexity: O(n), we create two vectors with size of number of vertices.
*/
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Save the edges
        // Index is the course number, values are its children
        vector<vector<int>> graph(numCourses, vector<int>());
        
        // Save number of parents of each course
        vector<int> course_index(numCourses, 0);
        
        // Process all the edges
        for(auto pre:prerequisites){
            graph[pre[1]].push_back(pre[0]);
            ++course_index[pre[0]];
        }
        
        // Initially, put the vertices which have no parents into the queue
        queue<int> q;
        for(int i=0; i<numCourses; ++i){
            if(course_index[i]==0){
                q.push(i);
            }
        }
        
        // Process all the vertices
        while(!q.empty()){
            int index = q.front(); q.pop();
            for(auto val:graph[index]){
                --course_index[val];
                
                // If there is a new vertex that has no parent, save it to the queue.
                if(course_index[val]==0){
                    q.push(val);
                }
            }
        }
        
        // Check if there is a cycle, e.g. [1,0], [0,1]
        for(auto val:course_index){
            if(val!=0){
                return false;
            }
        }
        
        return true;
    }
};
