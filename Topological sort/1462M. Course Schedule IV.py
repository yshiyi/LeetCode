"""
1462M. Course Schedule IV.py

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first 
if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, 
then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, 
you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

 

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
 

Constraints:
2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 104
0 <= ui, vi <= n - 1
ui != vi
"""

"""
Method: Topological Sort.
        Note that we need to create an extra dictionary to record all the directly or indirectly related parents.
"""
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        children = collections.defaultdict(list)
        parent = collections.defaultdict(int)
        result = collections.defaultdict(list)
        for i in range(numCourses):
            parent[i] = 0
        for pre in prerequisites:
            children[pre[0]].append(pre[1])
            parent[pre[1]] += 1

        q = collections.deque()
        for course in parent.keys():
            if parent[course] == 0:
                q.append(course)

        while len(q):
            course  = q.popleft()
            for child in children[course]:
                # Here, course is child's parent
                result[child].append(course)
                # As course is child's new parent, all course's parents will be child's parents too.
                # Hence, we need to update child's parents.
                result[child] = list(set(result[child] + result[course]))
                parent[child] -= 1
                if parent[child] == 0:
                    q.append(child)
        
        ans = [False for _ in range(len(queries))]
        for i in range(len(queries)):
            if queries[i][0] in result[queries[i][1]]:
                ans[i] = True
        return ans


