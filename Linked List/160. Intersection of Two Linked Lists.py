"""
160. Intersection of Two Linked Lists
Linked List

Description:
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
      a1 -> a2
               -> c1 -> c2 -> c3
b1 -> b2 -> b3

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

Similar Questions:
Minimum Index Sum of Two Lists - Easy
"""


# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        Method 1: Hash Table
                  Create two sets and traverse list A and list B. 
                  If node a appears in SetB or node b appears in SetA, then that node is the intersection.
                  Time complexity: O(m+n)
                  Space complexity: O(m+n)
                  
                  Create only one set and traverse list A first.
                  Then check every node in list B. If there is any node appears in the set, then that node is the intersection.
                  Time complexity: O(m+n)
                  Space complexity: O(m) or O(n)
        """
        SetA = set()
        SetB = set()
        nodeA, nodeB = headA, headB
        while nodeA or nodeB:
            if nodeA not in SetB:
                SetA.add(nodeA)
            else:
                return nodeA
            if nodeA:
                nodeA = nodeA.next
            
            if nodeB not in SetA:
                SetB.add(nodeB)
            else:
                return nodeB
            if nodeB:
                nodeB = nodeB.next
        return None
        
        
        """
        Method 2: Two pointers
                  |<-  a  ->|<-  b  ->|
                                       <-  c  ->|
                            |<-  b  ->|
                  If there is an intersection, then the travelled distance of two pointers should be the same.
                  From the figure, we can see that the only way that two pointers can meet together is that they travel through a + 2b + c.
                  Specifically, when p1 reaches the end of list A, it goes back to the head of list B. Do the same to p2.
                  Eventually, p1 will travel through a + b + c + b, and p2 will travel through b + c + a + b.
                  We need to recorde the end of each list. If the end is not the same, then there is no intersection.
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        lastA, lastB = None, None
        while pA != pB:
            if pA:
                pA = pA.next
            else:
                lastA = pA
                pA = headB
            
            if pB:
                pB = pB.next
            else:
                lastB = pB
                pB = headA
            
            if lastA and lastB:
                if lastA != lastB:
                    return None
        return pA
        
        
