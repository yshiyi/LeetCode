class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, left, right):
            pivot_index = randint(left, right)
            pivot = nums[pivot_index]
            i = right
            for j in range(right, left-1, -1):
                if nums[j]>=pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    if j==pivot_index:
                        pivot_index = i
                    i -= 1
            i += 1
            nums[i], nums[pivot_index] = nums[pivot_index], nums[i]
            return i
        def quickSelect(nums, left, right, k):
            if left<=right:
                index = partition(nums, left, right)
                if right - index == k - 1:
                    return nums[index]
                if right - index > k - 1:
                    return quickSelect(nums, index+1, right, k)
                else:
                    return quickSelect(nums, left, index-1, k-(right-index+1))
            return -1
        
        
        return quickSelect(nums, 0, len(nums)-1, k)
