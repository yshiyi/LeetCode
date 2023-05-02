"""
216M. Combination Sum III.py

Description:
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Constraints:
2 <= k <= 9
1 <= n <= 60
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.target = n
        self.k = k
        num = []
        self.helper(range(1, 10), num, 0, 0)
        return self.ans
    
    def helper(self, nums, num, Sum, start):
        if Sum == self.target and len(num) == self.k:
            self.ans.append(copy.deepcopy(num))
            return
        if Sum > self.target:
            return
        for i in range(start, len(nums)):
            Sum += nums[i]
            num.append(nums[i])
            self.helper(nums, num, Sum, i+1)
            num.pop()
            Sum -= nums[i]
