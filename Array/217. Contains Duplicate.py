'''
217. Contains Duplicate
Array, Hash table

Description:
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

Similar Questions:
Contains Duplicate II - Easy
Contains Duplicate III - Medium
'''

# Solution:
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        '''
        Method 1: Create a hash table (i.e., dictionary)
                  Check if the element of nums is in dic. If not, add it to dic and remain dup = False.
                  If it is in dic, let dup = True and return dup
        '''
        dup = False
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                dup = True
                return dup
        return dup
        
        '''
        Method 2: Use set()!!!
                  Note the elements contained in a set are distinct!!
                  Compare len(set(nums)) and len(nums)
        '''
        return True if len(set(nums)) < len(nums) else False

