"""
24. Swap Nodes in Pairs
Linked List, Recursion

Description:
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Similar Question:
Reverse Nodes in k-Group - Hard
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Method 1: Iterative method
        """
        if head is None or head.next is None:
            return head
        
        head2 = ListNode(0)
        
        
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
        Approach 1: Create two pointers and a new linked list.
                    Save the nodes from the original list to the new one iteratively.
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
        cur3 = head2
        cur1, cur2 = head, head.next
        while cur2:
            temp = cur2.next
            cur3.next = cur2
            cur3 = cur3.next
            cur3.next = cur1
            cur3 = cur3.next
            cur3.next = temp
            cur1 = temp
            if temp is None:
                break
            elif temp.next is None:
                cur3.next = cur1
                break
            else:
                cur2 = temp.next
        
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
        Approach 2: Using only one pointer and create a new list.
                    Check cur and cur.next.
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
        cur2 = head2
        cur1 = head
        
        while cur1 and cur1.next:
            temp = cur1.next.next
            cur2.next = cur1.next
            cur2 = cur2.next
            cur2.next = cur1
            cur2 = cur2.next
            cur2.next = temp
            cur1 = temp
        
        return head2.next

        
        """
        Method 2: Recursive method
        """
        if not head or not head.next: 
            return head
        
        nextTemp = head.next
        nextnextTemp = head.next.next
        
        nextTemp.next = head
        head.next = self.swapPairs(nextnextTemp)
        
        return nextTemp
