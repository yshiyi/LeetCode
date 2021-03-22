# Hash Table
<!-- GFM-TOC -->
* [Leetcode Hash Table](#Hash-Table)
    * [1. The Principle of Builtin Hash Table](#1-The-Principle-of-Builtin-Hash-Table)
    * [2. Remove or remove elements within array](#2-Remove-or-remove-elements-within-array)
    * [3. Two pointers](#3-Two-pointers)
    * [4. Peak and valley](#4-Peak-and-valley)
    * [5. Use some particular functions](#5-Use-some-particular-functions)
<!-- GFM-TOC -->

## 1. The Principle of Builtin Hash Table
The typical design of built-in hash table is:
  1. The key value can be any hashable type. And a value which belongs to a hashable type will have a hashcode. 
     This code will be used in the mapping function to get the bucket index.\
  2. Each bucket contains an array to store all the values in the same bucket initially.\
  3. If there are too many values in the same bucket, these values will be maintained in a height-balanced binary 
     search tree instead.\

The average time complexity of both insertion and search is still O(1). And the time complexity in the worst case is O(logN) 
for both insertion and search by using height-balanced BST. It is a trade-off between insertion and search.
