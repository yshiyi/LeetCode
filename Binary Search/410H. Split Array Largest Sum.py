class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = 0, 0
        for num in nums:
            left = max(num, left)
            right += num
        
        def binarySearch(nums, targetSum, m):
            curSum, n = 0, 1
            for i in range(len(nums)):
                curSum += nums[i]
                if curSum > targetSum:
                    curSum = nums[i]
                    n += 1
                    if n > m:
                        return False
            return True
        
        while left < right:
            mid = (right + left)//2
            if binarySearch(nums, mid, m):
                right = mid
            else:
                left = mid + 1
        return left
