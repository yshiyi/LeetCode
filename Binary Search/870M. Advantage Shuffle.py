"""
870M. Advantage Shuffle

Description:
You are given two integer arrays nums1 and nums2 both of the same length. 
The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

Example 1:
Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]

Example 2:
Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]
 

Constraints:
1 <= nums1.length <= 105
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 109
"""

'''
Method: The key idea is 田忌赛马.  
        Sort nums1 and traverse nums2. Keep the min and max of nums1 in each iteration. 
        If none of value in nums1 is larger than the value in nums2, use the min to match it up.
        Otherwise, use binary search to find the smallest number that is greater than the value in nums2.
'''

# Solution:
class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [0]*len(nums1)
        nums1.sort()
        for i in range(len(nums2)):
            _min, _max = nums1[0], nums1[-1]
            if nums2[i]>=_max:
                ans[i] = _min
                nums1.pop(0)
            else:
                index = self.helper(nums1, nums2[i])
                ans[i] = nums1[index]
                nums1.pop(index)
        return ans
    
    def helper(self, nums, target):
        left ,right = 0, len(nums)-1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]<=target:
                left = mid + 1
            else:
                right = mid - 1
        return left
