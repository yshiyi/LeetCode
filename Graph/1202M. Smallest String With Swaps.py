"""
1202M. Smallest String With Swaps

Description:
You are given a string s, and an array of pairs of indices in the string pairs 
where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.


Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 
Constraints:
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""

"""
Method: Creat an undirected graph.
        Use BFS to find all positions that are connected.
        bcade [[0,2], [2, 4], [1, 3]]
        0, 2, and 4 are in a group, the letters are 'bae'. Since we can swap any number of times, the best one we can obstain is 'abe'.
        The same to 1 and 3. The best result we can obtain is 'cd'.
        Hence, the best result is 'acbde'.
"""
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        graph = collections.defaultdict(list)
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        
        n = len(s)
        res = [""] * n
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            q = collections.deque()
            q.append(i)
            visited.add(i)
            pos, char = [], []
            while len(q):
                cur = q.popleft()
                # Record the positions
                pos.append(cur)
                # Record the letters at those positions
                char.append(s[cur])
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            
            # Sort the positions and letters so that the smallest letter will stay at the front position.
            pos.sort()
            char.sort()
            
            for ch, pos in zip(char, pos):
                res[pos] = ch
        
        return ''.join(res)


