"""
25. Reverse Nodes in k-Group
Linked List

Description:
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:
Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Example 3:
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]

Example 4:
Input: head = [1], k = 1
Output: [1]

Similar Question:
Swap Nodes in Pairs - Medium
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    """
    Method: Using the similar idea of recursive method in 24M. Swap Nodes in Pairs
            We first reverse the first k nodes and save them to a new list.
            Then send the rest of the list back to the recursive function.
            Note, we can't use global self.head2. It will save the nodes in front of it rather than in the end.
    """
    def getLen(self, head):
        L = 0
        while head:
            L += 1
            head = head.next
        return L
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        L = self.getLen(head)
        
        if L < k:
            return head
        
        head2 = None
        count = k
        while head and count:
            temp = head.next
            head.next = head2
            head2 = head
            head = temp
            count -= 1
        
        cur = head2
        while cur.next:
            cur = cur.next

        cur.next = self.reverseKGroup(head, k)
        
        
        return head2
