'''
86M. Partition List

Description:
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

 
Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 
Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

# Method: Traverse the whole list twice. Must create a new node!
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        res = ListNode(-1)
        p = res
        p1 = head

        while p1:
            if p1.val < x:
                newNode = ListNode(p1.val)
                p.next = newNode
                p = p.next
            p1 = p1.next
        p1 = head
        while p1:
            if p1.val >=x:
                newNode = ListNode(p1.val)
                p.next = newNode
                p = p.next
            p1 = p1.next

        return res.next

