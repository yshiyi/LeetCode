"""
234. Palindrome Linked List
Linked List, Two Pointers

Description:
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?


Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Similar Question:
Palindrome Number - Easy
Valid Palindrome - Easy
Reverse Linked List - Easy
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        """
        Method 1: Two Pointers
                  Original idea is to create a new list to hold the reversed list. 
                  But it doesn't work out, because once the original list is reversed, it won't remain the same as before.
                  
                  Therefore, we need to create two pointers.
                  One moves two steps and the other moves one step per iteration. So, we can determine the middle point.
                  Then, we reverse the second part of the list and compare it with the first half.
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        head2 = None
        while slow:
            temp = slow.next
            slow.next = head2
            head2 = slow
            slow = temp
        
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
        
        
        """
        Method 2: Create a list to hold the values of the list.
                  Then use nodes[::-1] == nodes to compare values from beginning and end.
        """
        nodes=[]
        while head:
            nodes.append(head.val)
            head=head.next
        return nodes[::-1]==nodes

