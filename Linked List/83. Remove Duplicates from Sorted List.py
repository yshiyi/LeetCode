"""
83. Remove Duplicates from Sorted List
Linked List

Description:
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3

Similar Questions:
Remove Duplicates from Sorted List II - Medium
"""

#Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Method: Brute force
                Create two pointers.
                We move the first pointer in the main loop.
                If the second pointer points to a duplicate, we then skip that node and keep moving it until we reach to a new node.
                Then we link the first pointer to the second by cur.next = cur2.
        """
        if head is None or head.next is None:
            return head
        
        cur = head
        while cur:
            cur2 = cur

            while cur2 and cur2.val == cur.val:
                cur2 = cur2.next
            cur.next = cur2
            cur = cur.next
        return head
