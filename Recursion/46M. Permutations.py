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
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        num = []
        self.helper(nums, num)
        return self.ans
    
    def helper(self, nums, num):
        if len(num)==len(nums):
            self.ans.append(copy.deepcopy(num))
            return
        for n in nums:
            if n in num:
                continue
            num.append(n)
            self.helper(nums, num)
            num.pop()
        
