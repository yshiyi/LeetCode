# Method 1: Merge sort
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)==1:
            return nums
        pivot = int(len(nums)/2)
        return self.mergeSort(self.sortArray(nums[0:pivot]), self.sortArray(nums[pivot:]))
    
    def mergeSort(self, left, right):
        l, r = 0, 0
        res = []
        while l<len(left) and r<len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        res.extend(left[l:])
        res.extend(right[r:])
        return res
        

