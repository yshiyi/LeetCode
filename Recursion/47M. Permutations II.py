class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        check = [0]*len(nums)
        
        def isValid(nums, check, i):
            if check[i]==1:
                return False
            if i>0 and nums[i]==nums[i-1] and check[i-1]==0:
                return False
            return True
        
        def backtrack(nums, check, temp):
            if len(temp) == len(nums):
                res.append(list(temp))
                return
            for i in range(len(nums)):
                if isValid(nums, check, i):
                    check[i] = 1
                    temp.append(nums[i])
                    backtrack(nums, check, temp)
                    temp.pop()
                    check[i] = 0
                    
        backtrack(sorted(nums), check, temp)
        return res
