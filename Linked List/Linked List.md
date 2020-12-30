# Linked List
<!-- GFM-TOC -->
* [Leetcode Linded List](#Leetcode Linded List)
    * [1. Determine if the linked list has a cycle in it](#1-Determine if the linked list has a cycle in it)
<!-- GFM-TOC -->

##  1. Determine if the linked list has a cycle in it
[141\. Linked List Cycle (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.py)
**Description:**\
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.\
**Method:** \
Using Two-Pointer method.
Let the first pointer move one step at a time, and the second pointer move two steps at a time.
Check if head.next and head.next.next exist.
While fast and fast.next exist, we keep moving two pointers and check they are equal.
```
if not head:
    return False
fast, slow = head, head
while fast and fast.next:
         fast = fast.next.next
         slow = slow.next
         if fast == slow:
             return True
return False
'''
