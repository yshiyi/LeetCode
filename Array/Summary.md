# Array
This is a brief summary of all the problems in this folder.
There are a number of typical methods to solve particular problems:\
1. Search for a particular number, or check duplicates\
Hash Table. ex.: easy - [01](#1-Two-Sum-(-Search-for-a-certain-number-)), 136, 217, 350; medium - 36\
2. Peak and Valley\
Use the template to find out the peak. ex.: [122](#122-Best-time-to-Buy-and-Sell-Stock-II), 941
```
for (int i = 0; i<.size()-1; i++) {
   while (i < .size()-1 && prices[i] > prices[i+1]) {
      i++;
   }
   valley = prices[i];
   while (i < .size()-1 && prices[i] < prices[i+1]) {
      i++;
   }
   peak = prices[i];
   increasement += peak - valley;
}
```
**3.** Require in-place operation, remove duplicates/a particular element (26, 27), move elements within array (283),
   merge two arrays (88, 905, 977)\
   Two pointers\
**4.** Use some particular functions:\
   set() - 217\
   set(A).intersection(B) - 350\
   A.difference(B): for A - B, elements in A but not in B - 448\
   B.difference(A): for B - A, elements in B but not in A - 448\



## 1. Two Sum (Search for a certain number)
Hash Table\
Create a dictionary.\
|                                                                                                                                                                                                                  [.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/01.%20Two%20Sum.cpp)                                                                                                                                                                                                                 |                                                                                                                                      [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/01.%20Two%20Sum.py)                                                                                                                                     |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  <pre> vector<int> twoSum(vector<int>& nums, int target) { <br>   map<int, int> m;<br>   int l = nums.size();<br>   map<int, int>::iterator it;<br>   vector<int> result;<br>   for (int i=0; i<l; i++) {<br>       it = m.find(target - nums[i]);<br>       if(it==m.end()) {<br>           m.insert(make_pair(nums[i], i));<br>       }else {<br>           result.push_back(i);<br>           // result.push_back(m[target-nums[i]]);<br>           result.push_back((*it).second);<br>           break;<br>       }<br>   }<br>   return result;<br> }  </pre>|  <pre>def twoSum(self, nums, target):<br>       h = {}<br>       for i, num in enumerate(nums):<br>           \\ Method 1:<br>           n = target - num<br>           if n not in h:<br>               h[num] = i<br>           else:<br>               return [h[n], i]<br>            \\ Method 2:<br>           if n in nums:<br>               index = [i, nums.index(n)]<br>           break </pre> |



## 1051.Height checker:
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


## 1089. Duplicate zeros:
**Description:**\
Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.\
**Method:**\
Array\
Shift array by one\
|[.cpp](https://github.com/yshiyi/LeetCode/blob/main/Array/1089.%20Duplicate%20Zeros.cpp) | [.py](https://github.com/yshiyi/LeetCode/blob/main/Array/1089.%20Duplicate%20Zeros.py) |
|:-- | :-- |
|<pre>void duplicateZeros(vector<int>& arr) {<br>        int nums_zeros = 0;<br>        int l = arr.size();<br>        for (int i=0; i<l; i++) {<br>            if (i > l - nums_zeros - 1) {<br>                break;<br>            }<br>            if (arr[i] == 0) {<br>                if (i == l - nums_zeros - 1) {<br>                    arr[l-1]=0;<br>                    l--;<br>                    break;<br>                }<br>                nums_zeros++;<br>            }<br>        }<br>        int j = l - nums_zeros - 1;<br>        for (j; j>-1; j--) {<br>            if (arr[j] == 0) {<br>                arr[j + nums_zeros] = 0;<br>                nums_zeros--;<br>                arr[j + nums_zeros] = 0;<br>            }else {<br>                arr[j + nums_zeros] = arr[j];<br>            }<br>        }<br>    } </pre> |<pre>possible_dups = 0<br>        length_ = len(arr) - 1<br>        # Find the number of zeros to be duplicated<br>        for left in range(length_ + 1):<br>            # Stop when left points beyond the last element in the original list<br>            # which would be part of the modified list<br>            if left > length_ - possible_dups:<br>                break<br>            # Count the zeros<br>            if arr[left] == 0:<br>                # Edge case: This zero can't be duplicated. We have no more space,<br>                # as left is pointing to the last element which could be included<br>                if left == length_ - possible_dups:<br>                    arr[length_] = 0 # For this zero we just copy it without duplication.<br>                    length_ -= 1<br>                    break<br>                possible_dups += 1<br>        # Start backwards from the last element which would be part of new list.<br>        last = length_ - possible_dups<br>        # Copy zero twice, and non zero once.<br>        for i in range(last, -1, -1):<br>            if arr[i] == 0:<br>                arr[i + possible_dups] = 0<br>                possible_dups -= 1<br>                arr[i + possible_dups] = 0<br>            else:<br>                arr[i + possible_dups] = arr[i]<br> </pre>|

## 122. Best time to Buy and Sell Stock II
**Description:**\
Say you have an array prices for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).\
**Method:**\
Array, Greedy\
a. Sum up all difference between peaks and vallies\
b. Sum up all increasement if the value is increasing\
|[.cpp]() | [.py]() |
|:-- | :-- |
| <pre> int maxProfit(vector<int>& prices) {<br>        int profit = 0, buy = 0, sell = 0;<br>        int l = prices.size();<br>        // Method 1:<br>        for (int i=0; i<l-1; i++) {<br>            while (i<l-1 && prices[i] >= prices[i+1]) {<br>                i++;<br>            }<br>            buy = prices[i];<br>            while (i<l-1 && prices[i] <= prices[i+1]) {<br>                i++;<br>            }<br>            sell = prices[i];<br>            profit += sell - buy;<br>        }<br>        // Method 2:<br>        for (int i=0; i<l-1; i++) {<br>            if (prices[i+1]>prices[i]) {<br>                profit += prices[i+1] - prices[i];<br>            }<br>        }<br>        return profit;<br>    } </pre> |<pre> def maxProfit(self, prices):<br>        '''<br>        Method 1: Simply search for buy and sell value (i.e., valley and peak).<br>                  The total profit is the summation of all possible difference between peak and valley.<br>        '''<br>        profit = 0<br>        buy = prices[0]<br>        sell = prices[0]<br>        i = 0<br>        while i < len(prices) - 1:<br>            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:<br>                i += 1<br>            buy = prices[i]<br>            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:<br>                i += 1<br>            sell = prices[i]<br>            profit += sell - buy<br>        return profit<br>        '''<br>        Method 2: Simply add the increasement at each step if the value is increasing.<br>        '''<br>        profit = 0<br>        for i in range(len(prices) - 1):<br>            if prices[i + 1] > prices[i]:<br>                profit += prices[i + 1] - prices[i]<br>        return profit </pre>|


## 1295. Find Numbers with Even Number of Digits
Array\
Convert int to str and check the length of each string\

1299. Replace Elements with Greatest Element on Right Side
Array
Sweep the array from the back.
Save the current element to t, and find out the maximum between t and current max temp.

1346. Check If N and Its Double Exist
Array
Check 'if an element in array:'

136. Single Number (Find the single number)
Hash table, Bit manipulation
Create a dictionary. Sweep the array and check which element has been seen before

217. Contains Duplicate
Array, Hash table
a. Create a hash table (i.e., dictionary). 
   Check if the element of nums is in dic. If not, add it to dic and remain dup = False.
   If it is in dic, let dup = True and return dup
b. Use set(), which only contains distinct elements

26. Remove Duplicates from Sorted Array
Array, Two pointer
Create two pointers. One sweeps the whole array, the other pointer stops at the duplicate element position

27. Remove Element (remove a particular element from an array)
Array, Two Pointers
a. Similar to 26. Create two pointers.
b. Move the last element to the position (=val) and remove the last element

283. Move Zeroes
Array, Two Pointers
Create two pointer. The first one sweeps the whole array, the second one only moves when encounters a nonzero element.

350. Intersection of Two Arrays II
Hash Table, Two Pointers, Binary Search, Sort
a. Use set(A).intersection(B) to extract the common elements in both A and B.
   Convert the intersection into a list.
   For each element in the list, we find the minimum number of that element contained in both nums1 and nums2.
   result.extend([x]*min(nums1.count(x),nums2.count(x)))
b. Using a hash table (i.e., a dictionary) to contain the distinct elements we have visit in nums1
   For each distinct element, we find the minimum number of that element contained in both nums1 and nums2.
c. Sort both nums1 and nums2 at first.
   Count the minimum number of shared elements.

414. Third Maximum Number
Array
There are three scenarios we need to consider.
The first one: there is only one element. We return the only one element.
The second one: there are two elements. We return the maximum one.
The third one: more than two elements. We sort the array reversely and use a counter to count the number
of maximum element. When we find the third maximum number, we return that number. If we can't find the 
third maximum until the end of array, we then return the first element (i.e., the largest) element.

448. Find All Numbers Disappeared in an Array
Array
a. Create nums_disappear to hold the missing numbers.
   At first, we need to check if the first number in nums is 1. If not, we add 1 to (1st number - 1) to nums_disappear.
   If the 1st number = 1, we check the rest of numbers. 
   If there is a number greater than its previous number + 1, we add the numbers between them to nums_disappear.
   When we reach to the end of nums and the last number != len(nums)+1, we add the last number to len(nums)+1 to nums_disappear.
b. Use set() to compare.
   The first set contains the numbers from 1 to len(nums)+1.
   The second set contains the numbers in nums.
   A.difference(B): for A - B, elements in A but not in B
   B.difference(A): for B - A, elements in B but not in A

485. Max Consecutive Ones
Array
The basic idea is to loop the array from the beginning and count the number of 1s.
When the element is equal to 1, we increase the value of count and compare it to the value of count_max. 
Update the value of max_count, if the current count is greater than the recorded maximum count.
When the element is equal to 0, we reset the value of count by making it equal to 0.

66. Plus One
Array
We simply check the value of each digit from the end.
If it is equal to 9, we let it be 0.
If it is not equal to 9, the operation should end and return the result.
If all digits are 9, we then insert 1 at the first position and return the result. return [1] + result

88. Merge Sorted Array
Array, Two Pointers
Create a new array to hold all elements and put them back to nums at the end.
We create two pointers. 
In the main loop, we sweep the array nums1 and compare each element in nums1 to nums2.
We save the smaller element to the new array. 
If this element comes from nums2, we then increase the counter index.
In the second loop, I put any left elements in nums2 (they are greater then all elements in nums1) to the new array.
At the end, we transfer all elements from the new array to nums1.

905. Sort Array By Parity (even numbers go first and followed by odd numbers)
Array, Two Pointers
Create two pointers.
The first pointer sweeps the entire array and searches for the even elements.
The second pointer counts the number of even numbers. It stops at the odd element positions.

941. Valid Mountain Array
Array
At first, we walk up from left to right, and save the index when we reach the peak.
If the peak is at the start or at the end, it is not a mountain.
After we reach the peak, we keep walking down to the right.
If we stop at the end, then it is a mountain.
```
# walk up
while i < len(A) - 1 and A[i] < A[i+1]:
    i += 1
# walk down
while i < len(A) - 1 and A[i] > A[i+1]:
    i += 1
```

## [977\. Squares of a Sorted Array](https://github.com/yshiyi/LeetCode/blob/main/Array/977.%20Squares%20of%20a%20Sorted%20Array.py)
Array, Two Pointers\
**Description:**\
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.\
**Method:**\
1. use the default function sort() and simplified loop\
   ```
   return sorted(x*x for x in A)
   ```
2. Create two pointers: i and j.
   j: counts the number of negative elements, points to the first non-negative element.\
   i: points to the largest negative element.\
   Then we start to compare elements from j to N and from i to 0.\
   When j reaches to N or i reaches to 0, we stop the loop. \
   Then add the rest of array (i.e., A[:i] or A[j:]) to the end of answer.\
```
while j < len(A) and A[j] < 0:
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
```

