'''
905. Sort Array By Parity
Array

Description:
Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

# Solution:
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        '''
        Method: Create two pointers.
                The first pointer sweeps the entire array and searches for the even elements.
                The second pointer counts the number of even numbers. It stops at the odd element positions.
        '''
        count = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[count], A[i] = A[i], A[count]
                count += 1
        return A
