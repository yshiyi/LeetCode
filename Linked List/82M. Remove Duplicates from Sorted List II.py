"""
82. Remove Duplicates from Sorted List II
Linked List

Description:
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3

Similar Question:
Remove Duplicates from Sorted List - Easy
"""

# Solution:
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
        Method 1: Two pointers
                  Create a dummy head before the linked list to avoid duplicate beginnings.
                  The first pointer points to the distinct node.
                  The second pointer swaps through the whole list.
        """
        if head is None or head.next is None:
            return head
        
        head2 = ListNode(None)
        head2.next = head
        
        """
        Approach 1: Too many conditions to check
        """
        cur1, cur2 = head2, head2
        while cur2 and cur2.next:
            if cur1 == cur2 and cur2.next.next is None:
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1 != cur2 and cur2.next.next is None:
                cur1.next = cur2.next.next
                cur2 = cur1
            elif cur2.next.val == cur2.next.next.val:
                cur2 = cur2.next
            elif cur1 != cur2 and cur2.next.val != cur2.next.next.val:
                cur1.next = cur2.next.next
                cur2 = cur1
            elif cur1 == cur2 and cur2.next.val != cur2.next.next.val:
                cur1 = cur1.next
                cur2 = cur2.next
        
        
        """
        Approach 2: Let the second pointer start from the original head.
                    Just keep moving the second pointer.
                    When the second pointer reaches the end of the list of duplicates, we move the first pointer.
        """
        cur1, cur2 = head2, head
        while cur2:
            if cur2.next and cur2.val == cur2.next.val:
                while cur2.next and cur2.val == cur2.next.val:
                    cur2 = cur2.next
                cur1.next = cur2.next
            else:
                cur1 = cur1.next
            cur2 = cur2.next
        
        return head2.next
        
        
        
        """
        Method 2: Using hash table
                  Swap through the whole list first, and save the duplicates in a set.
                  Then start the beginning of the list again.
                  Link the nodes which are not contained in the set.
        """
        curr=head
        dup=set()
        while curr and curr.next:
            if curr.val==curr.next.val:
                dup.add(curr.val)
            curr=curr.next
        dummy=ListNode(0)
        dummy.next=head
        curr=dummy
        while curr and curr.next:
            if curr.next.val in dup:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next
                
        
