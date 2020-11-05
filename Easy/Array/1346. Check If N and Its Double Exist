'''
1346. Check If N and Its Double Exist

Description:
Given an array arr of integers, check if there exists two integers N and M 
such that N is the double of M ( i.e. N = 2 * M).

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

# Solution:
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        '''
        Method 1: Simply sweep the entire array, and check if there exists 2*M or M/2. 
        '''
        exist = False
        if len(arr) < 2:
            return False
        else:
            for i in range(len(arr)-1):
                for j in range(i+1, len(arr)):
                    if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                        exist = True
        return exist
        
        '''
        Method 2: Similar to method 1. But we use "if ... in arr" to improve the runtime.
        '''
        if arr is None or len(arr) <= 1: return False
        for i in range(len(arr)):
            if arr[i] != 0: # check if the current is not 0
                if arr[i]*2 in arr: 
                    return True
                if arr[i]%2 == 0 and arr[i] / 2 in arr:
                    return True
            else: # if 0, we have to look for a zero at a different index
                if 0 in arr[:i] or 0 in arr[i+1:]: return True
        return False

