"""
142. Linked List Cycle II
Linked List, Two Pointers

Description:
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Notice that you should not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Similar Questions:
Linked List Cycle - Easy
Find the Duplicate Number - Medium
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Method 1: Brute force method, using hash table
                  We iteratively go through all the nodes in the list. 
                  If the node has been seen before, then there is a cycle and the connection node is detected.
        """
        if not head:
            return None
        
        Set = set()
        current = head
        Set.add(current)
        while current.next:
            current = current.next
            if current in Set:
                return current
            Set.add(current)
        return None
        
        if not head:
            return None
        Set = set()
        current = head
        while current.next:
            if current in Set:
                return current
            Set.add(current)
            current = current.next
        return None
        
        %%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%
        """
        Method 2: Two Pointers
                            p1        p2
                            |         |
                            v         v
                  |<-  a  ->|<-  b  ->|<-  ---  ->|
                            |<-       c         ->|
                  a: No. of steps from beginning to the connection point
                  b: No. of steps from connection point to the meeting point
                  c: length of a full cycle
                  The travelled steps of pointer 1 is N = a + b (or + n1*c)
                  The travelled steps of pointer 2 is 2*N = a + b + n2*c = 2*a + 2*b (or + 2n1*c)
                  ==> a + b = (n2 - 2*n1) * c
                  Notice that a + b is equal to the length of cycle times an integer.
                  It means if we start move from p2 by a steps, we will reach to p1.
                  
                  Therefore, we use two pointers to check if there is a cycle.
                  If there is one, we then reset pointer 1 back to the starting point and let pointer 2 stay at p2.
                  And move both pointers together. When they meet again, the meeting node will be the connection node.
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
        
        # ''''''
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                counter = 0
                p1, p2 = head, fast
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                    counter += 1
                return p1
        return None
        
        

