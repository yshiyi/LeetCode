'''
941. Valid Mountain Array

Description:
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
      1. A.length >= 3
      2. There exists some i with 0 < i < A.length - 1 such that:
            A[0] < A[1] < ... A[i-1] < A[i]
            A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true
'''

# Solution:
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        '''
        Method1 : At the begnning, we assume the valley of the array is at the last position.
                  For each element in array, we check if this one is the valley. If so, we update valley_index and switch off flag.
                  Just in case if the array is non-decreasing, the valley_index will be remain the same as the initial value at the end.
        '''
        valley_index = len(A)  # Initialize the index of valley
        flag = True  # When flag is True, we need to update the index of valley
        Mountain = True
        if len(A) < 3:
            Mountain = False
        else:
            for i in range(1, len(A)):
                if flag:
                    if i < len(A)-1 and A[i] > A[i-1] and A[i] > A[i+1]:
                        valley_index = i
                        flag = False
                
                if i < valley_index and A[i] <= A[i-1]:
                    Mountain = False
                elif i > valley_index and A[i] >= A[i-1]:
                    Mountain = False
        if valley_index == len(A):
            Mountain = False
        return Mountain
        
        
        '''
        Method 2: At first, we walk up from left to right, and save the index when we reach the peak.
                  If the peak is at the start or at the end, it is not a mountain.
                  After we reach the peak, we keep walking down to the right.
                  If we stop at the end, then it is a mountain.
        '''
        i = 0

        # walk up
        while i < N = len(A) - 1 and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N = len(A) - 1:
            return False

        # walk down
        while i < N = len(A) - 1 and A[i] > A[i+1]:
            i += 1

        return i == N = len(A)-1
