# Linked List
This is a brief summary of the linked list and all the problems in this folder.

## What is a linked list?

Each node in a singly-linked list contains not only the value but also a reference field (or a pointer) to link to the next node. 
By this way, the singly-linked list organizes all the nodes in a sequence.

Unlike the array, we are not able to access a random element in a singly-linked list in constant time. 
If we want to get the ith element, we have to traverse from the head node one by one. 
It takes us O(N) time on average to visit an element by index, where N is the length of the linked list.

Like arrays, linked lists are used to represent sequential data. 
The benefit of linked lists is that insertion and deletion from anywhere in the list is O(1) 
whereas in arrays the following elements will have to be shifted.


## Singly Linked List 
### Add Operation - Singly Linked List
If we want to add a new value after a given node prev, we should: 
prev|prev.field  ->  cur|cur.field  ->  next|next.field
    1. Initialize a new node cur with the given value;
    2. Link the "next" field of cur to prev's next node next;
    3. Link the "next" field in prev to cur.
Unlike an array, we don’t need to move all elements past the inserted element. 
Therefore, you can insert a new node into a linked list in O(1) time complexity, which is very efficient.

%%%% Add a Node at the Beginning %%%%
As we know, we use the head node head to represent the whole list.
So it is essential to update head when adding a new node at the beginning of the list.
    1. Initialize a new node cur;
    2. Link the new node to our original head node head.
    3. Assign cur to head.
For example, let's add a new node 9 at the beginning of the list.
9  ->  23  ->  6  ->  15
    1. We initialize a new node 9 and link node 9 to current head node 23.
    2. Assign node 9 to be our new head


### Delete Operation - Singly Linked List
If we want to delete an existing node cur from the singly linked list, we can do it in two steps:
prev|prev.field  ->  cur|cur.field  ->  next|next.field
    * Find cur's previous node prev and its next node next
    * Link prev to cur's next node next
In our first step, we need to find out prev and next. It is easy to find out next using the reference field of cur. 
However, we have to traverse the linked list from the head node to find out prev which will take O(N) time on average, 
where N is the length of the linked list. So the time complexity of deleting a node will be O(N).
The space complexity is O(1) because we only need constant space to store our pointers.


%%%% Delete the first Node %%%%
If we want to delete the first node, the strategy will be a little different.
As we mentioned before, we use the head node head to represent a linked list. Our head is the black node 23 in the example below.
23  ->  6  ->  15
If we want to delete the first node, we can simply assign the next node to head. That is to say, our head will be node 6 after deletion.
The linked list begins at the head node, so node 23 is no longer in our linked list.


## Two-Pointer in Linked List
Imagine there are two runners with different speed. If they are running on a straight path, the fast runner will first arrive at the destination. 
However, if they are running on a circular track, the fast runner will catch up with the slow runner if they keep running.
  1. If there is no cycle, the fast pointer will stop at the end of the linked list.
  2. If there is a cycle, the fast pointer will eventually meet with the slow pointer.
It is a safe choice to move the slow pointer one step at a time while moving the fast pointer two steps at a time. 
For each iteration, the fast pointer will move one extra step. 
If the length of the cycle is M, after M iterations, the fast pointer will definitely move one more cycle and catch up with the slow pointer.

%%%% Tips %%%%
When we want to determine a particular node in a list, we need to use two-pointer method.
The fast pointer can move one more or n more steps ahead the slow pointer.
They can also redirect back to the head, when they reach the end of the list.

There are severl things we should pay attention:
    1. Always examine if the node is null before you call the next field.
        Getting the next node of a null node will cause the null-pointer error. 
        For example, before we run fast = fast.next.next, we need to examine both fast and fast.next is not null.
    2. Carefully define the end conditions of your loop.
        Run several examples to make sure your end conditions will not result in an endless loop. 
        And you have to take our first tip into consideration when you define your end conditions.


## Doubly Linked List
The doubly linked list works in a similar way but has one more reference field which is known as the "prev" field. 
With this extra field, you are able to know the previous node of the current node.

We can access data in the same exact way as in a singly linked list:
    1. We are not able to access a random position in constant time.
    2. We have to traverse from the head to get the i-th node we want.
    3. The time complexity in the worse case will be O(N), where N is the length of the linked list.


### Add Operation - Doubly Linked List
If we want to insert a new node cur after an existing node prev, we can divide this process into two steps:
23  ->  6  ->  15,   add 9 between 6 and 15
    1. link cur with prev and next, where next is the original next node of prev;
        9  ->  15
    2. re-link the prev and next with cur.
        23  ->  6  ->  9  ->  15
Similar to the singly linked list, both the time and the space complexity of the add operation are O(1).


### Delete Operation - Singly Linked List
If we want to delete an existing node cur from the doubly linked list, 
we can simply link its previous node prev with its next node next.
Since we no longer need to traverse the linked list to get the previous node, 
both the time and space complexity are O(1).

Note: Unlike the singly linked list, it is easy to get the previous node in constant time with the "prev" field.



## Review
Let's briefly review the performance of the singly linked list and doubly linked list.

They are similar in many operations:
    1. Both of them are not able to access the data at a random position in constant time.
    2. Both of them are able to add a new node after given node or at the beginning of the list in O(1) time.
    3. Both of them are able to delete the first node in O(1) time.

But it is a little different to delete a given node (including the last node).
    1. In a singly linked list, it is not able to get the previous node of a given node 
       so we have to spend O(N) time to find out the previous node before deleting the given node.
    2. In a doubly linked list, it will be much easier because we can get the previous node with 
       the "prev" reference field. So we can delete a given node in O(1) time.





