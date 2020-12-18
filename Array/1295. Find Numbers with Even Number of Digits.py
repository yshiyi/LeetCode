'''
1295. Find Numbers with Even Number of Digits
Array

Description:
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

Example 2:
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
'''

# Solution:
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # The basic idea is to use function str() to convert each element to string, 
        # and check out the length of each string to determine if the element has even number of digits.
        # If the element has, we then increase the value of count.
        count = 0  # Record the number of elements with even number of digits
        for i in range(len(nums)):
            string = str(nums[i])
            if len(string)%2 == 0:
                count += 1
        return count
        
