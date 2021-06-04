class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        left, right = (m+n+1)//2, (m+n+2)//2
        
        def findKth(nums1, i, nums2, j, k):
            if i>=len(nums1):
                return nums2[j+k-1]
            if j>=len(nums2):
                return nums1[i+k-1]
            if k==1:
                return min(nums1[i], nums2[j])
            if (i+k//2-1)>=len(nums1):
                minVal1 = float('inf')
            else:
                minVal1 = nums1[i+k//2-1]
            if (j+k//2-1)>=len(nums2):
                minVal2 = float('inf')
            else:
                minVal2 = nums2[j+k//2-1]
            if minVal1 < minVal2:
                return findKth(nums1, i+k//2, nums2, j, k-k//2)
            else:
                return findKth(nums1, i, nums2, j+k//2, k-k//2)
            
        
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right))/2.0
    
