class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        check = [0]*len(nums)
        nums.sort()
        
        def isValid(nums, check, i):
            if check[i]==1:
                return False
            if i>0 and nums[i]==nums[i-1] and check[i-1]==0:
                return False
            return True
        
        def backtrack(nums, res, temp, check, start):
            res.append(list(temp))
            for i in range(start, len(nums)):
                if isValid(nums, check, i):
                    check[i]=1
                    temp.append(nums[i])
                    backtrack(nums, res, temp, check, i+1)
                    temp.pop()
                    check[i]=0
        backtrack(nums, res, temp, check, 0)
        return res
