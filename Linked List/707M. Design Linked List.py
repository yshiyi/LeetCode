"""
707. Design Linked List
Linked List, Design

Description:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.


Implement the MyLinkedList class:
MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. 
                        After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. 
                                    If index equals the length of the linked list, the node will be appended to the end of the linked list. 
                                    If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

Similar Question:
Design Skiplist - Hard
"""

# Solution:
"""
707. Design Linked List
Linked List, Design

Description:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next.
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list.
Assume all nodes in the linked list are 0-indexed.


Implement the MyLinkedList class:
MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list.
                        After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
                                    If index equals the length of the linked list, the node will be appended to the end of the linked list.
                                    If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

Similar Question:
Design Skiplist - Hard
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for i in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return

        current = self.head
        # Create a new node with the desired value.
        newNode = ListNode(val)
        
        # If we add a new node as the head, then we make the newnode.next point to the current head.
        # And assign the newnode as the head, self.head.
        if index <= 0:
            newNode.next = current
            self.head = newNode
        else:
            # If we want to add a node into the list, we need to first link the newNode.next to the current.next.
            # And link the current.next to the new node.
            # Note, current node is the one before the desired index.
            for i in range(index - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode

        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return -1

        current = self.head
        
        # If we want to remove the head, we just simply assign current.next as the new head.
        if index == 0:
            self.head = current.next
        else:
            # If we want to remove a node from the list, we save the current node as the previous node.
            # And move to the next node by doing: current = current.next
            # Then we just simply link the previous.next to current.next.
            # Node, current is always pointing to the target index.
            for i in range(index):
                previous = current
                current = current.next
            previous.next = current.next
            # for i in range(index - 1):
            #     current = current.next
            # current.next = current.next.next
        self.size -= 1



obj = MyLinkedList()
param_1 = obj.get(1)
print(param_1)
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
print(obj.get(0), obj.get(1), obj.get(2))  # 1, 2, 3
obj.deleteAtIndex(1)
print(obj.get(0), obj.get(1), obj.get(2))  # 1, 3


# MyLinkedList = LinkedList()
# print(MyLinkedList)

