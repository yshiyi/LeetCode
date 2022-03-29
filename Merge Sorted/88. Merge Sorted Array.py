"""
88. Merge Sorted Array
Array, Two Pointers

Description:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]

Similar Questions:
Merge Two Sorted Lists - Easy
Squares of a Sorted Array - Easy
Interval List Intersections - Medium
"""

# Solution:
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        '''
        Method 1: Variable i is to count the element in nums2.
                  Variable index is to count the position where the nums2 element inserts into nums1.
                  The first case, the nums2 element is greater than the last element in nums1. We then simply add 
                  this element to position m+i.
                  The second case, the nums2 element is less than the first element in nums1. We then add this elment
                  to the first position in nums1 and shift the rest elements in nums1 to the right by 1.
                  The third case, we compare each element in nums2 to nums1. If nums2 element is less than nums1 element,
                  we then add this element into nums1 and shift the rest of elements in nums1.
        '''
        index = 0
        for i in range(n):
            if nums2[i] > nums1[m+i-1]:
                nums1[m+i] = nums2[i]
            elif nums2[i] <= nums1[0]:
                for h in range(m+i, 0, -1):
                    nums1[h] = nums1[h-1]
                nums1[0] = nums2[i]
                index += 1
            else:
                j = index
                while j < m+i:
                    if nums2[i] <= nums1[j]:
                        for k in range(m+i, j, -1):
                            nums1[k] = nums1[k-1]
                        nums1[j] = nums2[i]
                        index = j+1
                        j = m+i+1
                    else:
                        j += 1
        return nums1


        '''
        Method 2: We create a new array to hold all elements and put them back to nums at the end.
                  We use two pointers. 
                  In the main loop, we sweep the array nums1 and compare each element in nums1 to nums2.
                  We save the smaller element to the new array. 
                  If this element comes from nums2, we then increase the counter index.
                  In the second loop, I put any left elements in nums2 (they are greater then all elements in nums1) to the new array.
                  At the end, we transfer all elements from the new array to nums1.
        '''
        # arr= []
        #
        # index=0
        # for i in range(m):
        #     if index < n and nums1[i] < nums2[index]:
        #         arr.append(nums1[i])
        #     else:
        #         while index < n and nums2[index] < nums1[i]:
        #             arr.append(nums2[index])
        #             index += 1
        #         arr.append(nums1[i])
        #
        # for i in range(index,n):
        #     arr.append(nums2[i])
        # for j in range(len(arr)):
        #     nums1[j] = arr[j]
        # return nums1
