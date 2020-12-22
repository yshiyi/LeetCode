"""
206. Reverse Linked List
Linked List

Description:
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Similar Question:
Reverse Linked List II - Medium
Binary Tree Upside Down - Medium
Palindrome Linked List - Easy
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Method 1: Iterative method
                  Note, if we let temp = current and current = temp.next, then when we modify current, we also modify temp.
                  But, if we let temp = current.next, then the changes on current won't affect temp.
        """
        head2 = None
        current = head
        while current:
            temp = current.next
            current.next = head2
            head2 = current
            current = temp
        return head2
    
        
        """
        Method 2: Recursive method
                  Same idea with method 1.
        """
        self.head2 = None
        return self.CreateRev(head)
    
    def CreateRev(self, head):
        if head:
            temp = head.next
            head.next = self.head2
            self.head2 = head
            head = temp
        else:
            return
        self.CreateRev(head)
        return self.head2

    
        
