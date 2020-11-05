'''
1299. Replace Elements with Greatest Element on Right Side

Description:
Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
'''

# Solution:
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        '''
        Method 1: Sweep the entire array from the beginning.
                  Search for the maximum element from i+1 to len(arr), and save that element and its position.
                  If the current looping index i is less than that position, we simply replace the current element with the max.
                  If i reaches to max_index, we then search for the max again.
        '''
        n_inf = float("-inf")
        max_index = 0
        if len(arr) == 1:
            arr[0] = -1
            return arr
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            elif max_index == i:
                max_element = n_inf
                for j in range(i+1, len(arr)):
                    if arr[j] > max_element:
                        max_element = arr[j]
                        max_index = j
                arr[i] = max_element
            else:
                arr[i] = max_element
        return arr
        
        
        '''
        Method 2: We sweep the array from the back.
                  Save the current element to t, and find out the maximum between t and current max temp.
        '''
        temp = -1
        for i in range(len(arr)-1, -1, -1):
            t = arr[i]
            arr[i] = temp
            temp = max(temp, t)
        return arr


