"""
40. Combination Sum II

Description:
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
 

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

# Solution:
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        num = []
        check = [0]*len(candidates)
        self.helper(sorted(candidates), num, target, 0, check)
        return self.res
    
    def isValid(self, nums, i, start, check):
        if check[i]==1:
            return False
        elif i > start and nums[i]==nums[i-1] and check[i-1]==0:
            return False
        return True
    
    def helper(self, nums, num, target, start, check):
        if sum(num)==target:
            self.res.append(copy.deepcopy(num))
            return
        if sum(num)>target:
            return
        for i in range(start, len(nums)):
            if self.isValid(nums, i, start, check):
                num.append(nums[i])
                check[i]=1
                self.helper(nums, num, target, i+1, check)
                check[i]=0
                num.pop()
