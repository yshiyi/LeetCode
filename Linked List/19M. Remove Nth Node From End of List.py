"""
19. Remove Nth Node From End of List
Linked List, Two Pointers

Description:
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Similar Question:
Delete N Nodes After M Nodes of a Linked List - Easy
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        """
        Method 1: Two passes
                  In the first pass, we obtain the length of the list, Len.
                  In the second pass, we remove the number at Len - n. We need to move to one before the target number, at Len - n - 1.
                  Then node.next = node.next.next.
                  Note, if Len - n == 0, means remove the head, then return head.next.
        """
        Len = 0
        node = head
        while node:
            node = node.next
            Len += 1
            
        node = head
        if Len - n == 0:
            head = head.next
            return head
        for _ in range(Len - n - 1):
            node = node.next
        node.next = node.next.next
        
        return head
        
        
        """
        Method 2: Two pointers
                  Move the first pointer n steps ahead.
                  Then move both pointers together and remain the gap n.
                  When the first pointer reaches the last node, then p2.next = p2.next.next.
                  Note, when p1 finishes moving n steps, we need to check if p1 is none.
                  If it is, then it means to remove the head.
        """
        p1, p2 = head, head
        for _ in range(n):
            p1 = p1.next
        if p1 is None:
            return head.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head
