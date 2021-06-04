class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)
        while left < right:
            mid = (right+left)//2
            count = 0
            for v in nums:
                if v<=mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
            
        return left
