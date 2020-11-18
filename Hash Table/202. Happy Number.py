'''
202. Happy Number
Hash Table, Math

Description:
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Similar Questions:
Linked List Cycle - Easy
Add Digits - Easy
Ugly Number - Easy
'''

# Solution:
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        '''
        Method: Create a set to hold the numbers have seen.
                Firstly, calculate the sum of the square of each digits of number n.
                Then check if this number is contained in the set seen.
                If so, it will be an infinit loop and return false.
                Otherwise, add this number to seen and go on.
        '''
        seen = set()
        while True:
            n = self.squareSum(n)
            if n not in seen:
                seen.add(n)
            else:
                return False
            if n == 1:
                return True
            # print(n, seen)
            
        
        
    def squareSum(self, n):
        result = 0
        for x in str(n):
            result += int(x) ** 2
        return result
