# This is a recursive approach
class Solution(object):
    def swapPairs(self, head):
        # Method 1
        def recurSwap(head):
            if head is None or head.next is None:
                return head
            temp = head.next.next
            head2 = head.next
            head2.next = head
            head.next = recurSwap(temp)
            return head2
        return recurSwap(head)
      
        # Method 2
        if head is None or head.next is None:
            return head
        temp = head.next.next
        head2 = head.next
        head2.next = head
        head.next = self.swapPairs(temp)
        return head2
