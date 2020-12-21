"""
141. Linked List Cycle
Linked List, Two Pointers

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Similar Question:
Linked List Cycle II - Medium
Happy Number - Easy
"""

#Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        """
        Method: Using Two-Pointer method.
                Let the first pointer move one step at a time, and the second pointer move two steps at a time.
                Check if head.next and head.next.next exist.
                While fast and fast.next exist, we keep moving two pointers and check they are equal.
        """
        if not head:
            return False
        
        if head.next and head.next.next:
            slow = head.next
            fast = head.next.next
        
            while fast and fast.next:
                if slow == fast:
                    return True
                else:
                    slow = slow.next
                    fast = fast.next.next
        else:
            return False
        
        return False
    
    
    """
    Same method with less code
    """
		if not head:
		    return False
		fast, slow = head, head
		# don' t need to check the slow pointer because the fast pointer can reach to the end of the list faster 
		# if the list does't have a cycle.  
		while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
		return False

