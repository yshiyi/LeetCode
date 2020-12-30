# Linked List
<!-- GFM-TOC -->
* [Leetcode Linded List](#Leetcode-Linded-List)
    * [1. Determine if the linked list has a cycle in it](#1-Determine-if-the-linked-list-has-a-cycle-in-it)
    
<!-- GFM-TOC -->

##  1. Determine if the linked list has a cycle in it
[141\. Linked List Cycle (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/141.%20Linked%20List%20Cycle.py)\
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
```

[142M\. Linked List Cycle (Medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/142M.%20Linked%20List%20Cycle%20II.py)\
**Description:**\
Similar to 141, but this time we need to find to which the tail connects if there is a cycle in the linked list.\
**Method:** \
Two Pointers\
<pre>
          p1        p2\
          |         |\
          v         v\
|<-  a  ->|<-  b  ->|<-  ---  ->|\
          |<-       c         ->|\
</pre>
a: No. of steps from beginning to the connection point\
b: No. of steps from connection point to the meeting point\
c: length of a full cycle\
The travelled steps of pointer 1 is N = a + b (or + n1*c)\
The travelled steps of pointer 2 is 2*N = a + b + n2*c = 2*a + 2*b (or + 2n1*c) ==> a + b = (n2 - 2*n1) * c\
Notice that a + b is equal to the length of cycle times an integer.
It means if we start move from p2 by a steps, we will reach to p1.\
Therefore, we use two pointers to check if there is a cycle.
If there is one, we then reset pointer 1 back to the starting point and let pointer 2 stay at p2.
And move both pointers together. When they meet again, the meeting node will be the connection node.\
```
fast, slow = head, head
while fast and fast.next:
   slow = slow.next
   fast = fast.next.next
   if slow == fast:
       break
if not fast or not fast.next:
   return None
slow = head
while slow != fast:
   slow = slow.next
   fast = fast.next
return slow
```
