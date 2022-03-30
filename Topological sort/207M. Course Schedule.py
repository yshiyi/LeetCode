"""
207. Course Schedule

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
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. 
So it is impossible.
 

Constraints:
1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

"""
Method: Directed Acyclic Graph (Topological sort)
        Two lists, both of lists have the size of num of nodes
        1st list: contains the children of each node
        2nd list: contains the number of parents of each node
        Use a queue to track the nodes that have no parents
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        children = [[] for _ in range(numCourses)]
        parents = [0] * numCourses
        
        # Fill in two lists
        for pre in prerequisites:
            children[pre[1]].append(pre[0])
            parents[pre[0]] += 1
        
        # Find those node that don't have any parents
        q = collections.deque()
        for i in range(len(parents)):
            if parents[i]==0:
                q.append(i)
        
        # for each node that has no parents, we find its children and reduce the num of parents by 1
        # if there is a new node that has no parents, add it into queue
        while len(q):
            index = q.popleft()
            for val in children[index]:
                parents[val] -= 1
                if parents[val]==0:
                    q.append(val)
        
        # Check if there is any cycle
        for val in parents:
            if val != 0:
                return False
        
        return True


