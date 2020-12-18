'''
448. Find All Numbers Disappeared in an Array
Array

Description:
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input: [4,3,2,7,8,2,3,1]
Output: [5,6]

Similar Questions:
First Missing Positive - Hard
Find All Duplicates in an Array - Medium
'''

# Solution:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        '''
        Method 1: Create nums_disappear to hold the missing numbers.
                  At first, we need to check if the first number in nums is 1. If not, we add 1 to (1st number - 1) to nums_disappear.
                  If the 1st number = 1, we check the rest of numbers. 
                  If there is a number greater than its previous number + 1, we add the numbers between them to nums_disappear.
                  When we reach to the end of nums and the last number != len(nums)+1, we add the last number to len(nums)+1 to nums_disappear.
        '''
        nums_sorted = sorted(nums)
        nums_disappear = []
        if len(nums) < 1:
            return nums
        if nums_sorted[0] != 1:
            for l in range(1, nums_sorted[0]):
                    nums_disappear.append(l)
        for i in range(1, len(nums)):
            if nums_sorted[i] > nums_sorted[i-1]+1:
                for j in range(1, nums_sorted[i]-nums_sorted[i-1]):
                    nums_disappear.append(nums_sorted[i-1] + j)
            elif i == len(nums) - 1 and nums_sorted[i] != len(nums):
                for k in range(1, len(nums)-nums_sorted[i]+1):
                    nums_disappear.append(nums_sorted[i] + k)
        return nums_disappear
        
        
        '''
        Method 2: Use set() to compare.
                  The first set contains the numbers from 1 to len(nums)+1.
                  The second set contains the numbers in nums.
                  A.difference(B): for A - B, elements in A but not in B
                  B.difference(A): for B - A, elements in B but not in A
        '''
        standard = set(range(1,len(nums)+1))
        nums = set(nums)
        missing = list(standard.difference(nums)) # for standard - nums, numbers in standard but not in nums
        return missing
