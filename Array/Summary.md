# Array
<!-- GFM-TOC -->
* [Leetcode Array](#Array)
    * [1. Introduction to Array](#1-Introduction-to-Array)
    * [2. Search for a particular number or check duplicates](#2-Search-for-particular-number-or-check-duplicates)
       * [1. Two Sum](#1-Two-Sum)
       * [1346. Check If N and Its Double Exist](#1346-Check-If-N-and-Its-Double-Exist)
       * [136. Single Number](#136-Single-Number)
       * [217. Contains Duplicate](#217-Contains-Duplicate)
       * [414. Third Maximum Number](#414-Third-Maximum-Number)
       * [448. Find All Numbers Disappeared in an Array](#448-Find-All-Numbers-Disappeared-in-an-Array)
    * [3. Remove or remove elements within array](#3-Remove-or-remove-elements-within-array)
       * [1089. Duplicate zeros](#1089-Duplicate-zeros)
       * [26. Remove Duplicates from Sorted Array](#26-Remove-Duplicates-from-Sorted-Array)
       * [27. Remove Element](#27-Remove-Element)
       * [283. Move Zeroes](#283-Move-Zeroes)
    * [4. Two pointers](#4-Two-pointers)
       * [1299. Replace Elements with Greatest Element on Right Side](#1299-Replace-Elements-with-Greatest-Element-on-Right-Side)
       * [15M. 3Sum](#15M-3Sum)
       * [167. Two Sum II - Input array is sorted](#167-Two-Sum-II-Input-array-is-sorted)
       * [344. Reverse String](#344-Reverse-String)
       * [88. Merge Sorted Array](#88-Merge-Sorted-Array)
       * [905. Sort Array By Parity](#905-Sort-Array-By-Parity)
       * [209M. Minimum Size Subarray Sum](#209M-Minimum-Size-Subarray-Sum)
    * [5. Peak and valley](#5-Peak-and-valley)
       * [122. Best time to Buy and Sell Stock II](#122-Best-time-to-Buy-and-Sell-Stock-II)
       * [941. Valid Mountain Array](#941-Valid-Mountain-Array)
    * [6. Use some particular functions](#6-Use-some-particular-functions)
       * [1051. Height checker](#1051-Height-checker)
       * [1295. Find Numbers with Even Number of Digits](#1295-Find-Numbers-with-Even-Number-of-Digits)
       * [189M. Rotate Array](#189M-Rotate-Array)
       * [350. Intersection of Two Arrays II](#350-Intersection-of-Two-Arrays-II)
       * [36M. Valid Sudoku](#36M-Valid-Sudoku)
       * [485. Max Consecutive Ones](#485-Max-Consecutive-Ones)
       * [48M. Rotate Image](#48M-Rotate-Image)
       * [66. Plus One](#66-Plus-One)
       * [724. Find Pivot Index](#724-Find-Pivot-Index)
       * [977. Squares of a Sorted Array](#977-Squares-of-a-Sorted-Array)
       * [84H. Largest Rectangle in Histogram](#84H-Largest-Rectangle-in-Histogram)
<!-- GFM-TOC -->

## 1. Introduction to Array
An array is a basic data structure to store a collection of elements sequentially. 
But elements can be accessed randomly since each element in the array can be identified by an array index.\
**Static Array**
```
// 1. Initialize
int a0[5];
int a1[5] = {1, 2, 3};  // other element will be set as the default value
// 2. Get Length
int size = sizeof(a1) / sizeof(*a1);
cout << "The size of a1 is: " << size << endl;
// 3. Access Element
cout << "The first element is: " << a1[0] << endl;
// 4. Iterate all Elements
cout << "[Version 1] The contents of a1 are:";
for (int i = 0; i < size; ++i) {
    cout << " " << a1[i];
}
cout << endl;
cout << "[Version 2] The contents of a1 are:";
for (int& item: a1) {
    cout << " " << item;
}
cout << endl;
// 5. Modify Element
a1[0] = 4;
// 6. Sort
sort(a1, a1 + size);
```
**Dynamic Array**
```
// 1. initialize
vector<int> v0;
vector<int> v1(5, 0);
// 2. make a copy
vector<int> v2(v1.begin(), v1.end());
vector<int> v3(v2);
// 2. cast an array to a vector
int a[5] = {0, 1, 2, 3, 4};
vector<int> v4(a, *(&a + 1));
// 3. get length
cout << "The size of v4 is: " << v4.size() << endl;
// 4. access element
cout << "The first element in v4 is: " << v4[0] << endl;
// 5. iterate the vector
cout << "[Version 1] The contents of v4 are:";
for (int i = 0; i < v4.size(); ++i) {
    cout << " " << v4[i];
}
cout << endl;
cout << "[Version 2] The contents of v4 are:";
for (int& item : v4) {
    cout << " " << item;
}
cout << endl;
cout << "[Version 3] The contents of v4 are:";
for (auto item = v4.begin(); item != v4.end(); ++item) {
    cout << " " << *item;
}
cout << endl;
// 6. modify element
v4[0] = 5;
// 7. sort
sort(v4.begin(), v4.end());
// 8. add new element at the end of the vector
v4.push_back(-1);
// 9. delete the last element
v4.pop_back();
```

## 2. Search for a particular number or check duplicates
* [1. Two Sum](#1-Two-Sum)
* [1346. Check If N and Its Double Exist](#1346-Check-If-N-and-Its-Double-Exist)
* [136. Single Number](#136-Single-Number)
* [217. Contains Duplicate](#217-Contains-Duplicate)
* [414. Third Maximum Number](#414-Third-Maximum-Number)
* [448. Find All Numbers Disappeared in an Array](#448-Find-All-Numbers-Disappeared-in-an-Array)

### 1. Two Sum 
**Description:**\
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
**Method:**\
Hash Table, Create a dictionary.\
|                                                                                                                                                                                                                  [.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/01.%20Two%20Sum.cpp)                                                                                                                                                                                                                 |                                                                                                                                      [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/01.%20Two%20Sum.py)                                                                                                                                     |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  <pre> vector<int> twoSum(vector<int>& nums, int target) { <br>   map<int, int> m;<br>   int l = nums.size();<br>   map<int, int>::iterator it;<br>   vector<int> result;<br>   for (int i=0; i<l; i++) {<br>       it = m.find(target - nums[i]);<br>       if(it==m.end()) {<br>           m.insert(make_pair(nums[i], i));<br>       }else {<br>           result.push_back(i);<br>           // result.push_back(m[target-nums[i]]);<br>           result.push_back((*it).second);<br>           break;<br>       }<br>   }<br>   return result;<br> }  </pre>|  <pre>def twoSum(self, nums, target):<br>       h = {}<br>       for i, num in enumerate(nums):<br>           \\ Method 1:<br>           n = target - num<br>           if n not in h:<br>               h[num] = i<br>           else:<br>               return [h[n], i]<br>            \\ Method 2:<br>           if n in nums:<br>               index = [i, nums.index(n)]<br>           break </pre> |

### 1346. Check If N and Its Double Exist
**Description:**\
Given an array arr of integers, check if there exists two integers N and M 
such that N is the double of M ( i.e. N = 2 * M).\
**Method:**\
For python, use "if ... in arr" to improve speed. For c++, beware of the conversion between int and double. In addition, we can also use count(v.begin(), v.end(), val).
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/1346.%20Check%20If%20N%20and%20Its%20Double%20Exist.cpp) | [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/1346.%20Check%20If%20N%20and%20Its%20Double%20Exist.py)|
|:-- |:-- |
|<pre> bool checkIfExist(vector<int>& arr) {<br>        // Method 1:<br>        bool result = false;<br>        set\<double\> s; <br>        for (int i=0; i<arr.size(); i++) {<br>            if (s.find((double)arr[i]/2) != s.end() \|\| s.find((double)arr[i]\*2) != s.end()) {<br>                return result = true;<br>            }else {<br>                s.insert((double)arr[i]);<br>            }<br>        }<br>        return result;<br>        // Method 2: using count(v.begin(), v.end(), value)<br>        for(auto i: arr){<br>            // just take care of exeptions and use count all over :)<br>            if (i == 0){<br>                if (count(arr.begin(), arr.end(), i) > 1) <br>                    return true;<br>                else<br>                    continue;<br>            }<br>            if (count(arr.begin(), arr.end(), i\*2))<br>                return true;<br>        }<br>        return false;<br>    }</pre>|<pre>def checkIfExist(self, arr):<br>        if arr is None or len(arr) <= 1: return False<br>        for i in range(len(arr)):<br>            if arr[i] != 0: # check if the current is not 0<br>                if arr[i]*2 in arr: <br>                    return True<br>                if arr[i]%2 == 0 and arr[i] / 2 in arr:<br>                    return True<br>            else: # if 0, we have to look for a zero at a different index<br>                if 0 in arr[:i] or 0 in arr[i+1:]: return True<br>        return False<br> </pre>|

### 136. Single Number 
**Description:**\
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?\
**Method:**\
Hash table, Bit manipulation\
For python, create a set to search for the duplicated element. For c++, use count() which is slow or use XOR (i.e., a^0=a; a^a=0).
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/136.%20Single%20Number.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/136.%20Single%20Number.py)|
|:-- |:-- |
|<pre>int singleNumber(vector<int>& nums) {<br>        /* Method 1: using count(v.begin(), v.end(), value)<br>                     This method takes about 952 ms.<br>        */<br>        int single_num;<br>        for (auto i:nums) {<br>            if (count(nums.begin(), nums.end(), i) == 1) {<br>                return single_num = i;<br>            }<br>        }<br>        return single_num;<br>        /* Method 2: using XOR<br>                     In c++, XOR is ^;<br>                     a ^ 0 = a; a ^ a = 0;<br>                     This method takes only 16 ms.<br>        */<br>        int result = 0;<br>        for (auto i:nums) {<br>            result = result ^ i;<br>        }<br>        return result;<br>    } </pre>|<pre>def singleNumber(self, nums):<br>        '''<br>        Method 1: create a set instead of a dictionary<br>        '''<br>        single = set()<br>        for i in range(len(nums)):<br>            if nums[i] not in single:<br>                single.add(nums[i])<br>            else:<br>                single.remove(nums[i])<br>        return list(single)[0]<br>        '''<br>        Method 2: Apply Math, 2 * (a+b+c) - (a+a+b+b+c) = c<br>                  Use set, note: the keys contained in a set are distinct.<br>        '''<br>        return 2 * sum(set(nums)) - sum(nums) </pre>|

### 217. Contains Duplicate
**Description:**\
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.\
**Method:**\
Array, Hash table\
a. Create a hash table (i.e., set). \
   Check if the element of nums is in the set.\
b. Convert array/vector to a set then compare the length. For python, use set(nums).
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/217.%20Contains%20Duplicate.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/217.%20Contains%20Duplicate.py)|
|:-- |:-- |
|<pre>bool containsDuplicate(vector<int>& nums) {<br>        // Method 1: Using a set and check if the element is in the set<br>        set\<int\> s;<br>        int l = nums.size();<br>        for (auto val:nums) {<br>            if (s.find(val) != s.end()) {<br>                return true;<br>            }else {<br>                s.insert(val);<br>            }<br>        }<br>        return false;<br>        // Method 2: using a set. Save all the elements form nums to s, and compare the size.<br>        for (auto val:nums) {<br>            s.insert(val);<br>        }<br>        return !(s.size()==l);<br>    } </pre>|<pre> def containsDuplicate(self, nums):<br>        '''<br>        Method 1: Create a hash table (i.e., set)<br>                  Check if the element of nums is in the set.<br>        '''<br>        dic = set()<br>        for i in range(len(nums)):<br>            if nums[i] not in dic:<br>                dis.add(nums[i])<br>            else:<br>                return true<br>        return false<br>        '''<br>        Method 2: Use set()!!!<br>                  Note the elements contained in a set are distinct!!<br>                  Compare len(set(nums)) and len(nums)<br>        '''<br>        return True if len(set(nums)) < len(nums) else False</pre>|

### 414. Third Maximum Number
**Description:**\
Given a non-empty array of integers, return the third maximum number in this array. 
If it does not exist, return the maximum number. 
The time complexity must be in O(n).\
**Method:**\
Array\
Use a counter to search for the third maximum number, if len(nums)>2. If there is no such number, return max(nums).\
[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/414.%20Third%20Maximum%20Number.cpp)
```
int thirdMax(vector<int>& nums) {       
     /* Method: using vector<int>::reverse_iterator rit = nums.rbegin(), rit++ goes from right to left
                Note: 1. We can't access to nums.rend(), so we terminate the loop at the second element
                      2. Using *(it+1) to access next element. Using *(it++), iterator will automatically increase by 1.
                      3. Return next element when count == 2
                      4. max_element(v.begin(), v.end()) returns an iterator, we need to add * to dereference.
     */
     if (nums.size() > 2) {
         sort(nums.begin(), nums.end());
         int count = 0;
         for (vector<int>::reverse_iterator it=nums.rbegin(); it!=nums.rend()-1; ++it) {
             if (*it > *(it+1)) {
                 count++;
             }
             if (count == 2) {
                 return *(it+1);
             }
         }
     }
     return *max_element(nums.begin(), nums.end());
 }
```
[python](https://github.com/yshiyi/LeetCode/edit/main/Array/414.%20Third%20Maximum%20Number.py)
```
def thirdMax(self, nums):
'''
Method: Use a counter to search for the third maximum number, if len(nums)>2.
       If there is no such number, return max(nums).
'''
nums_sorted = sorted(nums, reverse=True)
count = 0
if len(nums) > 2:
   for i in range(1, len(nums_sorted)):
       if nums_sorted[i] < nums_sorted[i-1]:
           count += 1
       if count == 2:
           return nums_sorted[i]
return max(nums)
```

### 448. Find All Numbers Disappeared in an Array
**Description:**\
Given an array of integers where 1 ≤ a\[i\] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of \[1, n\] inclusive that do not appear in this array.\
**Method:**\
Array\
* For c++, use elements in nums as index indicator, and then increase the corresponding elements in res, e.g. \[4,3,2,7,8,2,3,1\] -> res = \[0 1 2 2 1 0 0 1 1\]. Finally, save the index numbers which contain zero
* For python, use set() to compare. The first set contains the numbers from 1 to len(nums)+1. The second set contains the numbers in nums.\
   A.difference(B): for A - B, elements in A but not in B\
   B.difference(A): for B - A, elements in B but not in A\

[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array.cpp)
```
vector<int> findDisappearedNumbers(vector<int>& nums) {
     vector <int> res;
     res.assign(nums.size()+1,0);
     for (int i = 0; i < nums.size();i++){
         res[nums[i]]++;
     }        
     nums.erase(nums.begin(),nums.end());        
     for (int i = 1; i < res.size();i++){
         if (res[i] == 0){
             nums.push_back(i);
         }
     }
     return nums;
   }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/448.%20Find%20All%20Numbers%20Disappeared%20in%20an%20Array.py)
```
def findDisappearedNumbers(self, nums):
     standard = set(range(1,len(nums)+1))
     nums = set(nums)
     missing = list(standard.difference(nums)) # for standard - nums, numbers in standard but not in nums
     return missing
```



## 3. Remove or remove elements within array
* [1089. Duplicate zeros](#1089-Duplicate-zeros)
* [26. Remove Duplicates from Sorted Array](#26-Remove-Duplicates-from-Sorted-Array)
* [27. Remove Element](#27-Remove-Element)
* [283. Move Zeroes](#283-Move-Zeroes)

### 1089. Duplicate zeros
**Description:**\
Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.\
**Method:**\
Array\
Search for zeros from left and count the number of ones need to be shifted. When there is a 0, reduce the array size by 1. For the edge case, when there is a 0 at left == length_ - possible_dups, we just simply copy this zero without duplicating it. Finally, start backwards from the last element, we copy zeros twice and non-zeros once.\
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/1089.%20Duplicate%20Zeros.cpp) | [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/1089.%20Duplicate%20Zeros.py) |
|:-- | :-- |
|<pre>void duplicateZeros(vector<int>& arr) {<br>        int nums_zeros = 0;<br>        int l = arr.size();<br>        for (int i=0; i<l; i++) {<br>            if (i > l - nums_zeros - 1) {<br>                break;<br>            }<br>            if (arr[i] == 0) {<br>                if (i == l - nums_zeros - 1) {<br>                    arr[l-1]=0;<br>                    l--;<br>                    break;<br>                }<br>                nums_zeros++;<br>            }<br>        }<br>        int j = l - nums_zeros - 1;<br>        for (j; j>-1; j--) {<br>            if (arr[j] == 0) {<br>                arr[j + nums_zeros] = 0;<br>                nums_zeros--;<br>                arr[j + nums_zeros] = 0;<br>            }else {<br>                arr[j + nums_zeros] = arr[j];<br>            }<br>        }<br>    } </pre> |<pre>possible_dups = 0<br>        length_ = len(arr) - 1<br>        # Find the number of zeros to be duplicated<br>        for left in range(length_ + 1):<br>            # Stop when left points beyond the last element in the original list<br>            # which would be part of the modified list<br>            if left > length_ - possible_dups:<br>                break<br>            # Count the zeros<br>            if arr[left] == 0:<br>                # Edge case: This zero can't be duplicated. We have no more space,<br>                # as left is pointing to the last element which could be included<br>                if left == length_ - possible_dups:<br>                    arr[length_] = 0 # For this zero we just copy it without duplication.<br>                    length_ -= 1<br>                    break<br>                possible_dups += 1<br>        # Start backwards from the last element which would be part of new list.<br>        last = length_ - possible_dups<br>        # Copy zero twice, and non zero once.<br>        for i in range(last, -1, -1):<br>            if arr[i] == 0:<br>                arr[i + possible_dups] = 0<br>                possible_dups -= 1<br>                arr[i + possible_dups] = 0<br>            else:<br>                arr[i + possible_dups] = arr[i]<br> </pre>|

### 26. Remove Duplicates from Sorted Array
**Description:**\
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.\
**Method:**\
Array, Two pointers\
Create two pointers. One sweeps the whole array, the other pointer stops at the duplicate element position.\
For c++, we can also use erase() function
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/26.%20Remove%20Duplicates%20from%20Sorted%20Array.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py)|
|:-- |:-- |
|<pre>int removeDuplicates(vector<int>& nums) {<br>        // Method 1: two pointers, erase duplicates<br>        if (nums.size()<1) {<br>            return nums.size();<br>        }<br>        vector\<int\>::iterator it = nums.begin()+1;<br>        int i = 1, l = nums.size();<br>        while (i < l) {<br>            if (nums[i] == nums[i-1]) {<br>                nums.erase(it);<br>                l--;<br>            }else {<br>                i++;<br>                it++;<br>            }<br>        }<br>        return nums.size();<br>        // Method 2: two pointers, move the distinct element front<br>        if(nums.size()<=1) return nums.size();<br>        int j = 1;<br>        for(int i=1;i<nums.size();i++){<br>            if(nums[i]!=nums[i-1]) {<br>                nums[j] = nums[i];<br>                j++;<br>            }<br>        }<br>        return j;<br>    } </pre>|<pre>def removeDuplicates(self, nums):<br>        '''<br>        Method 1: The problem is to return the first n elements where n is the number of distinguish elements.<br>                  Hence, we only need to compare elements one by one. If we encounter a different element, we put it in front.<br>                  This is a kind of two pointer method.<br>                  The first pointer sweeps the entire array. <br>                  The second pointer counts the number of distinct elements.<br>                  When the first pointer points to a distinct element (different from the previous one).<br>                  We move this element to the position where the second pointer is pointing to.<br>                  This method takes about 12 ms.<br>        '''<br>        len_ = 1<br>        if len(nums)==0:<br>            return 0<br>        for i in range(1,len(nums)):<br>            if nums[i] != nums[i-1]:<br>                nums[len_] = nums[i]<br>                len_ +=1<br>        return len_ </pre>|

### 27. Remove Element
**Description:**\
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.\
**Method:**\
Array, Two Pointers\
Move the last element to front (the position (=val)) and remove the last element
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/27.%20Remove%20Element.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/27.%20Remove%20Element.py)|
|:-- |:-- |
|<pre>int removeElement(vector<int>& nums, int val) {<br>        if (nums.size() < 1) {return nums.size();}<br>        // Method: move the last element to front and remove the last element.<br>        int i=0, l=nums.size();<br>        vector\<int\>::iterator it = nums.end();<br>        while (i<l) {<br>            if (nums[i] == val) {<br>                nums[i] = nums[l-1];<br>                nums.erase(it-1);<br>                it--;<br>                l--;<br>            }else{<br>                i++;<br>            }<br>        }<br>        return l;<br>    } </pre>|<pre>def removeElement(self, nums, val):<br>       '''<br>       Method : This is an in-place operation method.<br>                When nums[i] = val, we move the last element in the array to position i, remove the last element <br>                from the array and reduce the length of array by 1.<br>       '''<br>        i = 0<br>        L = len(nums)<br>        while i < L:<br>            if nums[i] == val:<br>                nums[i] = nums[-1]<br>                del nums[-1]<br>                L -= 1<br>            else:<br>                i += 1<br>        return L </pre>|

### 283. Move Zeroes
**Description:**\
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.\
**Method:**\
Array, Two Pointers\
Similar to 26. Create two pointer. The first one sweeps the whole array, the second one only moves when encounters a nonzero element.
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/283.%20Move%20Zeros.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/283.%20Move%20Zeros.py)|
|:-- |:-- |
|<pre> void moveZeroes(vector\<int\>& nums) {<br>        if (nums.size() < 1) {return;}<br>        int i = 0, j = 0, temp;<br>        for (i; i<nums.size(); i++) {<br>            if (nums[i] != 0) {<br>                temp = nums[j];<br>                nums[j] = nums[i];<br>                nums[i] = temp;<br>                j++;<br>            }<br>        }<br>    }</pre>|<pre>def moveZeroes(self, nums):<br>        '''<br>        Method: Create two pointers.<br>                Pointer i sweeps the entire array. Pointer count points to the zero position.<br>                Starting from the first element, when there is a zero, we stop count and keep increasing i.<br>                When there is nonzero element, we move this element to the position where count is pointing to.<br>                This operation only excutes when i != count (i.e., there is a zero element in front).<br>        '''<br>        i = 0<br>        count = 0<br>        if len(nums) < 2:<br>            return nums<br>        for i in range(len(nums)):<br>            if nums[i] != 0:<br>                if i != count:<br>                    nums[count] = nums[i]<br>                    nums[i] = 0<br>                count += 1<br>        return nums </pre>|


## 4. Two pointers
* [1299. Replace Elements with Greatest Element on Right Side](#1299-Replace-Elements-with-Greatest-Element-on-Right-Side)
* [15M. 3Sum](#15M-3Sum)
* [167. Two Sum II - Input array is sorted](#167-Two-Sum-II-Input-array-is-sorted)
* [344. Reverse String](#344-Reverse-String)
* [88. Merge Sorted Array](#88-Merge-Sorted-Array)
* [905. Sort Array By Parity](#905-Sort-Array-By-Parity)
* [209M. Minimum Size Subarray Sum](#209M-Minimum-Size-Subarray-Sum)

### 1299. Replace Elements with Greatest Element on Right Side
**Description:**\
Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
and replace the last element with -1.\
**Method:**\
Array, sweep through the array from the back.
Save the current element to t, and find out the maximum between t and current max temp.
| [.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/1299.%20Replace%20Elements%20with%20Greatest%20Element%20on%20Right%20Side.cpp) | [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/1299.%20Replace%20Elements%20with%20Greatest%20Element%20on%20Right%20Side.py)|
|:-- |:-- |
|<pre>vector<int> replaceElements(vector<int>& arr) {<br>        int l = arr.size();<br>        int max = arr[l-1], temp = -1, t;<br>        for (int i=l-1; i>-1; i--) {<br>            t = arr[i];<br>            arr[i] = temp;<br>            temp = std::max(temp, t);<br>        }<br>        return arr;<br>    }  </pre>|<pre>def replaceElements(self, arr):<br>        temp = -1<br>        for i in range(len(arr)-1, -1, -1):<br>            t = arr[i]<br>            arr[i] = temp<br>            temp = max(temp, t)<br>        return arr</pre>|

### 15M. 3Sum
**Description:**\
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.\
**Method:**\
Use two pointers.\
Sort the array first. The first pointer starts from the next number, and the second pointer starts from the end of array. If the summation is greater than zero, the second pointer moves backward. If the summation is less than zero, the first pointer moves forward. If the summation is equal to zero, we save the triplets and move to next element. If next number is the same, then we skip this number and move to next one.
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/15M.%203Sum.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/15M.%203Sum.py)|
|:-- |:-- |
|<pre>vector<vector\<int\>> threeSum(vector<int>& nums) {<br>        vector<vector\<int\>> result;<br>        vector\<int\> triplet;<br>        int r, l, sum;<br>        sort(nums.begin(), nums.end());<br>        for (int i=0; i<nums.size(); i++) {<br>            if (i>0 && nums[i]==nums[i-1]) {<br>                continue;<br>            }<br>            r = nums.size() - 1;<br>            l = i + 1;<br>            while (l < r) {<br>                sum = nums[i] + nums[l] + nums[r];<br>                if (sum > 0) {<br>                    r--;<br>                }else if (sum < 0) {<br>                    l++;<br>                }else if (sum == 0) {<br>                    triplet.push_back(nums[i]);<br>                    triplet.push_back(nums[l]);<br>                    triplet.push_back(nums[r]);<br>                    result.push_back(triplet);<br>                    triplet.clear();<br>                    l++;<br>                    while (l<r && nums[l]==nums[l-1]){<br>                        l++;<br>                    }<br>                }<br>            }<br>        }<br>        return result;<br>    } </pre>|<pre>def threeSum(self, nums):<br>        res = []<br>        nums.sort()<br>        for i, a in enumerate(nums):<br>            if i > 0 and a == nums[i - 1]:<br>                continue<br>            l, r = i + 1, len(nums) - 1<br>            while l < r:<br>                threeSum = a + nums[l] + nums[r]<br>                if threeSum > 0:<br>                    r -= 1<br>                elif threeSum < 0:<br>                    l += 1<br>                else:<br>                    res.append([a, nums[l], nums[r]])<br>                    l += 1<br>                    while nums[l] == nums[l - 1] and l < r:<br>                        l += 1<br>        return res </pre>|

### 167. Two Sum II Input array is sorted
**Description:**\
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length. You may assume that each input would have exactly one solution and you may not use the same element twice.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/167.%20Two%20Sum%20II%20-%20Input%20array%20is%20sorted.cpp)
```
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size()-1;
        vector<int> res;
        while(left<right){
            int sum = numbers[left] + numbers[right];
            if(sum==target){
                res.push_back(left+1);
                res.push_back(right+1);
                break;
            }else if(sum>target){
                right--;
            }else if(sum<target){
                left++;
            }
        }
        return res;
    }
};
```

### 344. Reverse String
**Description:**\
Write a function that reverses a string. The input string is given as an array of characters s.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/344.%20Reverse%20String.cpp)
```
class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0, right = s.size() - 1;
        while(left < right){
            swap(s[left], s[right]);
            right--;
            left++;
        }
    }
};
```


### 88. Merge Sorted Array
**Description:**\
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.\
**Method:**\
Array, Two Pointers\
Create a new array to hold all elements and put them back to nums at the end.\
We create two pointers. \
In the main loop, we sweep the array nums1 and compare each element in nums1 to nums2.\
We save the smaller element to the new array. \
If this element comes from nums2, we then increase the counter index.\
In the second loop, I put any left elements in nums2 (they are greater then all elements in nums1) to the new array.\
At the end, we transfer all elements from the new array to nums1.\
[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/88.%20Merge%20Sorted%20Array.cpp)
```
void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
     // Method: put all elements to a new vector first, and then sort nums3.
     vector<int> nums3;
     int i = 0;

     // Check if nums1 is empty
     if (nums1.size()>0) {
         while (i < m) {
             nums3.push_back(nums1[i]);
             i++;
         }
     }

     // Check if nums2 is empty
     if (n>0) {
         for (int j = 0; j<n; j++) {
             nums3.push_back(nums2[j]);
         }
     }

     // Check if nums3 is empty
     if (nums3.size()>0) {
         sort(nums3.begin(), nums3.end());
         nums1 = nums3;
     }
 }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/88.%20Merge%20Sorted%20Array.py)
```
def merge(self, nums1, m, nums2, n):
     arr= []
     index=0
     for i in range(m):
         if index < n and nums1[i] < nums2[index]:
             arr.append(nums1[i])
         else:
             while index < n and nums2[index] < nums1[i]:
                 arr.append(nums2[index])
                 index += 1
             arr.append(nums1[i])

     for i in range(index,n):
         arr.append(nums2[i])
     for j in range(len(arr)):
         nums1[j] = arr[j]
     return nums1
```

### 905. Sort Array By Parity
**Description:**\
Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
**Method:**\
Array, Two Pointers\
The first pointer sweeps the entire array and searches for the even elements. The second pointer counts the number of even numbers. It stops at the odd element positions.\
[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/905.%20Sort%20Array%20By%20Parity.cpp)
```
vector<int> sortArrayByParity(vector<int>& A) {
     int j=0, tmp;
     for (int i=0; i<A.size(); i++) {
         if (A[i]%2==0) {
             swap(A[j], A[i]);
             j++;
         }
     }
     return A;
 }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/905.%20Sort%20Array%20By%20Parity.py)
```
def sortArrayByParity(self, A):
     count = 0
     for i in range(len(A)):
         if A[i] % 2 == 0:
             A[count], A[i] = A[i], A[count]
             count += 1
     return A
```

### 209M. Minimum Size Subarray Sum
**Description:**\
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray \[numsl, numsl+1, ..., numsr-1, numsr\] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.\
**Method:**\
Sliding windows.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/String/209M.%20Minimum%20Size%20Subarray%20Sum.cpp)
```
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        if(nums[0]>=target){
            return 1;
        }
        
        int left=0, right=1;
        int sum = nums[0], min_len = INT_MAX;
        while(right < nums.size()){
            sum = sum + nums[right];
            while(sum>=target){
                min_len = min(min_len, right-left+1);
                sum = sum - nums[left];
                left++;
            }
            right++;
        }
        if(min_len==INT_MAX){
            return 0;
        }else{
            return min_len;
        }
    }
};
```


## 5. Peak and valley
* [122. Best time to Buy and Sell Stock II](#122-Best-time-to-Buy-and-Sell-Stock-II)
* [941. Valid Mountain Array](#941-Valid-Mountain-Array)

Use the template to find out the peak and valley.
```
for (int i = 0; i<.size()-1; i++) {
   // walk up
   while (i < .size()-1 && prices[i] < prices[i+1]) {
      i++;
   }
   peak = prices[i];
   // walk down
   while (i < .size()-1 && prices[i] > prices[i+1]) {
      i++;
   }
   valley = prices[i];

}
```

### 122. Best time to Buy and Sell Stock II
**Description:**\
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).\
**Method:**\
Array, Greedy\
a. Sum up all difference between peaks and vallies\
b. Sum up all increasement if the value is increasing\
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.cpp) | [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.py) |
|:-- | :-- |
| <pre> int maxProfit(vector<int>& prices) {<br>        int profit = 0, buy = 0, sell = 0;<br>        int l = prices.size();<br>        // Method 1:<br>        for (int i=0; i<l-1; i++) {<br>            while (i<l-1 && prices[i] >= prices[i+1]) {<br>                i++;<br>            }<br>            buy = prices[i];<br>            while (i<l-1 && prices[i] <= prices[i+1]) {<br>                i++;<br>            }<br>            sell = prices[i];<br>            profit += sell - buy;<br>        }<br>        // Method 2:<br>        for (int i=0; i<l-1; i++) {<br>            if (prices[i+1]>prices[i]) {<br>                profit += prices[i+1] - prices[i];<br>            }<br>        }<br>        return profit;<br>    } </pre> |<pre> def maxProfit(self, prices):<br>        '''<br>        Method 1: Simply search for buy and sell value (i.e., valley and peak).<br>                  The total profit is the summation of all possible difference between peak and valley.<br>        '''<br>        profit = 0<br>        buy = prices[0]<br>        sell = prices[0]<br>        i = 0<br>        while i < len(prices) - 1:<br>            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:<br>                i += 1<br>            buy = prices[i]<br>            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:<br>                i += 1<br>            sell = prices[i]<br>            profit += sell - buy<br>        return profit<br>        '''<br>        Method 2: Simply add the increasement at each step if the value is increasing.<br>        '''<br>        profit = 0<br>        for i in range(len(prices) - 1):<br>            if prices[i + 1] > prices[i]:<br>                profit += prices[i + 1] - prices[i]<br>        return profit </pre>|

### 941. Valid Mountain Array
**Description:**\
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
* A.length >= 3
* There exists some i with 0 < i < A.length - 1 such that:\
      A[0] < A[1] < ... A[i-1] < A[i]\
      A[i] > A[i+1] > ... > A[A.length - 1]\
**Method:**\
Array\
At first, we walk up from left to right, and save the index when we reach the peak. If the peak is at the start or at the end, it is not a mountain. After we reach the peak, we keep walking down to the right. If we stop at the end, then it is a mountain.\
[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/941.%20Valid%20Mountain%20Array.cpp)
```
bool validMountainArray(vector<int>& arr) {
     /* Method: There are some things need to notice
                If start from i=1, need to check i<arr.size() in the while loops, 
                check (i==1||i==arr.size()) in if, and return i==arr.size();
     */
     if (arr.size()<3) {
         return false;
     }
     int i=0;
     while (i < arr.size()-1 && arr[i] < arr[i+1]) {
         i++;
     }
     if (i==0 || i==arr.size()-1) {
         return false;
     }
     while (i < arr.size()-1 && arr[i] > arr[i+1]) {
         i++;
     }
     return i==arr.size()-1;
    }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/941.%20Valid%20Mountain%20Array.py)
```
def validMountainArray(self, A):
     i = 0
     # walk up
     while i < len(A) - 1 and A[i] < A[i+1]:
         i += 1
     # peak can't be first or last
     if i == 0 or i == len(A) - 1:
         return False
     # walk down
     while i < len(A) - 1 and A[i] > A[i+1]:
         i += 1
     return i == len(A)-1
```


## 6. Use some particular functions
* [1051. Height checker](#1051-Height-checker)
* [1295. Find Numbers with Even Number of Digits](#1295-Find-Numbers-with-Even-Number-of-Digits)
* [189M. Rotate Array](#189M-Rotate-Array)
* [350. Intersection of Two Arrays II](#350-Intersection-of-Two-Arrays-II)
* [36M. Valid Sudoku](#36M-Valid-Sudoku)
* [485. Max Consecutive Ones](#485-Max-Consecutive-Ones)
* [48M. Rotate Image](#48M-Rotate-Image)
* [66. Plus One](#66-Plus-One)
* [977. Squares of a Sorted Array](#977-Squares-of-a-Sorted-Array)

### 1051. Height checker
**Description:**\
Students are asked to stand in non-decreasing order of heights for an annual photo.
Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.\
**Method:** \
Array, sorted array\
Check the difference between two arrays\
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/1051.%20Height%20Checker.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/1051.%20Height%20Checker.py)|
|:-- |:-- |
|<pre> int heightChecker(vector<int>& heights) {<br>     vector<int> heights_org = heights;<br>     sort(heights.begin(), heights.end());<br>     int result = 0;<br>     for (unsigned int i=0; i < heights.size(); i++) {<br>         if (heights_org[i] != heights[i]) {<br>             result++;<br>         }<br>     }<br>     return result;<br>}</pre>  |<pre>def heightChecker(self, heights):<br>     count = 0<br>     h = heights<br>     h_sorted = sorted(h)<br>     for i in range(len(h_sorted)):<br>         if h_sorted[i] != h[i]:<br>             count += 1<br>     return count </pre> |

### 1295. Find Numbers with Even Number of Digits
**Description:**\
Given an array nums of integers, return how many of them contain an even number of digits.\
**Method:**\
Array, Convert int to str and check the length of each string\
For python, using str(). For c++, using to_string(int).

### 189M. Rotate Array
**Description:**\
Given an array, rotate the array to the right by k steps, where k is non-negative.\
**Method:**\
a. Create an extra array/vector to hold the result.\
b. Reverse array/vector three times. The 1st time, reverse the whole array/vector. The 2nd time, reverse the first k elements. The 3rd time, reverse the rest of elements.
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/189M.%20Rotate%20Array.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/189M.%20Rotate%20Array.py)|
|:-- |:-- |
|<pre>void rotate(vector<int>& nums, int k) {<br>        // Method 1: using reverse(nums.begin(), nums.end())<br>        k %= nums.size();<br>        vector<int>::iterator it = nums.begin();<br>        for (int i=0; i<k; i++) {<br>            it++;<br>        }<br>        reverse(nums.begin(), nums.end());<br>        reverse(nums.begin(), it);<br>        reverse(it, nums.end());<br>        // Method 2: Create an extra vector<br>        //           Elements will be moved to (i+k)%nums.size() position.<br>        k %= nums.size();<br>        vector<int> nums2;<br>        int l = nums.size();<br>        nums2.resize(l);<br>        for (int i=0; i<l; i++) {<br>            nums2[(i+k)%l] = nums[i];<br>        }<br>        nums.clear();<br>        for (auto v:nums2) {<br>            nums.push_back(v);<br>        }<br>    } </pre>|<pre>def rotate(self, nums, k):<br>        '''<br>        Method 1: Create an extra array<br>                  Elements will be moved to (i+k)%len(nums) position.<br>                  Runtime: 36 ms; Memory: 14.8 MB<br>        '''<br>        n = len(nums)<br>        a = [0] * n<br>        for i in range(n):<br>            a[(i + k) % n] = nums[i]<br>        nums[:] = a<br>        '''<br>        Method 2: Using reverse<br>                  At first, we reverse the entire array.<br>                  Second, we reverse the first k elements.<br>                  Third, we reverse the rest of n-k elements.<br>                  Runtime: 68 -76 ms; Memory: 13.7 - 13.8 MB<br>        '''<br>        n = len(nums)<br>        k %= n<br>        self.reverse(nums, 0, n - 1)<br>        print(nums)<br>        self.reverse(nums, 0, k - 1)<br>        print(nums)<br>        self.reverse(nums, k, n - 1)<br>        print(nums)<br>    def reverse(self, nums, start, end):<br>        while start < end:<br>            nums[start], nums[end] = nums[end], nums[start]<br>            start += 1<br>            end -= 1 </pre>|

### 350. Intersection of Two Arrays II
**Description:**\
Given two arrays, write a function to compute their intersection.\
**Method:**\
Hash Table, Two Pointers, Binary Search, Sort\
* Use set(A).intersection(B) to extract the common elements in both A and B.\
  Convert the intersection into a list.\
  For each element in the list, we find the minimum number of that element contained in both nums1 and nums2.\
  result.extend([x]\*min(nums1.count(x),nums2.count(x)))\
* Sort both nums1 and nums2 at first.\
  Count the minimum number of shared elements.\

|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/350.%20Intersection%20of%20Two%20Arrays%20II.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/350.%20Intersection%20of%20Two%20Arrays%20II.py)|
|:-- |:-- |
|<pre>vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {<br>        vector\<int\> result;<br>        result.resize(min(nums1.size(), nums2.size()));<br>        sort(nums1.begin(), nums1.end());<br>        sort(nums2.begin(), nums2.end());<br>        vector<int>::iterator it = set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), result.begin());<br>        // Note: it points to the position next to the last intersected element.<br>        //       If it is pointing to result.end(), there must be zeros. We need to remove those zeros.<br>        if (it != result.end()) {<br>            while(it!= result.end()) {<br>                result.erase(it);<br>            }<br>        }<br>        return result;<br>    } </pre>|<pre>def intersect(self, nums1, nums2):<br>        '''<br>        Method 1: Using set(A).intersection() to extract the common elements in both nums1 and nums2<br>                  Convert the intersection into a list.<br>                  For each element in the list, we find the minimum number of that element contained in both nums1 and nums2.<br>                  Extend the result list by that number of that element.<br>        '''<br>        common=list(set(nums1).intersection(nums2))<br>        result = []<br>        for x in common:<br>            result.extend([x]*min(nums1.count(x),nums2.count(x)))<br>        return result<br>        '''<br>        Method 2: Sort both nums1 and nums2 at first.<br>                  Count the minimum number of shared elements.<br>        '''<br>        nums1 = sorted(nums1)<br>        nums2 = sorted(nums2)<br>        result = []<br>        i = 0<br>        while i < len(nums1):<br>            if nums1[i] in nums2:<br>                result.extend([nums1[i]]*min(nums1.count(nums1[i]), nums2.count(nums1[i])))<br>                i += nums1.count(nums1[i])<br>            else:<br>                i += 1<br>        return result </pre>|

```
/*
Method: Using Hashtable
        Traverse nums1, record the values and their appearances.
        Then sweep through nums2. 
        If the value is in the map and its value is greater than 0, then save it to res and reduce its value in map by 1.
*/
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> m;
        vector<int> res;
        for (auto a : nums1) ++m[a];
        for (auto a : nums2) {
            if (m[a] > 0){
                res.push_back(a);
                m[a]--;
            }
        }
        return res;
    }
};
```

### 36M. Valid Sudoku
**Description:**\
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
* Each row must contain the digits 1-9 without repetition.
* Each column must contain the digits 1-9 without repetition.
* Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.\

**Method:**\
The basic idea is to look for the duplicates in each row, each column and each box. To increase the searching speed, we should use hash table (i.e., dictionary). At first, we create three lists, and each list contains nine empty dictionaries. We then move along the board. Check if the element has been seen before.
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/36M.%20Valid%20Sudoku.cpp)|[.py](https://github.com/yshiyi/LeetCode/blob/main/Array/36M.%20Valid%20Sudoku.py)|
|:-- |:-- |
|<pre> bool isValidSudoku(vector<vector<char>>& board) {<br>        // Create 3 vectors of sets and each vector contains 9 sets.<br>        vector\<set\<int\>\> v_row, v_col, v_box;<br>        v_row.resize(9);<br>        v_col.resize(9);<br>        v_box.resize(9);<br>        for (int i=0; i<board.size(); i++) {<br>            for (int j=0; j<board[i].size(); j++) {<br>                if (board[i][j] != '.') {<br>                    // For char variable, <br>                    // 1. char - '0' can convert '0' -> 0, '1' -> 1.<br>                    // 2. char c = 'a'; int ic = (int)c; value of ic is 97<br>                    int num = board[i][j]-'0';<br>                    int box_index = i/3 * 3 + j/3;<br>                    if (v_row[i].find(num)!=v_row[i].end() \|\| v_col[j].find(num) != v_col[j].end() \|\| v_box[box_index].find(num) != v_box[box_index].end()) {<br>                        return false;<br>                    }else {<br>                        v_row[i].insert(num);<br>                        v_col[j].insert(num);<br>                        v_box[box_index].insert(num);<br>                    }<br>                }<br>            }<br>        }<br>        return true;<br>    }</pre>|<pre>def isValidSudoku(self, board):<br>        # Initiate 3 lists, each list contains 9 dictionaries<br>        rows = [{} for i in range(9)]<br>        columns = [{} for i in range(9)]<br>        boxes = [{} for i in range(9)]<br>        # validate a board<br>        # Starting from each row<br>        for i in range(9):<br>            # Sweep each column<br>            for j in range(9):<br>                num = board[i][j]<br>                if num != '.':<br>                    num = int(num)<br>                    box_index = (i \/\/ 3 ) * 3 + j \/\/ 3<br>                    if num not in rows[i] and num not in columns[j] and num not in boxes[box_index]:<br>                        rows[i][num] = i<br>                        columns[j][num] = j<br>                        boxes[box_index][num] = box_index<br>                    else:<br>                        return False<br>        return True<br> </pre>|

### 485. Max Consecutive Ones
**Description:**\
Given a binary array, find the maximum number of consecutive 1s in this array.\
**Method:**\
Array\
a. The basic idea is to loop the array from the beginning and count the number of 1s. When the element is equal to 1, we increase the value of count and compare it to the value of count_max. Update the value of max_count, if the current count is greater than the recorded maximum count. When the element is equal to 0, we reset the value of count by making it equal to 0.\
b. Or we can compare count with count_max when the element is not equal to 1. But in this case, we need to return max(count, count_max) at the end.\
[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/485.%20Max%20Consecutive%20Ones.cpp)
```
int findMaxConsecutiveOnes(vector<int>& nums) {
     int counter = 0, max_ones = 0;
     for (int i=0; i<nums.size(); i++) {
         if (nums[i]==1) {
             counter++;
         }else {
             if (counter > max_ones){
                 max_ones = counter;
             }
             counter = 0;
         }
     }
     return max(max_ones, counter);
}
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/485.%20Max%20Consecutive%20Ones.py)
```
def findMaxConsecutiveOnes(self, nums):
     count = 0  # Record the number of 1s
     count_max = 0  # Record the maximum number of 1s has been counted
     for i in range(len(nums)):
         if nums[i] == 1:
             count += 1
             if count > count_max:
                 count_max = count
         else:
             count = 0
     return count_max
```

### 48M. Rotate Image
**Description:**\
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
**Method:**\
Rotate Four rectangles
For a 3\*3 matrix, observe that (0,0) -> (2,0) -> (2,2) -> (0,2).
We only need to do this rotation for half of the matrix (i.e., len(matrix)//2). 
If the size of the matrix is an odd number, we only need to do the rotation for less than half of the matrix.
As moving down the matrix, we can gradually consider two less element (i.e., one at the beginning and one at the end).\
Time complexity: O(N^2); Space complexity: O(1)\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/48M.%20Rotate%20Image.cpp)
```
void rotate(vector<vector<int>>& matrix) {
     int l = matrix.size(), temp;
     for (int i=0; i<l/2; i++) {
         for (int j=0+i; j<l-i-1; j++) {
             temp = matrix[i][j];
             matrix[i][j] = matrix[l-j-1][i];
             matrix[l-j-1][i] = matrix[l-i-1][l-j-1];
             matrix[l-i-1][l-j-1] = matrix[j][l-i-1];
             matrix[j][l-i-1] = temp;
         }
     }
 }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/48M.%20Rotate%20Image.py)
```
def rotate(self, matrix):
     l = len(matrix)
     for i in range(l // 2):
         for j in range(0 + i, l - i - 1, 1):
             tmp = matrix[i][j]
             matrix[i][j] = matrix[l-j-1][i]
             matrix[l-j-1][i] = matrix[l-i-1][l-j-1]
             matrix[l-i-1][l-j-1] = matrix[j][l-i-1]
             matrix[j][l-i-1] = tmp
```

### 66. Plus One
**Description:**\
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.\
**Method:**\
Array\
We simply check the value of each digit from the end. If it is equal to 9, we let it be 0. If it is not equal to 9, the operation should end and return the result. If all digits are 9, we then insert 1 at the first position and return the result. return \[1\] + result\
[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/66.%20Plus%20One.cpp)
```
vector<int> plusOne(vector<int>& digits) {
     // Method: using reverse_iterator
     vector<int>::reverse_iterator rit = digits.rbegin();
     for (rit; rit!=digits.rend(); rit++) {
         if (*rit != 9) {
             ++(*rit);
             return digits;
         }else {
             *rit = 0;
         }
     }
     vector<int> res;
     res.resize(digits.size()+1);
     res[0] = 1;
     for (int i=1; i<res.size(); i++) {
         res[i] = digits[i-1];
     }
     return res;
 }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/66.%20Plus%20One.py)
```
def plusOne(self, digits):
     for i in range(len(digits)-1, -1, -1):
         if digits[i] == 9:
             digits[i] = 0
         else:
             digits[i] += 1
             return digits
     # digits.insert(0, 1)
     return [1] + digits
```

### 724. Find Pivot Index
**Description:**\
Given an array of integers nums, calculate the pivot index of this array.\
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.\
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.\
Return the leftmost pivot index. If no such index exists, return -1.\
**Method:**\
1. Using hash table
2. Summing up all elements, take the sum from left and check.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/724.%20Find%20Pivot%20Index.cpp)
```
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        if(nums.size()==1 && nums[0]==0){
            return 0;
        }else if(nums.size()==1 && nums[0]!=0){
            return -1;
        }
        unordered_map<int, int> m;
        m[nums.size()-1] = 0;
        int sum_right = 0;
        for(int j=nums.size()-2; j>-1; j--){
            sum_right = sum_right + nums[j+1];
            m[j] = sum_right;
        }
        if(m[0]==0){
            return 0;
        }
        int sum = 0;
        for(int i=1;i<nums.size();i++){
            sum = sum + nums[i-1];
            if(sum==m[i]){
                return i;
            }
        }
        
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/724.%20Find%20Pivot%20Index.py)
```
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```


### 977. Squares of a Sorted Array
**Description:**\
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.\
**Method:**\
Array, Two Pointers\
* use the default function sort() and simplified loop\
* Create two pointers: i and j.\
  j: counts the number of negative elements, points to the first non-negative element.\
  i: points to the largest negative element.\
  Then we start to compare elements from j to N and from i to 0.\
  When j reaches to N or i reaches to 0, we stop the loop. \
  Then add the rest of array (i.e., A\[:i\] or A\[j:\]) to the end of answer.\

[c++](https://github.com/yshiyi/LeetCode/blob/main/Array/977.%20Squares%20of%20a%20Sorted%20Array.cpp)
```
vector<int> sortedSquares(vector<int>& nums) {
     for (unsigned int i=0; i<nums.size(); i++) {
         nums[i] = pow(nums[i], 2);
     }
     sort(nums.begin(), nums.end());
     return nums;
 }
```
[python](https://github.com/yshiyi/LeetCode/blob/main/Array/977.%20Squares%20of%20a%20Sorted%20Array.py)
```
def sortedSquares(self, A):
     # Method 1: use the default function sort() and simplified loop
     return sorted(x*x for x in A)


     # Method 2: square every element in the array and write a function to implement quicksort algorithm.
     A_square = [x * x for x in A]
     return self.quickSort(A_square)

 def quickSort(self, nums):
     if len(nums) < 2:
         return nums
     else:
         pivot = nums[0]
         less = [i for i in nums[1:] if i <= pivot]
         greater = [i for i in nums[1:] if i > pivot]
         return self.quickSort(less) + [pivot] + self.quickSort(greater)


     '''
     Method 3: Create two pointers: i and j.
               j: counts the number of negative elements, points to the first non-negative element.
               i: points to the largest negative element.
               Then we start to compare elements from j to N and from i to 0.
               When j reaches to N or i reaches to 0, we stop the loop. 
               Then add the rest of array (i.e., A[:i] or A[j:]) to the end of answer.
     '''
     N = len(A)
     # i, j: negative, positive parts
     j = 0
     while j < N and A[j] < 0:
         j += 1
     i = j - 1

     ans = []
     while 0 <= i and j < N:
         if A[i]**2 < A[j]**2:
             ans.append(A[i]**2)
             i -= 1
         else:
             ans.append(A[j]**2)
             j += 1

     while i >= 0:
         ans.append(A[i]**2)
         i -= 1
     while j < N:
         ans.append(A[j]**2)
         j += 1

     return ans
```

### 84H. Largest Rectangle in Histogram
**Description:**\
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.\
**Example:**\
Input: heights = \[2,1,5,6,2,3\]\
Output: 10\
Explanation: The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units.\
**Method:**\
Using Stack\
The technique is called monotonous stack in which we save the elements in monotonous sequence.\
In this problem, the area of the rectangle depends on the smallest integer.\
Hence, the values saved in the stack should be monotonically increasing.\
The basic procedure is:\
1. We save the values into a stack.
2. When we encounter a value that is smaller than the previous one (i.e., the top one in the stack),
   we pop out the top value can calculate the area of the rectangle it can construct.
3. Then we check out the new top value. If it is still smaller than the current value, we repeat step 2.
   We save the current value to the stack until there are no values greater than it.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Array/84H.%20Largest%20Rectangle%20in%20Histogram.cpp)
```
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = 0;
        // This stack saves the index of values instead of the values themself.
        stack<int> s;
        // Insert an extra 0 at the end of the array so that we can easily check the last value in the array.
        heights.push_back(0);
        for(int i=0; i<heights.size(); i++){
            // If we encounter a value that is smaller than the top value in the stack, 
            // we start to calculate the area of rectangle.
            while(!s.empty() && heights[s.top()] >= heights[i]){
                // We first save and pop out the top index.
                int cur = s.top(); s.pop();
                /* This part is tricky.
                   If the stack becomes empty, it means the current index contains the smallest value in the array so far.
                   Hence, the length of the area of the rectangle that it can construct is just the current index i.
                   If the stack is not empty, the length is i - s.top() - 1.
                   Note, the new top index must be the index right before cur. 
                   Imagine a sequence [1,3,2,4,7], 1 and 3 are processed when we get to 2. 
                */
                int length = s.empty() ? i : (i - s.top() - 1);
                int area = heights[cur] * length;
                res = max(res, area);
            }
            s.push(i);
        }
        return res;
    }
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Array/84H.%20Largest%20Rectangle%20in%20Histogram.py)
```
class Solution(object):
    def largestRectangleArea(self, heights):
        res = 0
        st = collections.deque()
        heights.append(0)
        for i in range(len(heights)):
            # We can also use
            # st and heights[st[-1]] >= heights[i]
            # This is faster than len(st)
            while len(st) and heights[st[-1]] >= heights[i]:
                cur = st[-1]
                st.pop()
                if len(st)==0:
                    length = i
                else:
                    length = i - st[-1] - 1
                area = heights[cur] * length
                res = max(res, area)
            st.append(i)
        return res
```
