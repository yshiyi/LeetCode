'''
Remove Duplicates from Sorted Array
Array, Two pointer

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. 
             It doesn't matter what values are set beyond the returned length.
'''


# Solution:

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Method 1: We just simply start from the first element and compare it with the following elements 
                  until we get a different one.
                  We then remove the duplicated elements in the list and jump to next different element.
                  This method takes about 20 ms.
        '''
        count = 0
        i = 0
        while i <= len(nums):
            if i == len(nums):
                break
            else:    
                j = 1
                while i+j+1 <= len(nums):
                    if nums[i] == nums[i+j]:
                        j += 1
                    else:
                        break    
                count += 1
                del nums[i+1:i+j]
                i = count
        return count


        '''
        Method 2: This method uses the function count() to find out the number of each element appears in the list.
		              If the number of element is greate than 1, we then remove n-1 duplicate elements.
                  It takes about 16 ms.
        '''
        i = 0
        while i <= len(nums):
            if i == len(nums):
                break
            else:
                num_dup = nums.count(nums[i])
                if num_dup == 1:
                    i += 1
                else:
                    del nums[i+1:i+num_dup]
                    i += 1
        return i

        '''
        Method 3: The problem is to return the first n elements where n is the number of distinguish elements.
                  Hence, we only need to compare elements one by one. If we encounter a different element, we put it in front.
                  This is a kind of two pointer method.
                  The first pointer sweeps the entire array. 
                  The second pointer counts the number of distinct elements.
                  When the first pointer points to a distinct element (different from the previous one).
                  We move this element to the position where the second pointer is pointing to.
                  This method takes about 12 ms.
        '''
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_
