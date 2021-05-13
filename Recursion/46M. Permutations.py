class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        
        def backtrack(nums, temp):
            if len(temp) == len(nums):
                res.append(list(temp))
                return
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtrack(nums, temp)
                    temp.pop()
                    
        backtrack(nums, temp)
        return res
