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
    * [3. Template II Access Neighbor](#3-Template-II-Access-Neighbor)
    * [4. Template III Access Both Neighbors](#4-Template-III-Access-Both-Neighbors)
    * [5. Binary Search Template Analysis](#5-Binary-Search-Template-Analysis)
    * [6. Summary](#6-Summary)
       * [6.1 Find the value equal to target](#61-Find-the-value-equal-to-target)
          * [153M. Find Minimum in Rotated Sorted Array](#153M-Find-Minimum-in-Rotated-Sorted-Array)
          * [154H. Find Minimum in Rotated Sorted Array II](#154H-Find-Minimum-in-Rotated-Sorted-Array-II)
          * [278. First Bad Version](#278-First-Bad-Version)
          * [287M. Find the Duplicate Number](#287M-Find-the-Duplicate-Number)
          * [33M. Search in Rotated Sorted Array](#33M-Search-in-Rotated-Sorted-Array)
       * [6.2 Find the first value greater than or equal to target](#62-Find-the-first-value-greater-than-or-equal-to-target)
       * [6.3 Find the first value greater than target](#63-Find-the-first-value-greater-than-target)
          * [162M. Find Peak Element](#162M-Find-Peak-Element)
       * [6.4 Use subfunction to determine the relation](#64-Use-subfunction-to-determine-the-relation)
       * [6.5 Others](#65-Others)
          * [270. Closest Binary Search Tree Value](#270-Closest-Binary-Search-Tree-Value)
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
Template #1 is the most basic and elementary form of Binary Search. It is used to search for an element or condition which can be determined by accessing a single index in the array.\
**Key Attribute:**
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

  int left = 0, right = nums.size() - 1;
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

int binarySearch(vector<int>& nums, int target){
  if(nums.size() == 0)
    return -1;
   
  // If we initialize right = nums.size(), then we don't need any post-process
  // Because, when left == right, it means the target doesn't exist
  int left = 0, right = nums.size();
  while(left < right){
    // Prevent (left + right) overflow
    int mid = left + (right - left) / 2;
    if(nums[mid] == target){ return mid; }
    else if(nums[mid] < target) { left = mid + 1; }
    else { right = mid; }
  }

  return -1;
}

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


# 5. Binary Search Template Analysis
**Template I (left<=right):**\
1. Most basic and elementary form of Binary Search
2. Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
3. No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

**Template II (left<right):**\
1. An advanced way to implement Binary Search.
2. Search Condition needs to access element's immediate right neighbor
3. Use element's right neighbor to determine if condition is met and decide whether to go left or right
4. Gurantees Search Space is at least 2 in size at each step
5. Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

**Template III (left+1<right):**\
1. An alternative way to implement Binary Search
2. Search Condition needs to access element's immediate left and right neighbors
3. Use element's neighbors to determine if condition is met and decide whether to go left or right
4. Gurantees Search Space is at least 3 in size at each step
5. Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

**Time and Space Complexity:**\
1. Runtime: O(log N) -- logorithmic time (base 2)
2. Space: O(1) -- constant space


# 6. Summary
## 6.1 Find the value equal to target
This is the typical problem of binary search. For example, nums = \[2, 3, 4, 6, 8\], target = 4.\
The code is:
```
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid;
    }
    return -1;
}
```
There are four places that we can modify:
1. The initial value of right. right = nums.size() or right = nums.size()-1
2. The relation between left and right. left < right or left <= right
3. Update of right. right = mid or right = mid - 1
4. The return value. left, right or -1

If we initialize right = nums.size(), then the condition for while loop must be left < right. Because left can't be equal to right which is out of boundary, it is not possible to calculate mid. In addition, right = mid. Because nums\[mid\]!=target, and we need to check the value before mid.\
If we initialize right = nums.size()-1, then the condition for while loop must be left<=right. In this case, left can be equal to right. In addition, right = mid - 1.



### 153M. Find Minimum in Rotated Sorted Array
**Description:**\
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = \[0,1,2,4,5,6,7\] might become:\
\[4,5,6,7,0,1,2\] if it was rotated 4 times.\
\[0,1,2,4,5,6,7\] if it was rotated 7 times.\
Notice that rotating an array \[a\[0\], a\[1\], a\[2\], ..., a\[n-1\]\] 1 time results in the array \[a\[n-1\], a\[0\], a\[1\], a\[2\], ..., a\[n-2\]\].\
Given the sorted rotated array nums of unique elements, return the minimum element of this array. You must write an algorithm that runs in O(log n) time.\
**Method:**\
Consider 33M. Search in Rotated Sorted Array.\
We first compare nums\[mid\] to nums\[right\]. If nums\[mid\] > nums\[right\], it means the min is on the right side of array. Otherwise, it is on the left side.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/153M.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.cpp)
```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[mid] > nums[right]){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return nums[left];
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/153M.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.py)
```
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left+right)/2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

### 154H. Find Minimum in Rotated Sorted Array II
**Description:**\
Similar to 153M.\
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array. You must decrease the overall operation steps as much as possible.\
**Method:**\
Since there are duplicated values, nums\[mid\] may be equal to nums\[right\].\
To deal with the duplicate values, we only need to move right pointer to the left by 1 until we get a distinct value.
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/154H.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II.cpp)
```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right - left)/2;
            if(nums[mid]>nums[right]){
                left = mid + 1;
            }else if(nums[mid]<nums[right]){
                right = mid;
            }else{
                --right;
            }
        }
        return nums[left];
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/154H.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II.py)
```
class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = int(left + (right - left)/2)
            if nums[mid]>nums[right]:
                left = mid + 1
            elif nums[mid]<nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
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
**Method:**\
The idea is simple, similar to searching for a particular value.\
If mid is not a bad version, then move left to mid + 1. Otherwise, move right to mid.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/278.%20First%20Bad%20Version.cpp)
```
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1, right = n;
        while(left < right){
            int mid = left + (right-left)/2;
            if(!isBadVersion(mid)){
                left = mid+1;
            }else{
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

### 287M. Find the Duplicate Number
**Description:**\
Given an array of integers nums containing n + 1 integers where each integer is in the range \[1, n\] inclusive.\
There is only one repeated number in nums, return this repeated number.\
You must solve the problem without modifying the array nums and uses only constant extra space.\
**Method:**\
If we want to distribute n+1 objects to n boxes, there must be one box that contains more than one object.\
Using this idea, let mid = (left + right)/2, and compare each value in nums with mid.\
If the number of values that are less than or equal to mid is greater than mid, then the duplicate value must be less than or equal to mid.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/287M.%20Find%20the%20Duplicate%20Number.cpp)
```
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left = 1, right = nums.size();
        while (left < right){
            int mid = left + (right - left) / 2, cnt = 0;
            for (int num : nums) {
                if (num <= mid) ++cnt;
            }
            if (cnt <= mid) left = mid + 1;
            else right = mid;
        }    
        return right;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/287M.%20Find%20the%20Duplicate%20Number.py)
```
class Solution(object):
    def findDuplicate(self, nums):
        left, right = 1, len(nums)
        while left < right:
            mid = (right+left)//2
            count = 0
            for v in nums:
                if v<=mid:
                    count += 1
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left
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


## 6.2 Find the first value greater than or equal to target
Or find the last value less than target.\
This is another typical problem of binary search. The difference between 6.2 and 6.1 is that the target may or may not be in nums. Or target is not unique in nums.\
In this case, nums\[mid\]==target is not necessary. \
For example, nums = \[2, 4, 5, 6, 9\], target = 3 or nums = \[0, 1, 1, 1, 1\], target = 1.
```
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] < target) left = mid + 1;
        else right = mid;
    }
    return right;
}
```
Since we have already found the first value which is greater than or equal to the target, the one before it is then the last value which is less than the target. We only need to return right - 1.

## 6.3 Find the first value greater than target
Or find the last value which is not greater than target.\
This problem is very similar to 6.2. We only need to change the if statement to nums\[mid\]<=target. Then the return value will be strictly greater than the target.
```
int find(vector<int>& nums, int target) {
    int left = 0, right = nums.size();
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] <= target) left = mid + 1;
        else right = mid;
    }
    return right;
}
```
To find the last value which is not greater than target, we only need to return right - 1.

### 162M. Find Peak Element
**Description:**\
A peak element is an element that is strictly greater than its neighbors.\
Given an integer array nums, find a peak element, and return its index. \
If the array contains multiple peaks, return the index to any of the peaks.\
You may imagine that nums\[-1\] = nums\[n\] = -∞.\
You must write an algorithm that runs in O(log n) time.\
**Method:**\
Compare nums\[mid\] to nums\[mid + 1\], move left to mid+1, if nums\[mid\] is small or equal to next one. Otherwise, move right to mid.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/162M.%20Find%20Peak%20Element.cpp)
```
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[mid]>nums[mid+1]){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/162M.%20Find%20Peak%20Element.py)
```
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = int(left + (right-left)/2)
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left
```

## 6.4 Use subfunction to determine the relation
This type of problem is tough. Because the comparing step (nums\[mid\] and target) is excuted by using a subfunction.


## 6.5 Others
In this type of problem, the value of target is not fixed.\
For example, [162M. Find Peak Element](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/162M.%20Find%20Peak%20Element.cpp).\
In this problem, we need to compare two adjacent values, i.e., nums\[mid\] and nums\[mid+1\]. Hence, right = nums.size()-1. If right = nums.size(), mid can be out of boundary. In addition, the condition of while loop must be left<right.

### 270. Closest Binary Search Tree Value
**Description:**\
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.\
Note:\
Given target value is a floating point. You are guaranteed to have only one unique value in the BST that is closest to the target.\
Example:\
Input: root = \[4,2,5,1,3\], target = 3.714286
```
    4
   / \
  2   5
 / \
1   3
```
Output: 4\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/270.%20Closest%20Binary%20Search%20Tree%20Value.cpp)
```
/*
Method 1: Traverse the tree, compare each node with the target, and keep the minimum difference
          In this method, we use preorder traversal method
*/
class Solution{
public:
    int closestValue(TreeNode *root, double target){
        double diff = numeric_limits<double>::max();
        int res = 0;
        stack<TreeNode*> st;
        st.push(root);
        while(st.size()!=0){
            TreeNode* cur = st.top();
            st.pop();
            if(diff>=abs(cur->val - target)){
                diff = abs(cur->val - target);
                res = cur->val;
            }
            if(cur->right){
                st.push(cur->right);
            }
            if(cur->left){
                st.push(cur->left);
            }
        }
        return res;
    }
}

/*
Method 2: Based on the property of the binary search tree, we can increse the runtime to O(log N).
          We compare cur->val with target. If target > cur->val, we go to right. Otherwise, we go left.
*/
class Solution{
public:
    int closestValue(TreeNode* root, double target){
        double diff = numeric_limits<double>::max();
        int res = 0;
        while(root){
            if(diff>=abs(target - root->val)){
                diff = abs(target - root->val);
                res = root->val;
            }
            root = target > root->val ? root->left : root->right;
        }
        return res;
    }
}

/*
Method 3: Iterative approach I
          1. Compare target with root->val, determine which direction we would go
          2. Call iterative function and obtain the cloest value from that side
          3. Determine which one (i.e., root or l) is closest to the target
*/
class Solution{
public:
    int closestValue(TreeNode* root, double target){
        int res = root->val;
        if(target>root->val && root->left){
            TreeNode* l = closestValue(root->left, target);
            res = abs(target - root->val)>=abs(target - l->val) ? l->val : root->val;
        }else if (target<root->val && root->right){
            TreeNode* r = closestValue(root->right, target);
            res = abs(target - root->val)>=abs(target - r->val) ? r->val : root->val;
        }
        return res;
    }
}

/*
Method 4: Iterative approach II
          1. Compare cur->val with target, and keep recording the minimum difference
          2. Check cur->left and cur->right;
*/
class Solution{
public:
    int closestValue(TreeNode* root, double target){
        double diff = numeric_limits<double>::max();
        int res = 0;
        helper(root, target, diff, res);
        return res;
    }
    void helper(TreeNode* root, double target, double& diff, int& res){
        if(root==NULL){return;}
        if(diff>=abs(target - root->val)){
            diff = abs(target - root->val);
            res = root->val;
        }
        helper(root->left, target, diff, res);
        helper(root->right, target, diff, res);
    }
}
```








