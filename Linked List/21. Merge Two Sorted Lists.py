"""
21. Merge Two Sorted Lists
Linked List

Description:
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Similar Questions:
Merge k Sorted Lists - Hard
Merge Sorted Array - Easy
Sort List - Medium
Shortest Word Distance II - Medium
Add Two Polynomials Represented as Linked Lists - Medium
"""

# Solution:
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        """
        Method: Using the similar idea with merge sorted array.
                Create a new list to hold the nodes and two pointers to traverse l1 and l2.
                Compare each node from l1 and l2, and save the smaller one to the new list.
                When reach the end of one of the list, we add the rest of nodes of the other list to the end of the new list.
        """
        # if l1 is None and l2 is None:
        #     return
        # elif l1 is None and l2:
        #     return l2
        # elif l1 and l2 is None:
        #     return l1
        
        ans = ListNode(None)
        l = ans
                
        while l1 and l2:
            if l1.val <= l2.val:
                # temp = l1.next
                # l1.next = l.next
                l.next = l1
                l1 = l1.next  # temp
            else:
                # temp = l2.next
                # l2.next = l.next
                l.next = l2
                l2 = l2.next  # temp
            l = l.next

        if l1 is None and l2:
            l.next = l2
            return ans.next
        elif l1 and l2 is None:
            l.next = l1
            return ans.next
        else:
            return ans.next

