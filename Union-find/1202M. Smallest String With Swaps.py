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
Method: Use union-find to connect all the nodes into groups.
        For each group, we sort the list and obtain the best result.
        bcade [[0,2], [2, 4], [1, 3]]
        0, 2, and 4 are in a group, the letters are 'bae'. Since we can swap any number of times, the best one we can obstain is 'abe'.
        The same to 1 and 3. The best result we can obtain is 'cd'.
        Hence, the best result is 'acbde'.
        But this approach exceeds the time limit.
"""
class UF(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.count = n
    def find(self, p):
        while p!=self.parent[p]:
            p = self.parent[p]
        return p
    def union(self, p, q):
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += rootP
        self.count -= 1
    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        uf = UF(len(s))
        for edge in pairs:
            uf.union(edge[0], edge[1])
        pos = [[] for _ in range(uf.count)] 
        char = [[] for _ in range(uf.count)] 
        pos[0].append(0)
        char[0].append(s[0])
        for i in range(1, len(s)):
            for j in range(uf.count):
                if len(pos[j]) and not uf.connected(i, pos[j][0]):
                    continue
                pos[j].append(i)
                char[j].append(s[i])
                break

        res = [""] * len(s)
        for i in range(uf.count):
            pos[i].sort()
            char[i].sort()
            for p, c in zip(pos[i], char[i]):
                res[p] = c

        return ''.join(res)
        






