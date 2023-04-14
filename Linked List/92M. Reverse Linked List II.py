'''
92M. Reverse Linked List II

Description:
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list. 

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 
Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''

# Method: First, consider reversing first N nodes in the list. Second, traverse the list until reaching the first node that needs to reverse.
class Solution(object):
    successor = None
    def reverseN(self, head, n):
        global successor
        if n == 1:
            successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = successor
        return last

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head
        
