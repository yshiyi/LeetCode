'''


'''

# Solution:
'''
Method: Create a pointer in each list, and use a prioriy queue to save the values
        Pop the smallest one, and save it to the new list
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        cur = head
        q = []
        heapq.heapify(q)
        for l in lists:
            if l is not None:
                heapq.heappush(q, (l.val, l))
        while len(q) > 0:
            val, node = heapq.heappop(q)
            new_Node = ListNode(val)
            cur.next = new_Node
            cur = cur.next
            node = node.next
            if node is not None:
                heapq.heappush(q, (node.val, node))
        return head.next
