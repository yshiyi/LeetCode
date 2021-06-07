class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        left, right = matrix[0][0], matrix[-1][-1]
        
        def search_less_equal(matrix, target):
            n = len(matrix)
            i, j, res = n-1, 0, 0
            while i>=0 and j<n:
                if matrix[i][j]<=target:
                    res += i + 1
                    j += 1
                else:
                    i -= 1
            return res
        
        while left < right:
            mid = (right+left)//2
            count = search_less_equal(matrix, mid)
            if count < k:
                left = mid+1
            else:
                right = mid
        return left
        
