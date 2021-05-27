class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, target, left, right):
            if left > right:
                return -1
            mid = int((right+left)/2)
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                return binarySearch(nums, target, left, mid-1)
            else:
                return binarySearch(nums, target, mid+1, right)
            
        return binarySearch(nums, target, 0, len(nums)-1)
        
