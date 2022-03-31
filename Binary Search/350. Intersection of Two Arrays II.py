class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        """
        Method 1:
        """
        set1 = set(nums1)
        set2 = set(nums2)
        
        intersec = set1.intersection(set2)
        ans = []
        
        for num in intersec:
            min_no = min(nums1.count(num), nums2.count(num))
            for i in range(min_no):
                ans.append(num)
        return ans
        
        
        
        """
        Method 2:
        """
        n1 = collections.Counter(nums1)
        n2 = collections.Counter(nums2)
        n2_sorted = n2.keys()
        n2_sorted.sort()
        
        ans = []
        for n in n1.keys():
            if self.binarySearch(n2_sorted, n):
                times = min(n1[n], n2[n])
                ans.extend([n]*times)
        return ans
    
    def binarySearch(self, arr, target):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid]==target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
      
        
