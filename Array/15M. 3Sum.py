"""
15. 3Sum
Array, Two Pointers

Description:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Similar Questions:
Two Sum - Easy
3Sum Closest - Medium
4Sum - Medium
3Sum Smaller - Medium
"""

# Solution:
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        """
        Method 1: Use two pointers.
                  Sort the array first so that we can skip the duplicate number to make sure to find unique triplets.
                  The first pointer starts from the next number, and the second pointer starts from the end of array.
                  If the summation is greater than zero, the second pointer moves backward.
                  If the summation is less than zero, the first pointer moves forward.
                  If the summation is equal to zero, we save the triplets and move the first pointer. 
                  If the next number is the same, then we keep moving the first pointer.
                  This method is much faster than method 2.
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        
        """
        Method 2: This method uses the idea of TwoSum.
                  We create another function TwoSum to find the pair of numbers those summation is equal to the negative of current number.
                  Because we need to find the unique triplets, we need to make sure there are no duplicates.
                  Note, we can't use set(), because a list can't be saved to a set. A list can be further modified, but the element in a set must be fixed.
        """
        ans = []
        nums.sort()
        i = 0

        while i < len(nums)-2:
            items = self.Twosum(nums[i+1:], -nums[i])
            if items:
                for j in range(len(items)):
                    ans.append([nums[i], items[j][0], items[j][1]])
            i += 1
            while nums[i] == nums[i-1] and i < len(nums)-2:
                i += 1
        return ans
        
        
    def Twosum(self, lst, target):
        res = []
        Dic = {}
        for i in range(len(lst)):
            if target - lst[i] not in Dic:
                Dic[lst[i]] = i
            elif [target - lst[i], lst[i]] not in res:
                res.append([target - lst[i], lst[i]]) 
        return res

