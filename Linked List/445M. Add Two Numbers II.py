"""
445. Add Two Numbers II
Linked List

Description:
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

Similar Questions:
Add Two Numbers - Medium
Add Two Polynomials Represented as Linked Lists - Medium
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    """
    Method: Convert two lists to two integers.
            Then convert the summation of these two integers to a new linked list.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.convertToNum(l1)
        num2 = self.convertToNum(l2)
        num = num1 + num2
        ans = ListNode(None)
        cur = ans
        
        nums = str(num)
        L = len(nums)
        for i in range(L):
            newNode = ListNode(nums[i])
            cur.next = newNode
            cur = cur.next
        return ans.next
        
    
    def convertToNum(self, l):
        n = self.getLen(l)
        num = 0
        while n:
            num += l.val * (10 ** (n - 1))
            l = l.next
            n -= 1
        return num
    
    def getLen(self, l):
        n = 0
        while l:
            n += 1
            l = l.next
        return n
