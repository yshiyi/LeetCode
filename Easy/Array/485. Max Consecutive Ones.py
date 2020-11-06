'''
485. Max Consecutive Ones

Description:
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Similar questions:
•	Merge Two Sorted Lists (Easy)
•	Squares of a Sorted Array (Easy)
•	Interval List Intersections (Medium)
'''

# Solution:

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # The basic idea is to loop the array from the beginning and count the number of 1s.
        # When the element is equal to 1, we increase the value of count and compare it to the value of count_max. 
        # Update the value of max_count, if the current count is greater than the recorded maximum count.
        # When the element is equal to 0, we reset the value of count by making it equal to 0.
        
        count = 0  # Record the number of 1s
        count_max = 0  # Record the maximum number of 1s has been counted
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                if count > count_max:
                    count_max = count
            else:
                count = 0
        return count_max
