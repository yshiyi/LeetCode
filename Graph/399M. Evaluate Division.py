"""
399M. Evaluate Division

Description:
You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. 
You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:
1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""

"""
Method: Create a graph, and use BFS.
"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(list)
        for (A, B), value in zip(equations, values):
            graph[A].append((B, value))
            graph[B].append((A, 1/value))
        
        ans = []
        for (A, B) in queries:
            if A not in graph or B not in graph:
                ans.append(-1.0)
            else:
                seen = set()
                value = 1.0
                q = collections.deque()
                q.append((A, value))
                # This flag is to check if we have found the results.
                # [[a, b], [c, d]], query = [a,c], both a and c are in the graph, but there is no connection between them.
                flag = False
                while len(q):
                    C, val = q.popleft()
                    seen.add(C)
                    if B == C:
                        ans.append(val)
                        flag = True
                        break
                    for D, value in graph[C]:
                        if D in seen:
                            continue
                        q.append((D, value*val))
                if not flag: ans.append(-1.0)
        return ans

