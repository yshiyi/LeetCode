# This is a recursive solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        head2 = ListNode(0)
        
        def recurReverse(head, head2):
            if head is None:
                return head
            temp1, temp2 = head.next, head2.next
            head2.next = head
            head.next = temp2
            recurReverse(temp1, head2)
            return head2
        
        head2 = recurReverse(head, head2)
        return  head2.next
