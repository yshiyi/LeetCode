# Linked List
<!-- GFM-TOC -->
* [Leetcode Linded List](#Leetcode-Linded-List)
    * [1. Determine if the linked list has a cycle in it](#1-Determine-if-the-linked-list-has-a-cycle-in-it)
    * [2. Determine the intersection of two linked lists](#2-Determine-the-intersection-of-two-linked-lists)
    * [3. Remove element from linked list](#3-Remove-element-from-linked-list)
    * [4. Merge two sorted linked lists](#4-Merge-two-sorted-linked-lists)
    * [5. Reverse linked list](#5-Reverse-linked-list)
    * [6. Reverse nodes in pairs or groups](#6-Reverse-nodes-in-pairs-or-groups)
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

##  3. Remove element from linked list
[203. Remove Linked List Elements (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/203.%20Remove%20Linked%20List%20Elements.py)\
**Description:**\
Remove all elements from a linked list of integers that have value val.\
Example:\
Input:  1->2->6->3->4->5->6, val = 6\
Output: 1->2->3->4->5\

**Method:**
To remove a node from linked list, we need to implement current.next = current.next.next.
The condition is to check if current.next has a value and that value is equal to val.
The second step, we need to consider the first node of the list.
So, we create a while loop to check the head.val.

```
if head is None:
   return head
while head and head.val == val:
   head = head.next
curr = head
while curr:
   if curr.next and curr.next.val == val:
       curr.next = curr.next.next
   else:
       curr = curr.next
return head
```

[19. Remove Nth Node From End of List (Medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/19M.%20Remove%20Nth%20Node%20From%20End%20of%20List.py)\
**Description:**
Given the head of a linked list, remove the nth node from the end of the list and return its head.\
Follow up: Could you do this in one pass?\
Example:\
Input: head = [1,2,3,4,5], n = 2\
Output: [1,2,3,5]\

**Method 1: Two passes**\
In the first pass, we obtain the length of the list, Len.\
In the second pass, we remove the number at Len - n. We need to move to one before the target number, at Len - n - 1.\
Then node.next = node.next.next.\
Note, if Len - n == 0, means remove the head, then return head.next.\

**Method 2: Two pointers**\
Move the first pointer n steps ahead.
Then move both pointers together and remain the gap n.
When the first pointer reaches the last node, then p2.next = p2.next.next.
Note, when p1 finishes moving n steps, we need to check if p1 is none.
If it is, then it means to remove the head.

```
p1, p2 = head, head
for _ in range(n):
   p1 = p1.next
if p1 is None:
   return head.next
while p1.next:
   p1 = p1.next
   p2 = p2.next
p2.next = p2.next.next
return head
```

##  4. Merge two sorted linked lists
[21. Merge Two Sorted Lists (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/21.%20Merge%20Two%20Sorted%20Lists.py)\
**Description:**\
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.\
Example:\
Input: l1 = [1,2,4], l2 = [1,3,4]\
Output: [1,1,2,3,4,4]\

**Method:**\
Using the similar idea with merge sorted array.
Create a new list to hold the nodes and two pointers to traverse l1 and l2.
Compare each node from l1 and l2, and save the smaller one to the new list.
When reach the end of one of the list, we add the rest of nodes of the other list to the end of the new list.

```
ans = ListNode(None)
l = ans
while l1 and l2:
   if l1.val <= l2.val:
       l.next = l1
       l1 = l1.next  # temp
   else:
       l.next = l2
       l2 = l2.next  # temp
   l = l.next

if l1 is None and l2:
   l.next = l2
   return ans.next
elif l1 and l2 is None:
   l.next = l1
   return ans.next
else:
   return ans.next
```

##  5. Reverse linked list
[206. Reverse Linked List (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/206.%20Reverse%20Linked%20List.py)\
**Description:**
Reverse a singly linked list.\
Example:\
Input: 1->2->3->4->5->NULL\
Output: 5->4->3->2->1->NULL

**Method:** 
Note, if we let temp = current and current = temp.next, then when we modify current, we also modify temp.
But, if we let temp = current.next, then the changes on current won't affect temp.

```
# Iterative method
head2 = None
current = head
while current:
   temp = current.next
   current.next = head2
   head2 = current
   current = temp
return head2
```
```
# Recursive method
   self.head2 = None
   return self.CreateRev(head)

def CreateRev(self, head):
   if head:
      temp = head.next
      head.next = self.head2
      self.head2 = head
      head = temp
   else:
      return
   self.CreateRev(head)
   return self.head2
```

[234. Palindrome Linked List (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/234.%20Palindrome%20Linked%20List.py)\
**Description:**
Given a singly linked list, determine if it is a palindrome (e.g., 1-2-1, 1-2-2-1).\
Follow up: Could you do it in O(n) time and O(1) space?\

**Method 1: Two Pointers**\
Create two pointers.
One moves two steps and the other moves one step per iteration. So, we can determine the middle point.
Then, we reverse the second part of the list and compare it with the first half.

```
fast, slow = head, head
while fast and fast.next:
   fast = fast.next.next
   slow = slow.next

head2 = None
while slow:
   temp = slow.next
   slow.next = head2
   head2 = slow
   slow = temp

while head and head2:
   if head.val != head2.val:
       return False
   head = head.next
   head2 = head2.next
return True
```

**Method 2:**\
Create a list to hold the values of the list.
Then use nodes[::-1] == nodes to compare values from beginning and end.

```
nodes=[]
while head:
   nodes.append(head.val)
   head=head.next
return nodes[::-1]==nodes
```

##  6. Reverse nodes in pairs or groups
[24. Swap Nodes in Pairs (Medium)] (https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/24M.%20Swap%20Nodes%20in%20Pairs.py)\
[234. Palindrome Linked List (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/234.%20Palindrome%20Linked%20List.py)\
**Description:**
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes. Only nodes itself may be changed.\
Example:\
Input: head = [1,2,3,4]\
Output: [2,1,4,3]

**Method 1:**
Using only one pointer and create a new list. Check cur and cur.next, and save nodes to the new list.

```
cur2 = head2
cur1 = head
while cur1 and cur1.next:
   temp = cur1.next.next
   cur2.next = cur1.next
   cur2 = cur2.next
   cur2.next = cur1
   cur2 = cur2.next
   cur2.next = temp
   cur1 = temp
        
return head2.next
```

**Method 2:**
Recursive method

```
def swapPairs(self, head):
   if not head or not head.next: 
      return head

   nextTemp = head.next
   nextnextTemp = head.next.next

   nextTemp.next = head
   head.next = self.swapPairs(nextnextTemp)

   return nextTemp
```

[25. Reverse Nodes in k-Group (hard)] (https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/25H.%20Reverse%20Nodes%20in%20k-Group.py)\
**Description:**
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.\
Follow up:\
Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.\
Example:\
Input: head = [1,2,3,4,5], k = 2\
Output: [2,1,4,3,5]

**Method:**
Using the similar idea of recursive method in 24M. Swap Nodes in Pairs\
We first reverse the first k nodes and save them to a new list.
Then send the rest of the list back to the recursive function.
Note, we can't use global self.head2. It will save the nodes in front of it rather than in the end.

```
def reverseKGroup(self, head, k):
   L = self.getLen(head)

   if L < k:
      return head

   head2 = None
   count = k
   while head and count:
      temp = head.next
      head.next = head2
      head2 = head
      head = temp
      count -= 1

   cur = head2
   while cur.next:
      cur = cur.next

   cur.next = self.reverseKGroup(head, k)
   return head2
```


