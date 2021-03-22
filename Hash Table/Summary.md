# Hash Table
<!-- GFM-TOC -->
* [Leetcode Hash Table](#Hash-Table)
   * [1. The Principle of Builtin Hash Table](#1-The-Principle-of-Builtin-Hash-Table)   
   * [2. Hash Set](#2-Hash-Set)
   * [3. Hash Map](#3-Hash-Map)
   * [4. Design the key](#4-Design-the-key)
   * [5. Sliding Window](#5-Sliding-Window)
       * [219. Contains Duplicate II](#219-Contains-Duplicate-II)
       * [3M. Longest Substring Without Repeating Characters](#3M-Longest-Substring-Without-Repeating-Characters)
       * [438M. Find All Anagrams in a String](#438M-Find-All-Anagrams-in-a-String)
       * [567M. Permutation in String](#567M-Permutation-in-String)
       * [76H.Minimum Window Substring](#76H-Minimum-Window-Substring)
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
**Dscription:**\
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s. Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100. The order of output does not matter.
**Method:**\
Similar to [567M. Permutation in String](#567M-Permutation-in-String)\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/438M.%20Find%20All%20Anagrams%20in%20a%20String.cpp)
```
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> window, need;
        int left = 0, right = 0, match = 0;
        int target_len = p.size();
        vector<int> res;
        for (auto& c:p){
            need[c]++;
        }
        while (right < s.size()){
            char c = s[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                if(window[c]==need[c]){
                    match++;
                }
            }
            right++;
            while (match==need.size()){
                char d = s[left];
                if (need.find(d)!=need.end()){
                    if(window[d]==need[d]){
                        match--;
                    }
                    window[d]--;
                }
                if (right - left == target_len){
                    res.push_back(left);
                }
                left++;
            }
        }
        return res;
    }
};

```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/438M.%20Find%20All%20Anagrams%20in%20a%20String.py)
```
class Solution(object):
    def findAnagrams(self, s, p):
        window, need = {}, {}
        right, left, match = 0, 0, 0
        target_len = len(p)
        res = []
        for c in p:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        
        while (right < len(s)):
            c = s[right]
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                if window[c]==need[c]:
                    match += 1
            right += 1
            
            while (match == len(need)):
                d = s[left]
                if d in need:
                    if window[d]==need[d]:
                        match -= 1
                    window[d] -= 1
                if right - left == target_len:
                    res.append(left)
                left += 1
        
        return res
```

### 567M. Permutation in String
Two pointers, Sliding window\
**Description:**\
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.\
**Method:**\
Similar to [76H.Minimum Window Substring](#76H-Minimum-Window-Substring).\
Only differece is we need to check the length of the substring which contains the target characters. If the length is equal to that of the target string, then return true.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/567M.%20Permutation%20in%20String.cpp)
```
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> window, need;
        int left = 0, right = 0, match = 0;
        int len = s1.size(), window_size = 0;
        for (auto& c:s1) {
            need[c]++;
        }
        while (right < s2.size()){
            char c = s2[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                if (window[c]==need[c]){
                    match++;
                }
            }
            right++;
            
            while (match==need.size()){
                char d = s2[left];
                if(need.find(d)!=need.end()){
                    if(window[d]==need[d]) {
                        match--;
                    }
                    window[d]--;
                }
                window_size = right - left;
                if (window_size==len){
                    return true;
                }
                left++;
            }
        }
        return false;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/567M.%20Permutation%20in%20String.py)
```
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        window, need = {}, {}
        left, right, match = 0, 0, 0
        target_len = len(s1)
        window_size = 0
        for c in s1:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
                
        while (right < len(s2)):
            c = s2[right]
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                
                if window[c]==need[c]:
                    match += 1
            right += 1
            
            while (match==len(need)):
                d = s2[left]
                if d in need:
                    if window[d]==need[d]:
                        match -= 1
                    window[d] -= 1
                if right - left == target_len:
                    return True
                left += 1
        return False
```

### 76H. Minimum Window Substring
Hash Table, Two Pointers, String, Sliding Window\
**Description:**\
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "". Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.\
**Method:**
1. Create two unordered_map: need and window. 
   need contains the target string and the number of each characters.
   window contains the target characters and the corresponding number of appearances in the window.
   Note: use \[key\]++. In doing so, the map automatically assigns 0 to key, if key doesn't exist.
2. Define some necessary variables
   two pointers: left and right
   number of matching characters: match
   starting position of the shortest substring: start
   length of the shortest substring: len
3. Move the pointer right first until the window contains all the target characters
   Check if char c is in need, if so, window\[c\]++.
   When the number of c in window is equal to that in need, we increase match by 1.
4. When match == need.size(), i.e., current window contains all target characters.
   We start to move the point left
   If char d is in need and if window\[d\]==need\[d\], then reduce match by 1.
   Otherwise, just reduce window\[d\] by 1;
5. Finally, check the value of len.
   If it doesn't change, it means there is no such short string and return "".
   Otherwise, return s.substr(start, len+1).
   Note: the length of the shorstest substring is len+1. 
         Because the pointer right points to the position of the last character.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/76H.%20Minimum%20Window%20Substring.cpp)
```
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> window, need;
        for (auto& c:t) {
            need[c]++;
        }

        int left = 0, right = 0, match = 0;
        int start = 0, len = INT_MAX;
        while(right < s.size()) {
            char c = s[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                // if (window[c]==1){ This doesn't work, if there are duplicate char in target string.
                if (window[c]==need[c]){
                    match++;
                }
            }
            while (match == need.size()) {
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                char d = s[left];
                if (need.find(d)!=need.end()){
                    if (window[d]==need[d]){
                        match--;
                    }
                    window[d]--;
                }                
                left++;
            }
            right++;
        }
        
        if (len!=INT_MAX){
            string res = s.substr(start, len+1);
            return res;
        }else{
            return "";
        }
        
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/76H.%20Minimum%20Window%20Substring.py)
```
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window = {}
        need = {}
        left, right, match = 0, 0, 0
        start, min_len = 0, float('Inf')
        for i in range(len(t)):
            if t[i] not in need:
                need[t[i]] = 1
            else:
                need[t[i]] += 1
                
        while right < len(s):
            if s[right] in need:
                if s[right] not in window:
                    window[s[right]] = 1
                else:
                    window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    match += 1
            while match == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                if s[left] in need:
                    if window[s[left]]==need[s[left]]:
                        match -= 1
                    window[s[left]] -= 1
                left += 1
            right += 1
            
        if min_len != float('Inf'):
            return s[start:start+min_len+1]
        else:
            return ""
```










