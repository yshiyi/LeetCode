'''
378M. Kth Smallest Element in a Sorted Matrix

Description:
Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

Follow up:
1. Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
2. Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.

Similar Questions:
Find K Pairs with Smallest Sums - Medium
Kth Smallest Number in Multiplication Table - Hard
Find K-th Smallest Pair Distance - Hard
K-th Smallest Prime Fraction - Hard
'''

# Solution
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
        
