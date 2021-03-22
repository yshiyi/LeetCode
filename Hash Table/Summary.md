# Hash Table
<!-- GFM-TOC -->
* [Leetcode Hash Table](#Hash-Table)
   * [1. The Principle of Builtin Hash Table](#1-The-Principle-of-Builtin-Hash-Table)   
   * [2. Hash Set](#2-Hash-Set)
   * [3. Hash Map](#3-Hash-Map)
   * [4. Design the key](#4-Design-the-key)
   * [5. Sliding Window](#5-Sliding-Window)
       * [219. Contains Duplicate II](#219-Contains-Duplicate-II)
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
   e.g., (x0, x1, x2) --> (x0-x0, x1-x0, x2-x0), [249M.Group Shifted Strings (Python)](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/249M.%20Group%20Shifted%20Strings.py), [249M.Group Shifted Strings (C++)](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/249M.%20Group%20Shifted%20Strings.cpp)
3. In a tree, you might want to directly use the TreeNode as key sometimes. But in most cases, the serialization of the subtree might be a better idea.
4. In a matrix, you might want to use the row index or the column index as key.
5. In a Sudoku, you can combine the row index and the column index to identify which block this element belongs to.\
   e.g., create a list contains 9 dictionaries, [36M.Valid Sudoku (Python)](https://github.com/yshiyi/LeetCode/blob/main/Array/36M.%20Valid%20Sudoku.py), [36M.Valid Sudoku (C++)](https://github.com/yshiyi/LeetCode/blob/main/Array/36M.%20Valid%20Sudoku.cpp)
   ```
   Python
   rows = [{} for i in range(9)]
   columns = [{} for i in range(9)]
   boxes = [{} for i in range(9)]
   ```
   ```
   C++
   vector<set<int>> v_row, v_col, v_box;
   v_row.resize(9);
   v_col.resize(9);
   v_box.resize(9);
   ```
6. Sometimes, in a matrix, you might want to aggregate the values in the same diagonal line.


## 5. Sliding Window
### 219. Contains Duplicate II
Array, Hash Table, Sliding Window\
**Description:**\
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums\[i\] = nums\[j\] and the absolute difference between i and j is at most k.\
**Method:**
1. Using hash table
   The key is the element in nums, and the value is the index of the element in nums. We find out the minimum distance between two duplicate elements. In the end, we check if the minimum distance is less than k.
2. Sliding Window

[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/219.%20Contains%20Duplicate%20II.cpp)
```
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> m;
        int right = 0, left = 0;
        while(right < nums.size()){
            int val = nums[right];
            if(m.find(val)==m.end()){
                m[val] = right;
            }else if(right - m[val] <= k){
                return true;
            }
            right++;
            
            if(right - left > k){
                m.erase(nums[left]);
                left++;
            }
        }
        return false;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/219.%20Contains%20Duplicate%20II.py)
```
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        Set = set()  # Create a sliding window
        
        for i,num in enumerate(nums):
            if num in Set: # if already seen in last k items, then return True
                return True
            else: # otherwise, add that num to the set
                Set.add(num)
            
            if len(Set) > k: # there should be AT MOST k items in this set
                Set.remove(nums[i-k]) # if more than k items, remove the last-added item
                
        return False
```

### 3M. Longest Substring Without Repeating Characters
Hash Table, Two Pointers, String, Sliding Window\
**Description:**\
Given a string s, find the length of the longest substring without repeating characters.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/3M.%20Longest%20Substring%20Without%20Repeating%20Characters.cpp)
```
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size()==0){return 0;}
        if (s.size()==1){return 1;}
        int res = 0;
        int right = 0, left = 0, match = 0;
        unordered_map<char, int> window;
        while (right < s.size()){
            char c = s[right];
            window[c]++;
            
            while(window[c] > 1) {
                char d = s[left];
                window[d]--;
                left++;
            }
            
            right++;
            res = max(right-left, res);
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/3M.%20Longest%20Substring%20Without%20Repeating%20Characters.py)
```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p1 = 0
        max_len = 0
        Dic = {}
        
        for p2 in range(len(s)):
            if s[p2] in Dic:
                p1  = max(Dic[s[p2]], p1)
            Dic[s[p2]] = p2 + 1
            max_len = max(max_len, p2 - p1 + 1)
        
        return max_len

        # Another way using sliding window
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        window = {}
        right, left = 0, 0
        res = 0
        while (right < len(s)):
            c = s[right]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            right += 1
            while (window[c]>1):
                d = s[left]
                window[d] -= 1
                left += 1
            res = max(res, right-left)
        return res
```

### 438M. Find All Anagrams in a String
Hash Table, Sliding Window\






















