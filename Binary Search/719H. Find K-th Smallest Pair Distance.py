class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left, right = 0, nums[-1]-nums[0]
        while left<right:
            mid = (right+left)//2
            count, j = 0, 1
            for i in range(len(nums)):
                while j<len(nums) and nums[j]-nums[i]<=mid:
                    j += 1
                count += j-i-1
            if count >=k:
                right = mid
            else:
                left = mid+1
        return left
        
        
