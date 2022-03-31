"""
269H. Alien Dictionary

Decription:
There is a new alien language that uses the English alphabet. 
However, the order among letters are unknown to you.
You are given a list of strings words from the dictionary, 
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language, and return it. 
If the given input is invalid, return "". If there are multiple valid solutions, return any of them.
 
Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:
Input: words = ["z","x"]
Output: "zx"
Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
Similar Question:
Course Schedule II - Mediu
"""

"""
Method: Topological sort, two maps
        1st map, key: letter, values: its children
        2nd map, key: letter, values: number of its parents
        Use a queue to save the letters that have no parents
"""
import collections, heapq
class Solution(object):
    def allienDictionary(self, words):
        if len(words)<2:
            return words[0]
        children = collections.defaultdict(list)
        parents = collections.defaultdict(int)
        
        # Add the first letter in the first word in the parents!
        parents[words[0][0]] = 0
        for i in range(len(words)-1):
            l = min(len(words[i]), len(words[i+1]))
            for j in range(l):
                if words[i][j]!=words[i+1][j]:
                    children[words[i][j]].append(words[i+1][j])
                    parents[words[i+1][j]] += 1
                    # Don't forget to break!
                    break
        
        q = []
        heapq.heapify(q)
        for letter in parents.keys():
            if parents[letter]==0:
                heapq.heappush(q, letter)
        
        ans = ""
        while len(q):
            letter = heapq.heappop(q)
            ans += letter
            for child in children[letter]:
                parents[child] -= 1
                if parents[child]==0:
                    heapq.heappush(q, child)
        
        # Check loop
        for letter in parents.keys():
            if parents[letter]!=0:
                return ""
        
        return ans

sol  = Solution()
words1 = ["wrt","wrf","er","ett","rftt"]
words2 = ["z","x"]
words3 = ["z","x","z"]
print(sol.allienDictionary(words1))
print(sol.allienDictionary(words2))
print(sol.allienDictionary(words3))


