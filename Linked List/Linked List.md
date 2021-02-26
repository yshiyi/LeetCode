# Linked List
<!-- GFM-TOC -->
* [Leetcode Linded List](#Leetcode-Linded-List)
    * [1. Determine if the linked list has a cycle in it](#1-Determine-if-the-linked-list-has-a-cycle-in-it)
    * [2. Determine the intersection of two linked lists](#2-Determine-the-intersection-of-two-linked-lists)
    * [3. Remove element from linked list](#3-Remove-element-from-linked-list)
    * [4. Merge two sorted linked lists](#4-Merge-two-sorted-linked-lists)
    * [5. Reverse linked list](#5-Reverse-linked-list)
    * [6. Reverse nodes in pairs or groups](#6-Reverse-nodes-in-pairs-or-groups)
    * [7. Add two numbers](#7-Add-two-numbers)
    * [8. Remove duplicates from sorted list](#8-Remove-duplicates-from-sorted-list)
    * [9. Copy list with random pointer](#9-Copy-list-with-random-pointer)
    * [10. Odd even linked list](#10-Odd-even-linked-list)
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

[61. Rotate List (medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/61M.%20Rotate%20List.py)\
**Description:**\
Given the head of a linked list, rotate the list to the right by k places.\
Example:\
Input: head = [1,2,3,4,5], k = 2\
Output: [4,5,1,2,3]

**Method 1:**\
Using the similar idea of 189M. Rotate Array\
First, convert the linked list to an array/a list.
Rotate this array by k times, elements will be moved to (i + k) % L position.
Finally, convert the rotated list to a new linked list.

```
l = []
while head:
   l.append(head.val)
   head = head.next

L = len(l)
l_new = [0 for _ in range(L)]  # [0] * L
for i in range(L):
   l_new[(i + k) % L] = l[i]

cur = ans = ListNode()
for i in range(L):
   newNode = ListNode(l_new[i])
   cur.next = newNode
   cur = cur.next
return ans.next
```

**Method 2:**\
Create a cycle link by linking the last to node of the list to the first node.
Move n-k-1 steps to make the pointer points to the last node in the rotated link.
Fianlly, let the cur2.next = None to terminate the cycle.

```
if head is None or head.next is None:
   return head

n = self.getLen(head)
if k % n == 0:
   return head
elif k > n:
   k = k % n

cur = head
while cur.next:
   cur = cur.next
cur.next = head
cur2 = head

for _ in range(n - k - 1):
   cur2 = cur2.next
head = cur2.next
cur2.next = None

return head
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
**Description:**\
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
**Description:**\
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
[24. Swap Nodes in Pairs (medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/24M.%20Swap%20Nodes%20in%20Pairs.py)\
**Description:**\
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

[25. Reverse Nodes in k-Group (hard)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/25H.%20Reverse%20Nodes%20in%20k-Group.py)\
**Description:**\
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

##  7. Add two numbers
[2. Add Two Numbers (medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/2M.%20Add%20Two%20Numbers.py)\
**Description:**\
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.\
Example:\
Input: l1 = [2,4,3], l2 = [5,6,4]\
Output: [7,0,8]\
Explanation: 342 + 465 = 807.

**Method 1:**\
Elementary math\
Create a new list to hold the result of summation.
Define a new variable carry. If the summation is greater or equal to 10, then carry = 1, otherwise carry = 0.
The result of summation is equal to the sum of each node val and carry.

```
carry = 0
ans = ListNode(None)
self.l = ans
while l1 and l2:
   val = l1.val + l2.val + carry
   carry = self.addTwo(val)
   l1 = l1.next
   l2 = l2.next

if l1:
   while l1:
       val = l1.val + carry
       carry = self.addTwo(val)
       l1 = l1.next
elif l2:
   while l2:
       val = l2.val + carry
       carry = self.addTwo(val)
       l2 = l2.next
if carry == 1:
   newNode = ListNode(carry)
   self.l.next = newNode
   self.l = self.l.next
return ans.next
```

**Method 2:**\
First, we convert both lists to decimal numbers.
Then find out the length of this number by using len(str(num)).
Finally, we save each of the digit to a new list.


[445. Add Two Numbers II (medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/445M.%20Add%20Two%20Numbers%20II.py)\
**Description:**\
Similar to 2M. Add Two Numbers. But this time, two numbers are added from the right.\
Follow up:\
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.\

Example:\
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)\
Output: 7 -> 8 -> 0 -> 7

**Method:**\
Convert two lists to two integers. Then convert the summation of these two integers to a new linked list.

```
num1 = self.convertToNum(l1)
num2 = self.convertToNum(l2)
num = num1 + num2
ans = ListNode(None)
cur = ans

nums = str(num)
L = len(nums)
for i in range(L):
   newNode = ListNode(nums[i])
   cur.next = newNode
   cur = cur.next
return ans.next
```

##  8. Remove duplicates from sorted list
[83. Remove Duplicates from Sorted List (easy)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/83.%20Remove%20Duplicates%20from%20Sorted%20List.py)\
**Description:**\
Given a sorted linked list, delete all duplicates such that each element appear only once.\
Example:\
Input: 1->1->2->3->3\
Output: 1->2->3

**Method:**
Brute force\
Create two pointers. We move the first pointer in the main loop.
If the second pointer points to a duplicate, we then skip that node and keep moving it until we reach to a new node.
Then we link the first pointer to the second by cur.next = cur2.

```
if head is None or head.next is None:
   return head

cur = head
while cur:
   cur2 = cur

   while cur2 and cur2.val == cur.val:
       cur2 = cur2.next
   cur.next = cur2
   cur = cur.next
return head
```

[82. Remove Duplicates from Sorted List II (medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/82M.%20Remove%20Duplicates%20from%20Sorted%20List%20II.py)\
**Description:**\
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.\

Example:\
Input: 1->2->3->3->4->4->5\
Output: 1->2->5

**Method 1:**\
Two pointers\
Create a dummy head before the linked list to avoid duplicate beginnings.
The first pointer points to the distinct node. The second pointer swaps through the whole list.
Let the second pointer start from the original head. Just keep moving the second pointer. When the second pointer reaches the end of the list of duplicates, we move the first pointer.\

```
if head is None or head.next is None:
   return head
head2 = ListNode(None)
head2.next = head
cur1, cur2 = head2, head
while cur2:
   if cur2.next and cur2.val == cur2.next.val:
       while cur2.next and cur2.val == cur2.next.val:
           cur2 = cur2.next
       cur1.next = cur2.next
   else:
       cur1 = cur1.next
   cur2 = cur2.next

return head2.next
```

**Method 2:**
Hash Table\
Swap through the whole list first, and save the duplicates in a set.
Then start the beginning of the list again.
Link the nodes which are not contained in the set.\

```
curr=head
dup=set()
while curr and curr.next:
   if curr.val==curr.next.val:
       dup.add(curr.val)
   curr=curr.next
dummy=ListNode(0)
dummy.next=head
curr=dummy
while curr and curr.next:
   if curr.next.val in dup:
       curr.next=curr.next.next
   else:
       curr=curr.next
return dummy.next
```

##  9. Copy list with random pointer
[138. Copy List with Random Pointer (medium)](https://github.com/yshiyi/LeetCode/blob/157d4db3d488a7496f1fd273dc5528a4c058b197/Linked%20List/138M.%20Copy%20List%20with%20Random%20Pointer.py)\
**Description:**
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:
* val: an integer representing Node.val
* random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

Example:\
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]\
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

**Method 1:**\
Iterative method\
Create a global dictionary self.visitedDict to check if the node has already been copied. The keys are the old node and values are the new node. Then swap through the whole list.\
We copy the current node in the original list. We then copy the next and random from the original. Since we have already created the next node, we can directly move to that node.

```
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
   new_head = self.copyNode(cur)
   cur2 = new_head
   while cur:
      cur2.next = self.copyNode(cur.next)
      cur2.random = self.copyNode(cur.random)
      cur = cur.next
      cur2 = cur2.next

   return new_head
```

**Method 2:**\
Recursive method\
In the recursive function, we first need to check if the node is none. If so, then return none.\
Then we check if this node has already been copied before, i.e., in the self.visitedDict. If it is in the dictionary, then return the value. If it is not, create a newnode with the head.val and call the recursive function to copy the next and random.\
This recursive function will eventually swap through all the nodes in the original list.

```
def copyRandomList(self, head):
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
```

##  10. Odd even linked list
[328. Odd Even Linked List (medium)](https://github.com/yshiyi/LeetCode/blob/main/Linked%20List/328M.%20Odd%20Even%20Linked%20List.py)\
**Description:**\
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:\
Input: 1->2->3->4->5->NULL\
Output: 1->3->5->2->4->NULL

**Method 1:**
Two pointers\
Create a variable to count the position.
When the fast pointer reaches the even position, take out the next odd node.
Then incert this odd node to the next position to where the slow pointer points.

```
if head is None:
   return head
cur1, cur2 = head, head

p = 1
while cur2 and cur2.next:
   if p % 2 == 0:
       # Take out odd node
       temp = cur2.next
       # Incert node
       temp.next = cur1.next
       cur1.next = temp
       # Move both pointers
       cur1 = cur1.next
       cur2.next = cur2.next.next
       p += 1
   else:
       cur2 = cur2.next
       p += 1

return head
```

**Method 2:**\
Create two list.
Insert the odd nodes to the odd list and insert the even nodes to the even list.
Finally, link two list together.

```
if head is None:
   return head
odd, even = head, head.next
even_head = even
while even and even.next:
   odd.next = odd.next.next
   odd = odd.next
   even.next = even.next.next
   even = even.next
odd.next = even_head
return head
```






