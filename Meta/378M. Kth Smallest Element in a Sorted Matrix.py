"""
378. Kth Smallest Element in a Sorted Matrix

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
"""

"""
Method 1: Heap, but it doesn't take the advantage that the matrix is already sorted by rows and by columns.
          Time complexity: O(M*N*logk)
          Space complexity: O(k)
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        q = []
        heapq.heapify(q)
        for row in matrix:
            for ele in row:
                heapq.heappush(q, ele*-1)
                if len(q)>k:
                    heapq.heappop(q)
        return q[0]*-1
        

"""
Method 2: minHeap
          We put the first element from each row into a queue, 
          and move the pointer that points to the smallest value.
          We then iterate k times.
          Time complexity: O(klogk)
          Space complexity: O(k)
"""
m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
        minHeap = []  # val, r, c
        heapq.heapify(minHeap)
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -1  # any dummy value
        for i in range(k):
            ans, r, c = heappop(minHeap)
            if c+1 < n: 
                heapq.heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return ans
