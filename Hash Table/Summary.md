# Hash Table
<!-- GFM-TOC -->
* [Leetcode Hash Table](#Hash-Table)
    * [1. The Principle of Builtin Hash Table](#1-The-Principle-of-Builtin-Hash-Table)
    * [2. Hash Set](#2-Hash-Set)
    * [3. Hash Map](#3-Hash-Map)
    * [4. Design the key](#4-Design-the-key)
    * [5. Use some particular functions](#5-Use-some-particular-functions)
<!-- GFM-TOC -->

## 1. The Principle of Builtin Hash Table
The typical design of built-in hash table is:
  1. The key value can be any hashable type. And a value which belongs to a hashable type will have a hashcode. 
     This code will be used in the mapping function to get the bucket index.
  2. Each bucket contains an array to store all the values in the same bucket initially.
  3. If there are too many values in the same bucket, these values will be maintained in a height-balanced binary 
     search tree instead.

The average time complexity of both insertion and search is still O(1). And the time complexity in the worst case is O(logN) 
for both insertion and search by using height-balanced BST. It is a trade-off between insertion and search.

## 2. Hash Set
The hash set is one of the implementations of a set which is a data structure to store no repeated values. 
Therefore, typically, a hash set is used to check if a value has ever appeared or not.
```
Python
hashset = set() # Initialize a hash set
hashset.add(1)  # Add a new key
hashset.remove(1)  # Remove a key
hashset.clear  # Clear the hash set
```
```
C++
set<int> s;     // Initialize a hash set
s.insert(key);  // Insert a new key
s.erase(key); s.erase(s.begin());  // Remove a key from set
s.clear();      // Clear the hash set
```
## 3. Hash Map
The hash map is one of the implementations of a map which is used to store (key, value) pairs.\
Scenario I: When we need more information rather than only the key. Then we can build a mapping relationship between key and information by hash map.\
Scenario II: To aggregate all the information by key.
```
Python
hashmap = {}  # Initialize a hash map
hashmap.pop('key', None)  # Return hashmap['key'] if key exists in the dictionary, and None otherwise
del hashmap['key']  # To delete a key that is guaranteed to exist
hashmap['pi'] = 3.1415 # Create a new key
hashmap.clear()  # Clear the hash map
```
```
C++
map<int, int> m;  // Initialize a hash map, keys are automatically sorted.
unordered_map<int, int> unordered_m;  // Keys are not sorted.
m.insert(make_pair(key, val)); m[key] = val; // Create a new key with val;
m[key]++;         // If key is not in the map before, the corresponding value is initialized as 0;
m.erase(key); m.erase(m.begin()); // Remove a particular key
m.clear();        // Clear the hash map
m.find(key);      // Find a particular key, return an iterator if key exists. Otherwise, return m.end().
m.count(key);     // Count the appearances of key, useful for multimap.
```

## 4. Design the key
1. When the order of each element in the string/array doesn't matter, you can use the sorted string/array as the key.
   Keep in mind that a list can't be used as a key of a dictionary. We need to convert it to a string
2. If you only care about the offset of each value, usually the offset from the first value, you can use the offset as the key.\
   e.g., (x0, x1, x2) --> (x0-x0, x1-x0, x2-x0)
3. In a tree, you might want to directly use the TreeNode as key sometimes. But in most cases, the serialization of the subtree might be a better idea.
4. In a matrix, you might want to use the row index or the column index as key.
5. In a Sudoku, you can combine the row index and the column index to identify which block this element belongs to.\
   e.g., create a list contains 9 dictionaries
   ```
   Python
   rows = \[{} for i in range(9)\]\
   columns = \[{} for i in range(9)\]\
   boxes = \[{} for i in range(9)\]\
   ```
   ```
   C++
   vector<set<int>> v_row, v_col, v_box;
   v_row.resize(9);
   v_col.resize(9);
   v_box.resize(9);
   ```
6. Sometimes, in a matrix, you might want to aggregate the values in the same diagonal line.

