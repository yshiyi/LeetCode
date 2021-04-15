# Binary Tree
<!-- GFM-TOC -->
* [Leetcode Binary Tree](#Binary-Tree)
    * [1. Introduction to Binary Tree](#1-Introduction-to-Binary-Tree)
       * [1.1 Pre order Traversal](#11-Pre-Order-Traversal)
       * [1.2 In order Traversal](#12-In-Order-Traversal)
       * [1.3 Post order Traversal](#13-Post-Order-Traversal)
       * [1.4 Breadth First Search](#14-Breadth-First-Search)
    * [2. Stack](#2-Stack)
       * [67. Add Binary](#67-Add-Binary)
    * [3. Two Pointers](#3-Two-Pointers)
       * [28. Implement strStr()](#28-Implement-strStr)
       * [344. Reverse String](#344-Reverse-String)
       * [9. Palindrome Number](#9-Palindrome-Number)
       * [167. Two Sum II](#167-Two-Sum-II)
       * [209M. Minimum Size Subarray Sum](#209M-Minimum-Size-Subarray-Sum)
    * [4. Hash Table](#4-Hash-Table)
       * [242. Valid Anagram](#242-Valid-Anagram)
       * [409. Longest Palindrome](#409-Longest-Palindrome)
       * [205. Isomorphic Strings](#205-Isomorphic-Strings)
    * [5. Others](#5-Others)
       * [14. Longest Common Prefix](#14-Longest-Common-Prefix)
       * [696. Count Binary Substrings](#696-Count-Binary-Substrings)
       * [561. Array Partition I](#561-Array-Partition-I)
       * [119. Pascal's Triangle II](#119-Pascals-Triangle-II)
       * [151M. Reverse Words in a String](#151M-Reverse-Words-in-a-String)
       * [557. Reverse Words in a String III](#557-Reverse-Words-in-a-String-III)
<!-- GFM-TOC -->

# 1. Introduction to Binary Tree
## 1.1 Pre Order Traversal
Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree. Here is an example:\
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
Preorder:F-B-A-D-C-E-G-I-H

## 1.2 In Order Traversal
In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.\
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
Inorder:A-B-C-D-E-F-G-H-I\
Typically, for binary search tree, we can retrieve all the data in sorted order using in-order traversal. 

## 1.3 Post Order Traversal
Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.\
<pre>
          F
      B       G
    A   D       I
       C E     H
</pre>
Inorder:A-C-E-D-B-H-I-G-F\
It is worth noting that when you delete nodes in a tree, deletion process will be in post-order. That is to say, when you delete a node, you will delete its left child and its right child before you delete the node itself.\
**Note:**\
Post-order is widely use in mathematical expression. It is easier to write a program to parse a post-order expression. Here is an example:
<pre>
          +
      *       5
    4   -       
       7 2     
</pre>
If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.























