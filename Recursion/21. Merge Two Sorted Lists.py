# This is a recursive approach
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
        ans = ListNode(None)
        self.l = ans
        def recurMerge(l1, l2):
            if l1 is None:
                self.l.next = l2
                return
            if l2 is None:
                self.l.next = l1
                return
            if l1.val <=l2.val:
                self.l.next = l1
                self.l = self.l.next
                recurMerge(l1.next, l2)
            else:
                self.l.next = l2
                self.l = self.l.next
                recurMerge(l1, l2.next)
            
        recurMerge(l1, l2)
        return ans.next
        
