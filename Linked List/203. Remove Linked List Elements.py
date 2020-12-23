"""
203. Remove Linked List Elements
Linked List

Description:
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

Similar Questions:
Remove Element - Easy
Delete Node in a Linked List - Easy
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        """
        Method: To remove a node from linked list, we need to implement current.next = current.next.next.
                The condition is to check if current.next has a value and that value is equal to val.
                The second step, we need to consider the first node of the list.
                So, we create a while loop to check the head.val.
        """
        if head is None:
            return head
        while head and head.val == val:
            head = head.next
        curr = head
        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
        
        """
        As a comparison, this is the first successful code. It checks too many conditions.
        """
        if head is None:
            return head
        elif head.next is None:
            if head.val == val:
                return head.next
            else:
                return head
        cur = head
        while cur:
            if head.val == val:
                head = head.next
                cur = head
                continue
            elif cur.val == val:
                pre.next = cur.next
                cur = cur.next
                continue

            pre = cur
            cur = cur.next
        return head


