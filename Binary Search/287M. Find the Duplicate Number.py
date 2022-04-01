class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1: Hashmap, counter
        """
        nums_count = collections.Counter(nums)
        for key in nums_count.keys():
            if nums_count[key]!=1:
                return key
        return -1
    
        """
        Method 2: Binary search
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
