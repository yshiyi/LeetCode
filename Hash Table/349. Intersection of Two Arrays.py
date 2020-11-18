'''
349. Intersection of Two Arrays
Hash Table, Two Pointers, Binary Search, Sort

Description:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Similar Questions:
Intersection of Two Arrays II - Easy
Intersection of Three Sorted Arrays - Easy
'''

# Solution:
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        Method 1: Convert nums1 to set to remove duplicates.
                  Check each element in nums1
        '''
        Nums1 = set(nums1)
        result = []
        # for x in Nums1:
        #     if x in nums2:
        #         result.append(x)
        # return result
        return [x for x in Nums1 if x in Nums2]
    
                
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
        

        '''
        Method 2: Convert both nums1 and nums2 to set.
                  Use set(A).intersection(B) to obtain the intersection
        '''
        Nums1 = set(nums1)
        Nums2 = set(nums2)
        return list(set(Nums1).intersection(Nums2))
        return list(Nums1 & Nums2)


