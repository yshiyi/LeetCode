'''
350. Intersection of Two Arrays II

Description:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

Similar Questions:
Intersection of Two Arrays - Easy
Find Common Characters - Easy
'''

# Solution:
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        '''
        Method 1: Using set(A).intersection() to extract the common elements in both nums1 and nums2
                  Convert the intersection into a list.
                  For each element in the list, we find the minimum number of that element contained in both nums1 and nums2.
                  Extend the result list by that number of that element.
        '''
        common=list(set(nums1).intersection(nums2))
        result = []
        for x in common:
            result.extend([x]*min(nums1.count(x),nums2.count(x)))
        return result
        
        '''
        Method 2: Using a hash table (i.e., a dictionary) to contain the distinct elements we have visit in nums1
                  For each distinct element, we find the minimum number of that element contained in both nums1 and nums2.
                  
        '''
        if len(nums1) < len(nums2):
            A1 = nums1
            A2 = nums2
        else:
            A1 = nums2
            A2 = nums1
            
        Ndic = {}
        result = []
        for i in range(len(A1)):
            if A1[i] not in Ndic:
                Ndic[A1[i]] = i
                if A1[i] in A2:
                    result.extend([A1[i]]*min(A1.count(A1[i]), A2.count(A1[i])))
        return result

        '''
        Method 3: Sort both nums1 and nums2 at first.
                  Count the minimum number of shared elements.
        '''
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        i = 0
        while i < len(nums1):
            if nums1[i] in nums2:
                result.extend([nums1[i]]*min(nums1.count(nums1[i]), nums2.count(nums1[i])))
                i += nums1.count(nums1[i])
            else:
                i += 1
        return result
        
