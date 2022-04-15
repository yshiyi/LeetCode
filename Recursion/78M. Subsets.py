class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                temp = list(res[i])
                temp.append(num)
                res.append(temp)
        
        return res
    
    
    def subsets(self, nums):
        self.ans = [[]]
        tmp = []
        self.helper(nums, 0, tmp)
        return self.ans
    
    def helper(self, nums, start, tmp):
        if start==len(nums):
            return
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.ans.append(copy.deepcopy(tmp))
            self.helper(nums, i+1, tmp)
            tmp.pop()
