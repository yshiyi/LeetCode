# Hash Table
<!-- GFM-TOC -->
* [Leetcode Hash Table](#Hash-Table)
   * [1. The Principle of Building Hash Table](#1-The-Principle-of-Building-Hash-Table)   
   * [2. Design the key](#4-Design-the-key)
   * [3. Hash Set](#2-Hash-Set)
       * [170. Two Sum III](#170-Two-Sum-III)
       * [202. Happy Number](#202-Happy-Number)
       * [349. Intersection of Two Arrays](#349-Intersection-of-Two-Arrays)
   * [4. Hash Map](#3-Hash-Map)
       * [205. Isomorphic Strings](#205-Isomorphic-Strings)
       * [249M. Group Shifted Strings](#249M-Group-Shifted-Strings)
       * [359. Logger Rate Limiter](#359-Logger-Rate-Limiter)
       * [387. First Unique Character in a String](#387-First-Unique-Character-in-a-String)
       * [454M. 4Sum II](#454-4Sum-II)
       * [599. Minimum Index Sum of Two Lists](#599-Minimum-Index-Sum-of-Two-Lists)
   * [5. Hash Map with Array](#5-Hash-Map-with-Array)
       * [347M. Top K Frequent Elements](#347M-Top-K-Frequent-Elements)
       * [380M. Insert Delete GetRandom O(1)](#380M-Insert-Delete-GetRandom)
   * [6. Sliding Window](#5-Sliding-Window)
       * [219. Contains Duplicate II](#219-Contains-Duplicate-II)
       * [3M. Longest Substring Without Repeating Characters](#3M-Longest-Substring-Without-Repeating-Characters)
       * [438M. Find All Anagrams in a String](#438M-Find-All-Anagrams-in-a-String)
       * [567M. Permutation in String](#567M-Permutation-in-String)
       * [76H. Minimum Window Substring](#76H-Minimum-Window-Substring)
   * [7. Python with Collections](#7-Python-with-Collections)
       * [a. Dictionary with list](#a-Dictionary-with-list)
           * [288M. Unique Word Abbreviation](#288M-Unique-Word-Abbreviation)
           * [49M. Group Anagrams](#49M-Group-Anagrams)
       * [b. Dictionary with int](#b-Dictionary-with-int)
           * [454M. 4Sum II](#454-4Sum-II)
       * [c. Counter](#c-Counter)
           * [347M. Top K Frequent Elements](#347M-Top-K-Frequent-Elements)
           * [387. First Unique Character in a String](#387-First-Unique-Character-in-a-String)
           * [771. Jewels and Stones](#771-Jewels-and-Stones)
<!-- GFM-TOC -->

## 1. The Principle of Building Hash Table
The typical design of built-in hash table is:
  1. The key value can be any hashable type. And a value which belongs to a hashable type will have a hashcode. 
     This code will be used in the mapping function to get the bucket index.
  2. Each bucket contains an array to store all the values in the same bucket initially.
  3. If there are too many values in the same bucket, these values will be maintained in a height-balanced binary 
     search tree instead.

The average time complexity of both insertion and search is still O(1). And the time complexity in the worst case is O(logN) 
for both insertion and search by using height-balanced BST. It is a trade-off between insertion and search.

## 2. Design the key
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


## 3. Hash Set
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
### 170. Two Sum III
Data structure design, Hash Table\
**Description:**\
Design and implement a TwoSum class. It should support the following operations: add and find.\
add - Add the number to an internal data structure.\
find - Find if there exists any pair of numbers which sum is equal to the value.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/170.%20Two%20Sum%20III%20%E2%80%94%20Data%20structure%20design.cpp)
```
class TwoSum {
private:
    set<int> s1, s2;
public:
    void add(int val) {
        s1.insert(val);
    }
    bool find(int val) {
        for (set<int>::iterator it=s1.begin(); it!=s1.end(); ++it) {
            int remain = val - *it;
            if (s2.find(remain) != s2.end()) {
                return true;
            }else {
                s2.insert(remain);
            }
        }
        return false;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/170.%20Two%20Sum%20III%20%E2%80%94%20Data%20structure%20design.py)
```
class TwoSum(object):
    def __init__(self):
        self.Set = set()

    def add(self, num):
        self.Set.add(num)

    def find(self, num):
        self.Set2 = set()
        for n in self.Set:
            if num - n not in self.Set2:
                self.Set2.add(n)
            else:
                return True
        return False
```


### 202. Happy Number
Hash Table, Math\
**Description:**\
Write an algorithm to determine if a number n is "happy". A happy number is a number defined by the following process:  Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers. Return True if n is a happy number, and False if not.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/202.%20Happy%20Number.cpp)
```
class Solution {
public:
    bool isHappy(int n) {
        set<int> s;
        while (true) {
            n = squaredSum(n);
            if (n == 1) {
                return true;
            }
            if (s.find(n) != s.end()) {
                return false;
            }else {
                s.insert(n);
            }
        }  
    }
    int squaredSum(int n) {
        string str = to_string(n);
        int sum = 0, mod;
        for (int i=0; i< str.size(); i++) {
            mod = n % 10;
            sum += pow(mod, 2);
            n = n / 10;  // n is defined as int, it will be automatically rounded down.
        }
        return sum;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/202.%20Happy%20Number.py)
```
class Solution(object):
    def isHappy(self, n):
        '''
        Method: Create a set to hold the numbers have seen.
                Firstly, calculate the sum of the square of each digits of number n.
                Then check if this number is contained in the set seen.
                If so, it will be an infinit loop and return false.
                Otherwise, add this number to seen and go on.
        '''
        seen = set()
        while True:
            n = self.squareSum(n)
            if n not in seen:
                seen.add(n)
            else:
                return False
            if n == 1:
                return True
        
    def squareSum(self, n):
        result = 0
        for x in str(n):
            result += int(x) ** 2
        return result
```


### 349. Intersection of Two Arrays
Hash Table, Two Pointers, Binary Search, Sort\
**Description:**\
Given two arrays, write a function to compute their intersection.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/349.%20Intersection%20of%20Two%20Arrays.cpp)
```
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        
        /* Method 1: Using set_intersection. It returns a pointer which points to the end of intersection.
                     Note: Initialize v with size of min(nums1.size(), nums2.size()).
                           Resize v by using v.resize(it - v.begin()).
        */
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        vector<int> v, res;
        v.resize(min(nums1.size(), nums2.size()));
        vector<int>::iterator it = set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), v.begin());
        v.resize(it-v.begin());
        
        set<int> s;
        for(auto& val:v){
            s.insert(val);
        }
        for(auto& val:s){
            res.push_back(val);
        }
        return res;
        
        
        /* Method 2: Using hashset.
                     Save all elements from nums1 to a set.
                     Then sweep nums2. If the element is in the set, then save it to res.
                     Note: We also need to remove the non-unqiue elements from set to prevent the duplication.
        */
        set<int> s;
        vector<int> res;
        for(auto& val:nums1){
            s.insert(val);
        }
        for(auto& val:nums2){
            if(s.find(val)!=s.end()){
                res.push_back(val);
                s.erase(val);
            }
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/349.%20Intersection%20of%20Two%20Arrays.py)
```
class Solution(object):
    def intersection(self, nums1, nums2):
        '''
        Method 1: Convert nums1 to set to remove duplicates.
                  Check each element in nums1
        '''
        Nums1 = set(nums1)
        result = []
        # for x in Nums1:
        #     if x in nums2:
        #         result.append(x)
        # return result
        return [x for x in Nums1 if x in Nums2]
    
        '''
        Method 2: Convert both nums1 and nums2 to set.
                  Use set(A).intersection(B) to obtain the intersection
        '''
        Nums1 = set(nums1)
        Nums2 = set(nums2)
        return list(set(Nums1).intersection(Nums2))
        return list(Nums1 & Nums2)
```



## 4. Hash Map
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
### 205. Isomorphic Strings
Hash Table\
**Description:**\
Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t. All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/205.%20Isomorphic%20Strings.cpp)
```
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int sl = s.size(), tl = t.size();
        if (sl != tl) {return false;}
        map<char, int> ms, mt;
        map<char, int>::iterator its, itt;
        for (int i=0; i<sl; i++) {
            its = ms.find(s[i]);
            itt = mt.find(t[i]);
            if (its!=ms.end() && itt!=mt.end()) {
                if ((its)->second == (itt)->second) {
                    continue;
                }else {
                    return false;
                }
            }else if (its==ms.end() && itt==mt.end()) {
                ms.insert(make_pair(s[i], i));
                mt.insert(make_pair(t[i], i));
            }else {
                return false;
            }
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/205.%20Isomorphic%20Strings.py)
```
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        '''
        Method : The goal is to check the pattern of two strings.
                 Use zip() to pair two strings together.
                 Firstly, we check if the character has been seen before. If so, save it to a dictionary.
                 Secondly, if the character has been seen before in both strings, we check the previous position.
                 If it appears at the same position, we continue the loop. Otherwise, we return false.
                 If there are other scenarios, we return false.
        '''
        Dic1 = {}
        Dic2 = {}
        index = 0
        for cha1, cha2 in zip(s, t):
            if cha1 not in Dic1 and cha2 not in Dic2:
                Dic1[cha1] = index
                Dic2[cha2] = index
            elif cha1 in Dic1 and cha2 in Dic2:
                if Dic1[cha1] == Dic2[cha2]:
                    continue
                else:
                    return False
            else:
                return False
            index += 1
        return True
```


### 249M. Group Shifted Strings
Hash Table\
**Description:**\
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz" or "adg -> beh -> cfi ..." Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.\
[C++]()
```
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> m;
        for (auto str:strings) {
            m[convertString(str)].push_back(str);
        }
        unordered_map<string, vector<string>>::iterator it=m.begin();
        while (it!=m.end()) {
            cout << (*it).first << endl;
            res.push_back(it->second);
            it++;
        }
        return res;
    }

    string convertString(string str) {
        string res;
        int num1;
        int num0 = (int)str[0] - 97;
        for (int i=0; i<str.size(); ++i) {
            num1 = (int)str[i] - 97 - num0;
            if (num1 < 0) {
                num1 += 26;
            }
            res.insert(i, to_string(num1));
        }
      
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/249M.%20Group%20Shifted%20Strings.py)
```
class Solution(object):
    def groupStrings(self, strs):
        # Use function ord() to convert alphabet to integer. ord('a') -> 97, chr(97) -> 'a'
        # We use ord('a') - 97 to convert 'a' to 0.
        # Note that 'abc' -> 0,1,2, 'bcd' -> 1,2,3 and 'xyz' -> 23,24,25. If we subtract the first number from the list,
        #   we can get  'abc' -> 0,1,2, 'bcd' -> 0,1,2 and 'xyz' -> 0,1,2
        # Notice that the successive letter of 'z' is 'a'. 'az' -> 0,25 and 'ba' -> 1,0.
        #   If we subtract 1 from 1,0, we get 0, -1. In this case, we can take the modulus of 26.
        #   0 % 26 = 0, -1 % 26 = 25.

        # The basic idea to convert the string to a list of integers.
        # Check if the sequence of the integers has been seen. If not, create a new key. If so, save it to existing key.

        result = {}
        for word in strs:
            word_converted = self.convertWord(word)
            # print(word_converted)
            if word_converted not in result:
                result[word_converted] = [word]
            else:
                result[word_converted] = result[word_converted] + [word]
        return result.values()

    def convertWord(self, word):
        L_word = []
        for char in word:
            L_word.append(ord(char))
        L_word = [(num - L_word[0]) % 26 for num in L_word]
        L_str = ''
        for num in L_word:
            L_str += str(num)
        return L_str
```


### 359. Logger Rate Limiter
Hash Table\
**Description:**\
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds. Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false. It is possible that several messages arrive roughly at the same time.\
**Method:**\
Create a dictionary to hold the message and its time stamp. If the message has never been seen before or it doesn't show up in the last 10 steps, return true. Otherwise, return false.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/359.%20Logger%20Rate%20Limiter.cpp)
```
class Solution{
public:
    bool shouldPrintMessage(string& message, int timestamp){
        if(myMap_.find(message)==myMap_.end() || timestamp - myMap_[message] >= 10){
            myMap_[message] = timestamp;
            return true;
        }else{
            return false;
        }
    }
    map<string, int> myMap_;
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/359.%20Logger%20Rate%20Limiter.py)
```
class Solution(object):
    def shouldPrintMessage(self, message, timestamp):
        logger = {}
        if message not in logger or timestamp - logger[message] >= 10:
            logger[message] = timestamp
            return True
        else:
            return False
```

### 387. First Unique Character in a String
Hash Table, String\
**Description:**\
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/387.%20First%20Unique%20Character%20in%20a%20String.cpp)
```
class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> m;
        for(auto& c:s){
            m[c]++;
        }
        for(int i=0; i<s.size(); ++i){
            if(m[s[i]]==1){
                return i;
            }
        }
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/387.%20First%20Unique%20Character%20in%20a%20String.py)
```
class Solution(object):
    def firstUniqChar(self, s):
        """
        Method: build hash map : character and how often it appears
        """
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
```

### 454M. 4Sum II
Hash Table, Binary Search\
**Description:**\
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A\[i\] + B\[j\] + C\[k\] + D\[l\] is zero.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/454M.%204Sum%20II.cpp)
```
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        map<int, int> m;
        int res = 0;
        for(auto& val1:A){
            for(auto& val2:B){
                m[val1+val2]++;
            }
        }
        
        for(auto& val3:C){
            for(auto& val4:D){
                int sum = val3 + val4;
                if(m.find(-sum)!=m.end()){
                    res += m[-sum];
                }
            }
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/454M.%204Sum%20II.py)
```
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        Method 1: Create a dictionary to store the combinations of A and B.
                  The key the possible summation and the value is the number of appearances.
                  Use dic.get(value, 0). Note, 0 is optional and is the return value when the specific key does not exist.
        """
        n = len(A)
        ans = 0
        Dic_AB = {}
        for i in range(n):
            for j in range(n):
                num = A[i] + B[j]
                Dic_AB[num] = Dic_AB.get(num, 0) + 1
        for k in range(n):
            for l in range(n):
                num2 = C[k] + D[l]
                if -num2 in Dic_AB:
                    ans += Dic_AB[-num2]
        
        return ans

        """
        Method 2: Similar idea to method 1.
                  Use collections.defaultdict to initialize a dictionary.
                  Faster than method 1.
        """
        d1 = collections.defaultdict(int)
        for i in A:
            for j in B:
                d1[i+j]+=1
        count = 0
        for i in C:
            for j in D:
                count+=d1[-(i+j)] 
        return count
```

### 599. Minimum Index Sum of Two Lists
Hash Table\
**Description:**\
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings. You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/599.%20Minimum%20Index%20Sum%20of%20Two%20Lists.cpp)
```
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        map<string, int> m;
        for(int i=0; i<list1.size(); ++i){
            m[list1[i]] = i;
        }
        int sum_min = INT_MAX;
        vector<string> res;
        for(int j=0; j<list2.size(); ++j){
            if(m.find(list2[j])!=m.end()){
                int sum = j + m[list2[j]];
                if(sum < sum_min){
                    sum_min = sum;
                    res.clear();
                    res.push_back(list2[j]);
                }else if(sum==sum_min){
                    res.push_back(list2[j]);
                }
            }
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/599.%20Minimum%20Index%20Sum%20of%20Two%20Lists.py)
```
class Solution(object):
    def findRestaurant(self, list1, list2):
        '''
        Method : At first, convert both lists to dictionary by using dict(zip(list, len(list)))
                 Loop through all the words in list1. 
                 If the word is also in list2, we then check if the summation of two values is less than min.
                 If so, we reset the result and save the word to result.
                 If the sum is equal to the min, we append the result.
        '''
        Dic1 = dict(zip(list1, range(len(list1))))
        Dic2 = dict(zip(list2, range(len(list2))))
        result = []
        index_ms = len(list1) + len(list2)
        for rest in Dic1:
            if rest in Dic2:
                if Dic1[rest] + Dic2[rest] < index_ms:
                    index_ms = Dic1[rest] + Dic2[rest]
                    result = []
                    result = [rest]
                elif Dic1[rest] + Dic2[rest] == index_ms:
                    result.append(rest)
        return result
```



## 5. Hash Map with Array
### 380M. Insert Delete GetRandom
Array, Hash Table, Design\
**Description:**\
Implement the RandomizedSet class:
1. bool insert(int val) Inserts an item. Returns true if the item was not present, false otherwise.
2. bool remove(int val) Removes an item. Returns true if the item was present, false otherwise.
3. int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
   Each element must have the same probability of being returned.
4. Follow up: Could you implement the functions of the class with each function works in average O(1) time?

**Method:**\
To insert or remove a value, we need to use hash table which takes O(1) operation time.\
To randomly select a value, we need to use array which takes O(1) operation time. Hash table doesn't support such function.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/380M.%20Insert%20Delete%20GetRandom%20O(1).cpp)
```
class RandomizedSet {
public:
    map<int, int> m;
    vector<int> vec;
    
    RandomizedSet() {
    }
    bool insert(int val) {
        if(m.find(val)==m.end()){
            int n = m.size();
            m[val] = n;
            vec.push_back(val);
            return true;
        }else{
            return false;
        }
    }
    
    bool remove(int val) {
        if(m.find(val)!=m.end()){
            int v = vec[m.size()-1];
            int v_index = m[v];
            if(v!=val){
                swap(vec[m.size()-1], vec[m[val]]);
                m[v] = m[val];
            }
            vec.pop_back();
            m.erase(val);
            return true;
        }else{
            return false;
        }
    }
    
    int getRandom() {
        int n = m.size();
        int r = rand() % n;
        return vec[r];
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/380M.%20Insert%20Delete%20GetRandom%20O(1).py)
```
from random import choice
class RandomizedSet:
    def __init__(self):
        self.nums = [] # Space O(N)
        self.hashTable = {} # Space O(N)
    def insert(self, val): # Time O(1)
        if not val in self.hashTable:
            self.nums.append(val)
            self.hashTable[val] = len(self.nums) - 1
            return True
        else:
            return False
    def remove(self, val): # Time O(1)
        if not val in self.hashTable:
            return False
        else:
            lastNum = self.nums[-1]
            valIndex = self.hashTable[val]
            if lastNum != val:
                #Swap
                self.nums[-1], self.nums[valIndex] = self.nums[valIndex], self.nums[-1]
                self.hashTable[lastNum] = valIndex
            # It means that always delete val at the last of nums list
            self.nums.pop(-1)
            del self.hashTable[val]
            return True

    def getRandom(self):
        return choice(self.nums) # Time O(1)
```
        

## 6. Sliding Window
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

## 7. Python with Collections
### a. Dictionary with list
#### 288M. Unique Word Abbreviation
Hash Table, Design\
**Description:**\
An abbreviation of a word follows the form \<first letter\>\<number of characters\>\<last letter\>.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/288M.%20Unique%20Word%20Abbreviation.cpp)
```
class ValidWordAbbre {
public:
    ValidWordAbbre(vector<string>& words) {
        for (int i=0; i<words.size(); ++i) {
            string abbre = convertToAbbre(words[i]);
            if (m.find(abbre) == m.end()) {
                m.insert(make_pair(abbre, 1));
            }else {
                m[abbre]++;
            }
        }
    }

    bool isUnique(string& word) {
        string abbre = convertToAbbre(word);
        if (m[abbre] == 1) {
            return true;
        }else {
            return false;
        }
    }

    string convertToAbbre(string& word) {
        if(word.size()<3){
            return word;
        }
        string res;
        int l = word.size();
        res = word[0] + to_string(l-2) + word[l-1];
        return res;
    }

private:
    unordered_map<string, int> m;
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/288M.%20Unique%20Word%20Abbreviation.py)
```
class ValidWordAbbr:
    def __init__(self, _dictionary):
        self.dic = collections.defaultdict(list)  #  collections.defaultdict(set)
        for word in _dictionary:
            self.dic[self.abbrev(word)].append(word)

    def isUnique(self, word):
        if self.abbrev(word) not in self.dic:
            return True
        elif word == self.dic[self.abbrev(word)]:
            return True
        else:
            return False

    def abbrev(self, word):
        if len(word) < 3:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
```

#### 49M. Group Anagrams
Hash Table, String\
**Description:**\
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/49M.%20Group%20Anagrams.cpp)
```
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> m;
        for(auto& str:strs){
            string sorted_str = str;
            sort(sorted_str.begin(), sorted_str.end());
            m[sorted_str].push_back(str);
        }
        vector<vector<string>> res;
        for(auto& key:m){
            res.push_back(key.second);
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/49M.%20Group%20Anagrams.py)
```
class Solution(object):
    def groupAnagrams(self, strs):
        '''
        Method 1: Use collections to make a dictionary with list
                  >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
                  >>> d = collections.defaultdict(list)
                  >>> for k, v in s:
                  ...     d[k].append(v)
                  ...
                  >>> d.items()
                  [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
        '''
        ans = collections.defaultdict(list)
        for s in strs:
            ans[str(sorted(s))].append(s)
        return ans.values()
        
        '''
        Method 2: For each sorted string, we check if it is contained in result.
                  If not, create a new key. If so, add this word to the existing value.
        '''
        result = {}
        if len(strs) < 1:
            return [['']]
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in result:
                result[sorted_word] = [word]
            else:
                result[sorted_word] = result[sorted_word] + [word]
        return result.values()
```

### b. Dictionary with int

### c. Counter
#### 347M. Top K Frequent Elements
Hash Table, Heap\
**Description:**\
Given a non-empty array of integers, return the k most frequent elements.\
**Method:**\
1. Use QuickSelect.
2. Use dictionary (Python). use Dic.key()\[Dic.values().index(val)\] to retrieve the key from value
3. Use collection.Counter() (Python)]

[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/347M.%20Top%20K%20Frequent%20Elements.cpp)
```
class Solution {
public:
    
    /* myCompare is declared as a member function of class Solution, 
       and hence requires this pointer for calling it. 
       The complete tag for functions like bool cmp is:
       bool myCompare(Solution* this, pair<int, int>& p1, pair<int, int>& p2)
       We can declare it as a static funtion, since static functions do not require this pointer for calling.
    */
    static bool myCompare(pair<int, int>& p1, pair<int, int>& p2) {
        return p1.second > p2.second;
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /* Method 1: First, use a map to count the appearances of each unique element,
                     Then, use a multimap to flip the key and value in map.
                     Finally, save the last k elements to a vector.
        */
        map<int, int> m;
        for (auto& val:nums) {
            if (m.find(val) != m.end()) {
                m[val]++;
            }else {
                m.insert(make_pair(val, 1));
            }
        }
        
        multimap<int, int> mm;
        for (auto& key:m) {
            mm.insert(make_pair(key.second, key.first));
        }
        
        vector<int> res;
        multimap<int, int>::reverse_iterator it = mm.rbegin();
        for (int i=0; i<k; ++i) {
            res.push_back(it->second);
            it++;
        }
        
        return res;
        
        
        /* Method 2: First, create a map. 
                     The key is the unique elements, the value is the currect size of vecValues.
                     In other words, the value in the map indicates the index of the key in vecValues.
                     Create a vector of pairs of integers. The index of the vector is the value of the map.
                     The first value of the pair is the unique element, 
                     and the second value of the pair is the number of appearances.
                     Then sort this vector using self-defined functional object (it must be static).
                     Finally, save the first k elements to vecAnswer.
        */
        unordered_map<int, int> mapValues;
        vector<pair<int, int>> vecValues;
        vector<int> vecAnswer;
        
        for(auto& val:nums)
        {
            if(mapValues.find(val) != mapValues.end())
            {
                vecValues[mapValues[val]].second++;
            }
            else
            {
                mapValues[val] = vecValues.size();
                vecValues.emplace_back(pair<int,int>{val, 1});
            }
        }
        
        sort(vecValues.begin(), vecValues.end(), myCompare);
        for(int nIndex = 0; nIndex < k; nIndex++)
        {
            vecAnswer.push_back(vecValues[nIndex].first);
        }
        return vecAnswer;
        
        
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/347M.%20Top%20K%20Frequent%20Elements.py)
```
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Method 1: Create a dictionary to the hold the distinct element and its frequency, i.e., element: frequency.
                  Sort the dictionary.values(), and add the first k keys to the answer.
                  Remember to remove the key from the dictionary after the insertion.
        """
        Dic = {}
        ans = []
        for n in nums:
            Dic[n] = Dic.get(n, 0) + 1
        lst = Dic.values()
        lst.sort(reverse=True)
        for i in range(k):
            ans.append(Dic.keys()[Dic.values().index(lst[i])])
            del Dic[ans[i]]
        return ans
        
        
        """
        Method 2: Similar to Method 1.
                  Use collections.Counter to convert a list to a counter. 
                  A counter is a kind of dictionary in which the keys are the distinct elements and values are their frequencies.
                  Then use heapq.nlargest(n, iterable, key) to extract the n elements with most frequency.
                  heapq.nlargest(n, iterable, key) return a list with the n largest elements from the dataset defined by iterable. 
                  key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in iterable.
                  In this case, key=count.get obtains the value of each element in count.keys() and find the largest n values.
                  
                  The property of this heap structure in Python is that each time the smallest of heap element is popped(min heap). 
                  Whenever elements are pushed or popped, heap structure in maintained. 
                  l = [5, 7, 9, 4, 3] 
                  # using heapify() to convert list into heap 
                  heapq.heapify(l)  # print(list(l)) -> [3, 4, 9, 5, 7]
                  # insert a value to heap
                  heapq.heappush(l, 10) # print(list(l)) -> [3, 4, 9, 5, 7, 10]
                  # pop the min value (which is 3) from heap
                  heapq.heappop(l)  # print(list(l)) -> [4, 5, 9, 10, 7]
                  # pop and return the smallest item from the heap, and also push the new item.
                  heapq.heapreplace(l, 2)  # print(list(l)) -> [2, 5, 9, 10, 7]
                  
        """
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
        
        
        
        """
        Method 3: Use quickselect, a.k.a. Hoare's selection algorithm.
                  Quickseelct is a textbook algorithm typicaly used to solve the problems "find kth something": 
                  kth smallest, kth largest, kth most frequent, kth less frequent, etc.
                  It has O(N) average time complexity, and its worst case time complexity is O(N^2).
                  Randomly select an element, and move less frequent elements to the left and others to the right.
        """
        # Count the frequency of each distinct element in nums
        count = Counter(nums)
        # Save the distinct elements in a list
        dis_nums = list(count.keys())
```


#### 771. Jewels and Stones
Hash Table\
**Description:**\
You're given strings J representing the types of stones that are jewels, and S representing the stones you have. Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels. The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/771.%20Jewels%20and%20Stones.cpp)
```
class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int res = 0;
        for(auto& c:stones){
            if(jewels.find(c)!=-1){
                res++;
            }
        }
        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Hash%20Table/771.%20Jewels%20and%20Stones.py)
```
class Solution(object):
    def numJewelsInStones(self, J, S):
        '''
        Method 1: Check each stone, if it is a jewel.
        '''
        num = 0
        for s in S:
            if s in J:
                num += 1
        return num
        
        '''
        Method 2: Using collections.Counter()
        '''
        stones_dic = Counter(stones);
        res = 0
        for key, val in stones_dic.items():
            if key in jewels:
                res += val
        return res
```



