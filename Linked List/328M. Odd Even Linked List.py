"""
328. Odd Even Linked List
Linkded List

Description:
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Similar Question:
Split Linked List in Parts - Medium
"""

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """
        Method 1: Two Pointers
                  Create a variable to count the position.
                  When the fast pointer reaches the even position, take out the next odd node.
                  Then insert this odd node to the next position to where the slow pointer points.
        """
        if head is None:
            return head
        cur1, cur2 = head, head

        p = 1
        while cur2 and cur2.next:
            if p % 2 == 0:
                # Take out odd node
                temp = cur2.next
                cur2.next = cur2.next.next
                # Incert node
                temp.next = cur1.next
                cur1.next = temp
                # Move both pointers
                cur1 = cur1.next
                p += 1
            else:
                cur2 = cur2.next
                p += 1
            
        return head
        
        """
        Method 2: Create two list
                  Insert the odd nodes to the odd list and insert the even nodes to the even list.
                  Finally, link two list together.
        """
        if head is None:
            return head
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
        
        # -------- #
        oddHead, evenHead = head, head.next
        odd, even = oddHead, evenHead
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        return oddHead
        
        
        
