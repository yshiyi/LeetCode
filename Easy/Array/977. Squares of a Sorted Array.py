'''
977. Squares of a Sorted Array
Array, Two Pointers

Description:
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Similar questions:
•	Merge Sorted Array Easy
•	Sort Transformed Array Medium
'''

# Solutions:
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        # Method 1: use the default function sort() and simplified loop
        return sorted(x*x for x in A)
        

        # Method 2: square every element in the array and write a function to implement quicksort algorithm.
        A_square = [x * x for x in A]
        return self.quickSort(A_square)
    
    def quickSort(self, nums):
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[0]
            less = [i for i in nums[1:] if i <= pivot]
            greater = [i for i in nums[1:] if i > pivot]
            return self.quickSort(less) + [pivot] + self.quickSort(greater)
        
        
        '''
        Method 3: Create two pointers: i and j.
                  j: counts the number of negative elements, points to the first non-negative element.
                  i: points to the largest negative element.
                  Then we start to compare elements from j to N and from i to 0.
                  When j reaches to N or i reaches to 0, we stop the loop. 
                  Then add the rest of array (i.e., A[:i] or A[j:]) to the end of answer.
        '''
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans

