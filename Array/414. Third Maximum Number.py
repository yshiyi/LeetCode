'''
414. Third Maximum Number
Array

Description:
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. 
The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

Similar Question:
Kth Largest Element in an Array - Medium
'''

# Solution:
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Method: Use a counter to search for the third maximum number, if len(nums)>2.
                If there is no such number, return max(nums).
        '''
        
        nums_sorted = sorted(nums, reverse=True)
        count = 0
        if len(nums) > 2:
            for i in range(1, len(nums_sorted)):
                if nums_sorted[i] < nums_sorted[i-1]:
                    count += 1
                if count == 2:
                    return nums_sorted[i]
        return max(nums)
            


