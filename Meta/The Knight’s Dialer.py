"""
Imagine you place a knight chess piece on a phone dial pad. This chess piece moves in an uppercase “L” shape: 
two steps horizontally followed by one vertically, or one step horizontally then two vertically:

Image for post
1  2  3
4  5  6
7  8  9
   0
Pay no attention to the poorly-redacted star and pound keys
Suppose you dial keys on the keypad using only hops a knight can make. 
Every time the knight lands on a key, we dial that key and make another hop. 
The starting position counts as being dialed.

How many distinct numbers can you dial in N hops from a particular starting position?
"""

"""
Method: Backtracking
"""
import copy
class Solution(object):
    def countDial(self, start, numhops):
        self.moves = {1: [6, 8],
                      2: [7, 9],
                      3: [5, 8],
                      4: [0, 3, 9],
                      6: [0, 1, 7],
                      7: [2, 6],
                      8: [1, 3],
                      9: [2, 4],
                      0: [4, 6]}
        self.ans = []
        self.helper(start, numhops, 1, [start])
        return self.ans

    def helper(self, start, numhops, cur_numhops, nums):
        if cur_numhops==numhops:
            self.ans.append(copy.deepcopy(nums))
            return

        for num in self.moves[start]:
            nums.append(num)
            cur_numhops += 1
            self.helper(num, numhops, cur_numhops, nums)
            cur_numhops -= 1
            nums.pop()

sol = Solution()
_start, _numhops = 1, 4
print(sol.countDial(_start, _numhops))
