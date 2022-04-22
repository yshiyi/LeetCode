"""
238. Product of Array Except Self

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements 
of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. 

Follow up: 
Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""

"""
Method: Sweep the array twice.
        First time, sweep from left and record the product until n-1.
        Second time, sweep from right and keep tracking the product from the right.
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_left = [1]
        for i in range(len(nums)-1):
            product_left.append(product_left[-1]*nums[i])
        ans = [0] * len(nums)
        product_right=1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = product_left[i] * product_right
            product_right *= nums[i]
        return ans
