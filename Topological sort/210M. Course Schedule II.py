"""
210. Course Schedule II

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.


Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. 
To take course 3 you should have finished both courses 1 and 2. 
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""

"""
Time complexity: O(E+V), E is the total number of edges, V is the total number of vertices.
Space complexity: O(E+V), we create two vectors. One saves all vertices, and the other one saves edges.
"""
# Solution:
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        children = [[] for _ in range(numCourses)]
        parents = [0] * numCourses
        for pre in prerequisites:
            children[pre[1]].append(pre[0])
            parents[pre[0]] += 1
        
        q = collections.deque()
        for i in range(len(parents)):
            if parents[i]==0:
                q.append(i)
        
        ans = []
        while len(q):
            index = q.popleft()
            ans.append(index)
            for val in children[index]:
                parents[val] -= 1
                if parents[val]==0:
                    q.append(val)
        
        for val in parents:
            if val != 0:
                return []
        return ans
        
