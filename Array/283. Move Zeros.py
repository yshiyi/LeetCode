'''
283. Move Zeroes
Array, Two Pointers

Description:
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Similar Question:
Remove Element - Easy
'''

# Solution:
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        '''
        Method: Create two pointers.
                Pointer i sweeps the entire array. Pointer count points to the zero position.
                Starting from the first element, when there is a zero, we stop count and keep increasing i.
                When there is nonzero element, we move this element to the position where count is pointing to.
                This operation only excutes when i != count (i.e., there is a zero element in front).
        '''
        i = 0
        count = 0
        if len(nums) < 2:
            return nums
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != count:
                    nums[count] = nums[i]
                    nums[i] = 0
                count += 1
        return nums
                

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        slow = 0
        while slow < len(nums):
            if nums[slow] == 0:
                break
            slow += 1
        if slow + 1 == len(nums):
            return nums
        fast = slow + 1
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        return nums
        
