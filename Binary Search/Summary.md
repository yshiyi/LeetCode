# Binary Search
<!-- GFM-TOC -->
* [Leetcode Binary Search](#Binary-Search)
    * [1. Introduction to Binary Search](#1-Introduction-to-Binary-Search)
       * [1.1 How to identify Binary Search](#11-How-to-identify-Binary-Search)
       * [1.2 3 Parts of a Successful Binary Search](#12-3-Parts-of-a-Successful-Binary-Search)
       * [704. Binary Search](#704-Binary-Search) 
    * [2. Template I Basic](#2-Template-I-Basic)
       * [69. Sqrt(x)](#69-Sqrtx)
       * [374. Guess Number Higher or Lower](#374-Guess-Number-Higher-or-Lower)
       * [33M. Search in Rotated Sorted Array](#33M-Search-in-Rotated-Sorted-Array)
    * [3. Template II Access Neighbor](#3-Template-II-Access-Neighbor)
       * [278. First Bad Version](#278-First-Bad-Version)
    * [4. Template III Access Both Neighbors](#4-Template-III-Access-Both-Neighbors)
<!-- GFM-TOC -->

# 1. Introduction to Binary Search
In its simplest form, Binary Search operates on a contiguous sequence with a specified left and right index. This is called the Search Space. Binary Search maintains the left, right, and middle indicies of the search space and compares the search target or applies the search condition to the middle value of the collection; if the condition is unsatisfied or values unequal, the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful. If the search ends with an empty half, the condition cannot be fulfilled and target is not found.\

## 1.1 How to identify Binary Search
Binary Search is an algorithm that divides the search space in 2 after every comparison. Binary Search should be considered every time you need to search for an index or element in a collection. If the collection is unordered, we can always sort it first before applying Binary Search.\

## 1.2 3 Parts of a Successful Binary Search
Binary Search is generally composed of 3 main sections:
1. Pre-processing - Sort if collection is unsorted.
2. Binary Search - Using a loop or recursion to divide search space in half after each comparison.
3. Post-processing - Determine viable candidates in the remaining space.

## 704. Binary Search
**Description:**\
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.\
You must write an algorithm with O(log n) runtime complexity.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/704.%20Binary%20Search.cpp)
```
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, target, 0, nums.size()-1);
    }
    int binarySearch(vector<int>& nums, int target, int left, int right){
        if(left>right){
            return -1;
        }
        int mid = (right + left)/2;
        if(nums[mid]==target){
            return mid;
        }
        if(nums[mid]>target){
            return binarySearch(nums, target, left, mid-1);
        }else{
            return binarySearch(nums, target, mid+1, right);
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/704.%20Binary%20Search.py)
```
# Method 1: Recursive approach
class Solution(object):
    def search(self, nums, target):
        def binarySearch(nums, target, left, right):
            if left > right:
                return -1
            mid = int((right+left)/2)
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                return binarySearch(nums, target, left, mid-1)
            else:
                return binarySearch(nums, target, mid+1, right) 
        return binarySearch(nums, target, 0, len(nums)-1)
        
# Method 2: Iterative approach
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((right+left)/2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
```

# 2. Template I Basic
Template #1 is the most basic and elementary form of Binary Search. It is used to search for an element or condition which can be determined by accessing a single index in the array.
**Key Attribute:**\
1. Most basic and elementary form of Binary Search
2. Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
3. No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

**Distinguishing Syntax:**\
Initial Condition: left = 0, right = length-1\
Termination: left > right\
Searching Left: right = mid-1\
Searching Right: left = mid+1\

## 69. Sqrt(x)
**Description:**\
Given a non-negative integer x, compute and return the square root of x.\
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.\
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/69.%20Sqrt(x).cpp)
```
class Solution {
public:
    int mySqrt(int x) {
        if(x<2){
            return x;
        }
        int left = 0, right = x;
        while(left<=right){
            int mid = (right+left)/2;
            if(mid<=x/mid && (mid+1)>x/(mid+1)){
                return mid;
            }
            if(mid>x/mid){
                right = mid-1;
            }
            if(mid<x/mid){
                left = mid + 1;
            }
        }
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/69.%20Sqrt(x).py)
```
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        left, right = 0, x
        while left <= right:
            mid = int(left+right)/2
            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return mid
            if mid*mid>x:
                right = mid-1
            else:
                left = mid+1
        return -1
```

## 374. Guess Number Higher or Lower
**Description:**\
We are playing the Guess Game. The game is as follows:\
I pick a number from 1 to n. You have to guess which number I picked.\
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.\
You call a pre-defined API int guess(int num), which returns 3 possible results:\
-1: The number I picked is lower than your guess (i.e. pick < num).\
1: The number I picked is higher than your guess (i.e. pick > num).\
0: The number I picked is equal to your guess (i.e. pick == num).\
Return the number that I picked.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/374.%20Guess%20Number%20Higher%20or%20Lower.cpp)
```
class Solution {
public:
    int guessNumber(int n) {
        int left = 0, right = n;
        while(left <= right){
            // Note: left + right can exceed the limit of int
            int mid = left+(right-left)/2;
            if(guess(mid)==0){
                return mid;
            }
            if(guess(mid)==1){
                left = mid + 1;
            }
            if(guess(mid)==-1){
                right = mid - 1;
            }
        }
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/374.%20Guess%20Number%20Higher%20or%20Lower.py)
```
class Solution(object):
    def guessNumber(self, n):
        left, right = 0, n
        while left<=right:
            mid = int(left+right)/2
            if guess(mid)==0:
                return mid
            if guess(mid)==1:
                left = mid + 1
            if guess(mid)==-1:
                right = mid - 1
```

## 33M. Search in Rotated Sorted Array
**Description:**\
There is an integer array nums sorted in ascending order (with distinct values).\
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is \[nums\[k\], nums\[k+1\], ..., nums\[n-1\], nums\[0\], nums\[1\], ..., nums\[k-1\]\] (0-indexed).\
For example, \[0,1,2,4,5,6,7\] might be rotated at pivot index 3 and become \[4,5,6,7,0,1,2\].\
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.\
**Method:**\
We can still use the conventional binary search approach. \
Notice, if the mid is less than right, then the right part is an ascending sequence. Otherwise, the left part is.\
Comparing to the conventional binary search, there are four scenarios we need to consider.\
Also note, since mid = left+(right-left)/2, mid could be equal to left. We need to consider this scenario as well.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/33M.%20Search%20in%20Rotated%20Sorted%20Array.cpp)
```
// Solution 1: Compare mid to right
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
    int binarySearch(vector<int>& nums, int left, int right, int target){
        if (left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid] < nums[right]){
                if(target>nums[mid] && target<=nums[right]){
                    return binarySearch(nums, mid+1, right, target);
                }else{
                    return binarySearch(nums, left, mid-1, target);
                }
            }else{
                if(target<nums[mid] && target>=nums[left]){
                    return binarySearch(nums, left, mid-1, target);
                }else{
                    return binarySearch(nums, mid+1, right, target);
                }
            }
        }
        return -1;
    }
};

// Solution 2: Compare mid to left
class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, 0, nums.size()-1, target);
    }
    int binarySearch(vector<int>& nums, int left, int right, int target){
        // cout << left << " " << right << endl;
        if (left <= right){
            int mid = left + (right-left)/2;
            // cout << nums[mid] << endl;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid] >= nums[left]){
                if(target<nums[mid] && target>=nums[left]){
                    return binarySearch(nums, left, mid-1, target);
                }else{
                    return binarySearch(nums, mid+1, right, target);
                }
            }else{
                if(target>nums[mid] && target<=nums[right]){
                    return binarySearch(nums, mid+1, right, target);
                }else{
                    return binarySearch(nums, left, mid-1, target);
                }
            }
        }
        return -1;
    }
};

// Solution: Iterative approach
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid] < nums[right]){
                if(target>nums[mid] && target<=nums[right]){
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            }else{
                if(target<nums[mid] && target>=nums[left]){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }
        }
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/33M.%20Search%20in%20Rotated%20Sorted%20Array.py)
```
class Solution(object):
    def search(self, nums, target):
        def binarySearch(nums, left, right, target):
            if left <= right:
                mid = int(left + (right-left)/2)
                if nums[mid] == target:
                    return mid
                if nums[mid] < nums[right]:
                    if nums[mid]<target and target<=nums[right]:
                        return binarySearch(nums, mid+1, right, target)
                    else:
                        return binarySearch(nums, left, mid-1, target)
                else:
                    if nums[left]<=target and target<nums[mid]:
                        return binarySearch(nums, left, mid-1, target)
                    else:
                        return binarySearch(nums, mid+1, right, target)
            return -1
        return binarySearch(nums, 0, len(nums)-1, target)
```

# 3. Template II Access Neighbor
Template #2 is an advanced form of Binary Search. It is used to search for an element or condition which requires accessing the current index and its immediate right neighbor's index in the array.\
**Key Attributes:**\
1. An advanced way to implement Binary Search.
2. Search Condition needs to access element's immediate right neighbor
3. Use element's right neighbor to determine if condition is met and decide whether to go left or right
4. Gurantees Search Space is at least 2 in size at each step
5. Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

**Distinguishing Syntax:**\
Initial Condition: left = 0, right = length\
Termination: left == right\
Searching Left: right = mid\
Searching Right: left = mid+1\

```
int binarySearch(vector<int>& nums, int target){
  if(nums.size() == 0)
    return -1;

  int left = 0, right = nums.size();
  while(left < right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid; }
  }

  // Post-processing:
  // End Condition: left == right
  if(left != nums.size() && nums[left] == target) return left;
  return -1;
}
```

## 278. First Bad Version
**Description:**
You are a product manager and currently leading a team to develop a new product. \
Unfortunately, the latest version of your product fails the quality check. \
Since each version is developed based on the previous version, all the versions after a bad version are also bad.\
Suppose you have n versions \[1, 2, ..., n\] and you want to find out the first bad one, which causes all the following ones to be bad.\
You are given an API bool isBadVersion(version) which returns whether version is bad. \
Implement a function to find the first bad version. \
You should minimize the number of calls to the API.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/278.%20First%20Bad%20Version.cpp)
```
/* 
Mehod 1: Using Template I
         There are two different approach: access the right neighbor and access the left neighbor.
         In this solution, we first check mid. If mid is false, we check the right side of the array.
         If mid is true, we check the left neighbor. If the left neightbor is false, then mid is the solution.
         Otherwise, we check the left side of array.
         We need to consider when mid == 1.
*/
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(!isBadVersion(mid)){
                left = mid + 1;
            }else{
                if(mid==1){
                    return mid;
                }
                if(!isBadVersion(mid-1)){
                    return mid;
                }else{
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};

/*
Method 2: Using Template II
          In this solution, we check the right neighbor. Hence, left < right, as left+1 will exceed the limit.
*/
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left < right){
            int mid = left + (right-left)/2;
            // If mid is false and mid+1 is true, then return mid.
            if(!isBadVersion(mid) && isBadVersion(mid+1)){
                return mid+1;
            }
            // If mid is false and mid+1 is false, we check mid+1 ~ right.
            if(!isBadVersion(mid) && !isBadVersion(mid+1)){
                left = mid + 1;
            }
            // As the condition of the while loop is left < right,
            // if right = mid - 1, then we can't examine the value at mid - 1.
            if(isBadVersion(mid)){
                right = mid;
            }
        }
        if(left==right && isBadVersion(left)){return left;}
        return -1;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/278.%20First%20Bad%20Version.py)
```
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while(left < right):
            mid = int((left+right)/2)
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            if not isBadVersion(mid) and not isBadVersion(mid+1):
                left = mid + 1
            if isBadVersion(mid):
                right = mid
        if left==right and isBadVersion(left):
            return left
```


# 4. Template III Access Both Neighbors
Template #3 is another unique form of Binary Search. It is used to search for an element or condition which requires accessing the current index and its immediate left and right neighbor's index in the array.\
**Key Attributes:**\
1. An alternative way to implement Binary Search
2. Search Condition needs to access element's immediate left and right neighbors
3. Use element's neighbors to determine if condition is met and decide whether to go left or right
4. Gurantees Search Space is at least 3 in size at each step
5. Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

**Distinguishing Syntax:**\
Initial Condition: left = 0, right = length-1\
Termination: left + 1 == right\
Searching Left: right = mid\
Searching Right: left = mid\
```
int binarySearch(vector<int>& nums, int target){
    if (nums.size() == 0)
        return -1;

    int left = 0, right = nums.size() - 1;
    while (left + 1 < right){
        // Prevent (left + right) overflow
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid;
        } else {
            right = mid;
        }
    }

    // Post-processing:
    // End Condition: left + 1 == right
    if(nums[left] == target) return left;
    if(nums[right] == target) return right;
    return -1;
}
```












