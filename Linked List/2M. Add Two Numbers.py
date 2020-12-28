"""
2. Add Two Numbers
Linked List, Math

Description:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Similar Questions:
Multiply Strings - Medium
Add Binary - Easy
Sum of Two Integers - Medium
Add Strings - Easy
Add Two Numbers II - Medium
Add to Array-Form of Integer - Easy
Add Two Polynomials Represented as Linked Lists - Medium
"""

# Solution:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        """
        Method 1: Elementary math
                  Create a new list to hold the result of summation.
                  Define a new variable carry. If the summation is greater or equal to 10, then carry = 1, otherwise carry = 0.
                  The result of summation is equal to the sum of each node val and carry.
        """
        carry = 0
        ans = ListNode(None)
        self.l = ans
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = self.addTwo(val)
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                val = l1.val + carry
                carry = self.addTwo(val)
                l1 = l1.next
        elif l2:
            while l2:
                val = l2.val + carry
                carry = self.addTwo(val)
                l2 = l2.next
        if carry == 1:
            newNode = ListNode(carry)
            self.l.next = newNode
            self.l = self.l.next
        return ans.next
    
    def addTwo(self, val):
        if val < 10:
            newNode = ListNode(val)
            carry = 0
        else:
            newNode = ListNode(val % 10)
            carry = 1
        self.l.next = newNode
        self.l = self.l.next
        return carry
    
        
        """
        Method 2: First, we convert both lists to decimal numbers.
                  Then find out the length of this number by using len(str(num)).
                  Finally, we save each of the digit to a new list.
        """
        num1, num2 = 0, 0
        i = 0
        while l1:
            num1 += l1.val * (10 ** i)
            i += 1
            l1 = l1.next
        i = 0
        while l2:
            num2 += l2.val * (10 ** i)
            i += 1
            l2 = l2.next
        num = num1 + num2
        cur = ans = ListNode(None)
        l = len(str(num))
        while l:
            val = num % 10
            if val >= 10:
                val = 0
            newNode = ListNode(val)
            cur.next = newNode
            cur = cur.next
            num = (num - val) / 10
            l -= 1
        return ans.next
