"""
138. Copy List with Random Pointer
Hash Table, Linked List

Description:
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) where random pointer points to, 
                  or null if it does not point to any node.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Example 4:
Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.

Similar Questions:
Clone Graph - Medium
Clone Binary Tree With Random Pointer - Medium
Clone N-ary Tree - Medium
"""

# Solution:

# Definition for a Node.
# class Node:
#     def __init__(self, x, next=None, random=None):
#         self.val = int(x)
#         self.next = next
#         self.random = random

"""
Method 1: Iterative method
          Create a global dictionary self.visitedDict to check if the node has already been copied.
          The keys are the old node and values are the new node.
          Then swap through the whole list.
"""
class Solution(object):
    def __init__(self):
        self.visitedDict = {}
    
    def copyNode(self, node):
        if node is None:
            return None
        if node in self.visitedDict:
            return self.visitedDict[node]
        else:
            newNode = Node(node.val, None, None)
            self.visitedDict[node] = newNode
            return newNode
    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = head
        
        """
        First approach: Create a dummy head, and create a copy of each node in the original list.
                        Link this copied node to the new_head.
                        Return new_head.next in the end.
                        This approach takes about 40 - 44 ms.
        """
        new_head = Node(0, None, None)
        cur2 = new_head
        while cur:
            newNode = self.copyNode(cur)
            newNode.next = self.copyNode(cur.next)
            newNode.random = self.copyNode(cur.random)
            cur2.next = newNode
            cur = cur.next
            cur2 = cur2.next
        return new_head.next
        
        """
        Second approach: We copy the current node in the original list.
                         We then copy the next and random from the original.
                         Since we have already created the next node, we can directly move to that node.
                         This approach takes about 32 ms.
        """
        new_head = self.copyNode(cur)
        cur2 = new_head
        while cur:
            cur2.next = self.copyNode(cur.next)
            cur2.random = self.copyNode(cur.random)
            cur = cur.next
            cur2 = cur2.next
        
       return new_head


"""
Method 2: Recursive method
          Create a global dictionary self.visitedDict to check if the node has already been copied.
          The keys are the old node and values are the new node.
          In the recursive function, we first need to check if the node is none. If so, then return non.
          Then we check if this node has already been copied before, i.e., in the self.visitedDict.
          If it is in the dictionary, then return the value.
          If it is not, create a newnode with the head.val and call the recursive function to copy the next and random.
          This recursive function will eventually swap through all the nodes in the original list.
"""
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        if head is None:
            return head
        
        if head in self.visitedDict:
            return self.visitedDict[head]
        else:
            # newNode = self.copyNode(head)
            newNode = Node(head.val, None, None)
            self.visitedDict[head] = newNode
            newNode.next = self.copyRandomList(head.next)
            newNode.random = self.copyRandomList(head.random)
            
            return newNode
