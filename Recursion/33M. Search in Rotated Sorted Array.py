class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, left, right, target):
            if left <= right:
                mid = int(left + (right-left)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < nums[right]:
                    if nums[mid]<target and target<=nums[right]:
                        return binarySearch(nums, mid+1, right, target)
                    else:
                        return binarySearch(nums, left, mid-1, target)
                else:
                    if nums[left]<=target and target<nums[mid]:
                        return binarySearch(nums, left, mid-1, target)
                    else:
                        return binarySearch(nums, mid+1, right, target)
            return -1
        return binarySearch(nums, 0, len(nums)-1, target)
