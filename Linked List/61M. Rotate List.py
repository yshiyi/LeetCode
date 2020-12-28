"""
61. Rotate List
Linked List, Two Pointers

Description:
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Similar Questions:
Rotate Array - Medium
Split Linked List in Parts - Medium
"""

# Solution:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        """
        Method 1: Using the similar idea of 189M. Rotate Array
                  First, convert the linked list to an array/a list.
                  Rotate this array by k times, elements will be moved to (i + k) % L position.
                  Finally, convert the rotated list to a new linked list.
        """
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        L = len(l)
        l_new = [0 for _ in range(L)]  # [0] * L
        for i in range(L):
            l_new[(i + k) % L] = l[i]
        
        cur = ans = ListNode()
        for i in range(L):
            newNode = ListNode(l_new[i])
            cur.next = newNode
            cur = cur.next
        return ans.next
        
        
        """
        Method 2: Create a cycle link by linking the last to node of the list to the first node.
                  Move n-k-1 steps to make the pointer points to the last node in the rotated link.
                  Fianlly, let the cur2.next = None to terminate the cycle.
        """
        if head is None or head.next is None:
            return head
        
        n = self.getLen(head)
        if k % n == 0:
            return head
        elif k > n:
            k = k % n

        cur = head
        while cur.next:
            cur = cur.next
        cur.next = head
        cur2 = head
        
        for _ in range(n - k - 1):
            cur2 = cur2.next
        head = cur2.next
        cur2.next = None
        
        return head

    
    def getLen(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        return n

