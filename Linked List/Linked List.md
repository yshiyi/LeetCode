# Linked List
<!-- GFM-TOC -->
* [Leetcode Linded List](#Leetcode-Linded-List)
    * [1. Determine if the linked list has a cycle in it](#1-Determine-if-the-linked-list-has-a-cycle-in-it)
    * [2. Determine the intersection of two linked lists](#2-Determine-the-intersection-of-two-linked-lists)
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
And move both pointers together. When they meet again, the meeting node will be the connection node.
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

##  2. Determine the intersection of two linked lists
[160. Intersection of Two Linked Lists (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/160.%20Intersection%20of%20Two%20Linked%20Lists.py)\
**Description:**\
Write a program to find the node at which the intersection of two singly linked lists begins.
```html
A:          a1 → a2
                    ↘
                      c1 → c2 → c3
                    ↗
B:    b1 → b2 → b3
```
**Method 1: Hash Table**\
Create only one set, traverse list A first and save all the nodes in A in the set.\
Then check every node in list B. If there is any node appears in the set, then that node is the intersection.\
Time complexity: O(m+n)\
Space complexity: O(m) or O(n)\
**Method 2: Two pointers**
<pre>
|<-  a  ->|<-  b  ->|
                     <-  c  ->|
          |<-  b  ->|
</pre>
If there is an intersection, then the travelled distance of two pointers should be the same.
From the figure, we can see that the only way that two pointers can meet together is that they travel through a + 2b + c.
Specifically, when p1 reaches the end of list A, it goes back to the head of list B. Do the same to p2.
Eventually, p1 will travel through a + b + c + b, and p2 will travel through b + c + a + b.
We need to recorde the end of each list. If the end is not the same, then there is no intersection.
```
if not headA or not headB:
   return None
pA, pB = headA, headB
lastA, lastB = None, None
while pA != pB:
   if pA:
       pA = pA.next
   else:
       lastA = pA
       pA = headB

   if pB:
       pB = pB.next
   else:
       lastB = pB
       pB = headA

   if lastA and lastB:
       if lastA != lastB:
           return None
return pA
```
