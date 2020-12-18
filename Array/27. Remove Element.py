'''
27. Remove Element
Array, Two Pointers

Description:
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
'''

# Solution:
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        '''
        Method 1: Use two pointer method.
                  When nums[i] != val, we move the value nums[i] to nums[counter] and increase both pointers counter and i.
                  When nums[i] = val, we keep the value of counter and increase i.
		              This method takes about 16-24 ms.
        '''
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
                i += 1
            else:
                i += 1
        return count
       
       '''
       Method 2: This is an in-place operation method.
                 When nums[i] = val, we move the last element in the array to position i, remove the last element 
                 from the array and reduce the length of array by 1.
       '''
        i = 0
        L = len(nums)
        while i < L:
            if nums[i] == val:
                nums[i] = nums[-1]
                del nums[-1]
                L -= 1
            else:
                i += 1
        return L

