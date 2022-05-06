"""
1136. Parallel Courses

Description:
There are N courses, labelled from 1 to N.
We are given relations[i] = [X, Y], representing a prerequisite relationship between course X and course Y: 
course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the prerequisites 
for the course you are studying.

Return the minimum number of semesters needed to study all courses.  
If there is no way to study all the courses, return -1.

 

Example 1:
   1     2
    \   /
      3
Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.

Example 2:
 1  ->   2
  \     /
     3
Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
 

Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.
"""

"""
Method: Topological sort
"""
import collections
class Solution(object):
    def parallelCourse(self, courses):
        children = collections.defaultdict(list)
        parent = collections.defaultdict(int)

        for course in courses:
            parent[course[0]] = 0

        for course in courses:
            children[course[0]].append(course[1])
            parent[course[1]] += 1
        
        q = collections.deque()
        for p in parent.keys():
            if parent[p]==0:
                q.append(p)
        
        ans = 0
        while len(q):
            size = len(q)
            for _ in range(size):
                course = q.popleft()
                for child in children[course]:
                    parent[child] -= 1
                    if parent[child]==0:
                        q.append(child)
            ans += 1
        for p in parent.keys():
            if parent[p]!=0:
                return -1
        return ans

sol = Solution()
courses = [[1,2],[2,3],[3,1]]
print(sol.parallelCourse(courses))

