'''
66. Plus One
Array

Description:
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

Similar Questions:
Multiply Strings - Medium
Add Binary - Easy
Plus One Linked List - Medium
Add to Array-Form of Integer - Easy
'''

# Solution:
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        '''
        Method 1: Brute Force
                  Sum up all the numbers in digits to obtain the decimal number.
                  Add one to that number.
                  Create a list, result, to hold the answer. 
                  Save the remainder of num / 10 to the corresponding index of result.
                  Then remove the last digit from the num by (num - num % 10) / 10.
                  When there are leading zeros (i.e., num == 0), we let result[i] = 0.
        '''
        num = 0
        for i in range(-1, -len(digits)-1, -1):
            num += digits[i] * 10 ** (-i - 1)
        num += 1
        
        # In case there are leading zeros
        result = [0] * max(len(str(num)), len(digits))
        for j in range(-1, -len(str(num))-1, -1):
            if num != 0:
                result[j] = num % 10
                num = (num - num % 10) / 10
            else:
                result[j] = 0
        return result
        
        
        '''
        Method 2: This is a straight-forward method.
                  We simply check the value of each digit from the end.
                  If it is equal to 9, we let it be 0.
                  If it is not equal to 9, the operation should end and return the result.
                  If all digits are 9, we then insert 1 at the first position and return the result.
        '''
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        # digits.insert(0, 1)
        return [1] + digits

