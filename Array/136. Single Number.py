'''
136. Single Number
Hash table, Bit manipulation

Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Similar Questions:
Single Number II - Medium
Single Number III - Medium
Missing Number - Easy
Find the Duplicate Number - Medium
Find the Difference - Easy
'''

# Solution:
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Method 1: Create a hash table (i.e., dictionary)
                  If the element is not in the dictionary, we then add this number as a new key and its index as the value.
                  If the element is already in the dictionary, we then remove that key and its value.
                  At the end, return the only key left in the dictionary.
        '''
        single = {}
        for i in range(len(nums)):
            if nums[i] not in single:
                single[nums[i]] = i
            else:
                del single[nums[i]]
        return single.keys()[0]
        
        
        '''
        Method 2: Similar to method 1, create a set instead of a dictionary
        '''
        single = set()
        for i in range(len(nums)):
            if nums[i] not in single:
                single.add(nums[i])
            else:
                single.remove(nums[i])
        return list(single)[0]
    
        '''
        Method 3: Apply Math, 2 * (a+b+c) - (a+a+b+b+c) = c
                  Use set, note: the keys contained in a set are distinct.
        '''
        return 2 * sum(set(nums)) - sum(nums)
