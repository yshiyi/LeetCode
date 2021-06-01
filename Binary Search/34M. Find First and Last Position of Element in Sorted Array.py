class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if len(nums)==0:
            return res
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right+left)//2
            if nums[mid]<target:
                left = mid+1;
            else:
                right = mid
        if nums[left]!=target:
            return res
        res[0]=left
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid]<=target:
                left = mid + 1
            else:
                right = mid
        if nums[right]==target:
            res[1] = right
        else:
            res[1] = right - 1
        return res
