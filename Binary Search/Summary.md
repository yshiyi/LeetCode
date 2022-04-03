# Binary Search
<!-- GFM-TOC -->
* [Leetcode Binary Search](#Binary-Search)
    * [1. Introduction to Binary Search](#1-Introduction-to-Binary-Search)
       * [1.1 How to identify Binary Search](#11-How-to-identify-Binary-Search)
       * [1.2 3 Parts of a Successful Binary Search](#12-3-Parts-of-a-Successful-Binary-Search)
       * [704. Binary Search](#704-Binary-Search) 
    * [2. Template I Basic](#2-Template-I-Basic)
    * [3. Template II Access Neighbor](#3-Template-II-Access-Neighbor)
    * [4. Template III Access Both Neighbors](#4-Template-III-Access-Both-Neighbors)
    * [5. Binary Search Template Analysis](#5-Binary-Search-Template-Analysis)
    * [6. Summary](#6-Summary)
       * [6.1 Find the value equal to target](#61-Find-the-value-equal-to-target)
          * [33M. Search in Rotated Sorted Array](#33M-Search-in-Rotated-Sorted-Array)
          * [81M. Search in Rotated Sorted Array II](#81M-Search-in-Rotated-Sorted-Array-II)
          * [153M. Find Minimum in Rotated Sorted Array](#153M-Find-Minimum-in-Rotated-Sorted-Array)
          * [154H. Find Minimum in Rotated Sorted Array II](#154H-Find-Minimum-in-Rotated-Sorted-Array-II)
          * [278. First Bad Version](#278-First-Bad-Version)
          * [349. Intersection of Two Arrays](#349-Intersection-of-Two-Arrays)
          * [350. Intersection of Two Arrays II](#350-Intersection-of-Two-Arrays-II)
          * [35. Search Insert Position](#35-Search-Insert-Position)
          * [367. Valid Perfect Square](#367-Valid-Perfect-Square)
          * [374. Guess Number Higher or Lower](#374-Guess-Number-Higher-or-Lower)
          * [702M. Search in a Sorted Array of Unknown Size](#702M-Search-in-a-Sorted-Array-of-Unknown-Size)
          * [74M. Search a 2D Matrix](#74M-Search-a-2D-Matrix)
       * [6.2 Find the first value greater than or equal to target](#62-Find-the-first-value-greater-than-or-equal-to-target)
          * [34M. Find First and Last Position of Element in Sorted Array](#34M-Find-First-and-Last-Position-of-Element-in-Sorted-Array)
          * [35. Search Insert Position](#35-Search-Insert-Position)
       * [6.3 Find the first value greater than target](#63-Find-the-first-value-greater-than-target)
          * [270. Closest Binary Search Tree Value](#270-Closest-Binary-Search-Tree-Value)
          * [69. Sqrt(x)](#69-Sqrtx)
       * [6.4 Use subfunction to determine the relation](#64-Use-subfunction-to-determine-the-relation)
          * [287M. Find the Duplicate Number](#287M-Find-the-Duplicate-Number)
          * [378M. Kth Smallest Element in a Sorted Matrix](#378M-Kth-Smallest-Element-in-a-Sorted-Matrix)
          * [410H. Split Array Largest Sum](#410H-Split-Array-Largest-Sum)
          * [4H. Median of Two Sorted Arrays](#4H-Median-of-Two-Sorted-Arrays)
          * [658M. Find K Closest Elements](#658M-Find-K-Closest-Elements)
          * [719H. Find Kth Smallest Pair Distance](#719H-Find-Kth-Smallest-Pair-Distance)
       * [6.5 Others](#65-Others)
          * [162M. Find Peak Element](#162M-Find-Peak-Element)
          * [744. Find Smallest Letter Greater Than Target](#744-Find-Smallest-Letter-Greater-Than-Target)
          * [852. Peak Index in a Mountain Array](#852-Peak-Index-in-a-Mountain-Array)
          * [29M. Divide Two Integers](#29M-Divide-Two-Integers)
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

### 81M. Search in Rotated Sorted Array II
**Description:**\
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).\
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is \[nums\[k\], nums\[k+1\], ..., nums\[n-1\], nums\[0\], nums\[1\], ..., nums\[k-1\]\] (0-indexed). For example, \[0,1,2,4,4,4,5,6,6,7\] might be rotated at pivot index 5 and become \[4,5,6,6,7,0,1,2,4,4\].\
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.\
You must decrease the overall operation steps as much as possible.\
**Method:**\
Similar to 33M. Search in Rotated Sorted Array\
The only difference is there exist duplicates in this question.\
Hence, other than two conditions that we check in 33M, there is one more condition we need to check.\
It is when nums\[mid\]==nums\[right\]. In this case, we can simply move right to the left by 1, --right.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/81M.%20Search%20in%20Rotated%20Sorted%20Array%20II.cpp)
```
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return true;
            }
            if(nums[mid]<nums[right]){
                if(nums[mid]<target && target<=nums[right]){
                    left = mid + 1;
                }else{
                    right = mid - 1;
                }
            // We can't check nums[mid]>nums[left]
            }else if(nums[mid]>nums[right]){
                if(nums[left]<=target && target<nums[mid]){
                    right = mid - 1;
                }else{
                    left = mid + 1;
                }
            }else{
                --right;
            }
        }
        return false;
    }
};
```

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
        while left<right:
            mid = (left+right)//2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid
        return left
```

### 349. Intersection of Two Arrays
**Method:**\
As long as the question requires to search for a particular value, we should consider to use binary search.\
In this problem, we can sort nums2. For each value in nums1, we apply binary search to nums2.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/349.%20Intersection%20of%20Two%20Arrays.cpp)
```
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s;
        sort(nums2.begin(), nums2.end());
        for(auto& val:nums1){
            if(binarySearch(nums2, val)){
                s.insert(val);
            }
        }
        return vector<int> (s.begin(), s.end());
    }
    bool binarySearch(vector<int>& nums, int target){
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target){
                return true;
            }
            if(nums[mid]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }
};
```

### 350. Intersection of Two Arrays II
**Method:**\
This is a solution using binary search method.\
Different from 349. Intersection of Two Arrays, we need to record the appearances of the value as many times as it shows.\
To avoid to save duplicates, we have to remove the value that is saved to the result.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/350.%20Intersection%20of%20Two%20Arrays%20II.cpp)
```
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        sort(nums2.begin(), nums2.end());
        for(auto& val:nums1){
            int pos = binarySearch(nums2, val);
            if(pos!=-1){
                res.push_back(val);
                // vec.erase() takes a position iterator.
                nums2.erase(nums2.begin()+pos);
            }
        }
        return res;
    }
    int binarySearch(vector<int>& nums, int target){
        int left = 0, right = nums.size()-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]>target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return -1;
    }
};
```

### 35. Search Insert Position
**Description:**|
Given a sorted array of distinct integers and a target value, return the index if the target is found. \
If not, return the index where it would be if it were inserted in order.\
You must write an algorithm with O(log n) runtime complexity.\
**Method:**\
The standard template of binary search can return the position of the target, if the target exists. If the target doesn't exist, the template returns the first value that is greater than the target.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/35.%20Search%20Insert%20Position.cpp)
```
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]>target){
                right = mid;
            }else{
                left = mid+1;
            }
        }
        return left;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/35.%20Search%20Insert%20Position.py)
```
class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                right = mid
            else:
                left = mid + 1
        return left
```

### 367. Valid Perfect Square
**Description:**\
Given a positive integer num, write a function which returns True if num is a perfect square else False.\
Follow up: Do not use any built-in library function such as sqrt.\
**Method:**\
When the problem asks us to search for a particular value, we should consider to apply binary search.\
We can apply binary search to 1 - num.\
Both right=num and right=num/2 work. We compare mid^2 with num. If mid^2>num, we move left. Otherwise, we move right.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/367.%20Valid%20Perfect%20Square.cpp)
```
class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==1){
            return true;
        }
        int left = 1, right = num/2;
        while(left <= right){
            int mid = left + (right-left)/2;
            // Note: num/mid return an int, e.g., 5/2 -> 2. We need to convert the result to double.
            if((double)num/mid==mid){
                return true;
            }
            if(mid>num/mid){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return false;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/367.%20Valid%20Perfect%20Square.py)
```
class Solution(object):
    def isPerfectSquare(self, num):
        if num==1:
            return True
        left, right = 1, num//2
        while left <= right:
            mid = (right+left)//2
            if mid**2==num:
                return True
            if mid**2>num:
                right = mid-1
            else:
                left = mid+1
        return False
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

### 702M. Search in a Sorted Array of Unknown Size
**Description:**\
Given an integer array sorted in ascending order, write a function to search target in nums. \ 
If target exists, then return its index, otherwise return -1. \
However, the array size is unknown to you. \
You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).\
You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647. \
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/702M.%20Search%20in%20a%20Sorted%20Array%20of%20Unknown%20Size.cpp)
```
#include <iostream>
#include <vector>
using namespace std;
class ArrayReader{
private:
    vector<int> v;
public:
    ArrayReader(vector<int> &v){
        this->v = v;
    }
    int get(int i){

        return i < v.size() ? v[i]:2147483647;
    }
};
class Solution {
public:
    int search(ArrayReader& reader, int target) {
        int left = 0, right = INT_MAX;
        while (left < right) {
            int mid = left + (right - left) / 2;
            int x = reader.get(mid);
            if (x == target)
                return mid;
            if (x > target) {
                right = mid;
            }
            else
                left = mid + 1;
        }
//        if(right!=INT_MAX && reader.get(right)==target){
//            return right;
//        }
        return -1;
    }
};

int main(){
    Solution ob;
    vector<int> v = {-1,0,3,5,9,12};
    ArrayReader reader(v);
    cout<<(ob.search(reader, 12));
    return 0;
}
```

### 74M. Search a 2D Matrix
**Description:**\
Write an efficient algorithm that searches for a value in an m x n matrix. \
This matrix has the following properties:\
Integers in each row are sorted from left to right.\
The first integer of each row is greater than the last integer of the previous row.\
**Method:**\
Binary Search\
If a question ask us to search for a particular value, then the first choice of method is Binary Search.\
From the description of the question, we can see that the first value in each row is greater than the last one in the previous row.\
Hence, we can apply binary search on the first column and find the first the value that is greater than target.\
Then target must be in the previoud row.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/74M.%20Search%20a%202D%20Matrix.cpp)
```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(target<matrix[0][0]){
            return false;
        }
        // Apply Binary Search on the first column and determine the row that target lies in
        int left = 0, right = matrix.size();
        while(left<right){
            int mid = left + (right-left)/2;
            if(matrix[mid].front()==target){
                return true;
            }
            if(matrix[mid].front()<target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        int row = left - 1;

        // Search for target in the particular row
        int lr = 0, rr = matrix[row].size();
        while(lr < rr){
            int mid = lr + (rr-lr)/2;
            if(matrix[row][mid]==target){
                return true;
            }
            if(matrix[row][mid]<target){
                lr = mid + 1;
            }else{
                rr = mid;
            }
        }
        
        return false;
    }
};
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

### 34M. Find First and Last Position of Element in Sorted Array
**Description:**\
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return \[-1, -1\].\
You must write an algorithm with O(log n) runtime complexity.\
**Method:**\
To search for the range of the duplicated value, we need to determine the first and last position of that value.\
In other words, we need to run binary search twice.\
In the first run, we can determine the left bound of the range.\
If there exists the target value, we run another time of binary search to determine the right bound.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/34M.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.cpp)
```
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> res(2, -1);
        if(nums.size()==0){
            return res;
        }
        int left = 0, right = nums.size()-1;
        // First run, determine the left bound
        while(left<right){
            int mid = left + (right-left)/2;
            // Only when nums[mid]<target, we move to the right
            if(nums[mid]<target){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        // We need to check if nums[left] is equal to target
        if(nums[left]!=target){
            return res;
        }
        res[0] = left;
        right = nums.size()-1;
        // Second run, determine the right bound
        while(left<right){
            int mid = left + (right-left)/2;
            // If nums[mid]==target, we also move to the right.
            if(nums[mid]<=target){
                left = mid  + 1;
            }else{
                right = mid;
            }
        }
        // Finally, we need to check if nums[right] is equal to the target.
        if(nums[right]==target){
            res[1]=right;
        }else{
            res[1]=right-1;
        }

        return res;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/34M.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.py)
```
class Solution(object):
    def searchRange(self, nums, target):
        res = [-1, -1]
        if len(nums)==0:
            return res
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right+left)//2
            if nums[mid]<target:
                left = mid+1;
            else:
                right = mid
        if nums[left]!=target:
            return res
        res[0]=left
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid]<=target:
                left = mid + 1
            else:
                right = mid
        if nums[right]==target:
            res[1] = right
        else:
            res[1] = right - 1
        return res

```




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

### 69. Sqrt(x)
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


## 6.4 Use subfunction to determine the relation
This type of problem is tough. Because the comparing step (nums\[mid\] and target) is excuted by using a subfunction.\
First of all, we need to first determine the value of left and that of right. Normally, left is the smallest value and right is the largest one.\
mid = (right+left)/2 as usual, but we need a subfunction or a tricky method to determine the direction of movement.\

### 287M. Find the Duplicate Number
**Description:**\
Given an array of integers nums containing n + 1 integers where each integer is in the range \[1, n\] inclusive.\
There is only one repeated number in nums, return this repeated number.\
You must solve the problem without modifying the array nums and uses only constant extra space.\
**Method:**\
In this problem, mid is not the target the number. The number of values less than mid is the target number.\
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

### 378M. Kth Smallest Element in a Sorted Matrix
**Description:**\
Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.\
Note that it is the kth smallest element in the sorted order, not the kth distinct element.\
**Method:**\
This problem is similar to 287M. Find the Duplicate Number. mid is just a number, and we need to determine the number of values less than mid.\
At first, we need to determine the range of search. \
In this problem, left is the smallest value in the matrix which is the first one in the first row.\
Right is the largest value which is the last one in the last row.\
We use binary search to find the first value that is greater than or equal to k.\
The tricky part is to determine the number of values that are not greater than mid.\
We can first compare the last value in each row. If mid is greater than that, then count += n.\
Otherwise, we need to compare the first value in each row. If mid is greater, then we enter that row.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/378M.%20Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix.cpp)
```
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int left = matrix[0].front(), right = matrix.back().back();
        return binarySearch(matrix, left, right, k);
    }
    int binarySearch(vector<vector<int>>& matrix, int left, int right, int k){
        int n = matrix.size();
        while(left < right){
            int mid = left + (right-left)/2;
            int count = 0;
            // Calculate # of values less 
            for(int i=0; i<n; ++i){
                if(matrix[i].back()<=mid){
                    count += n;
                }else{
                    if(matrix[i].front()>mid){
                        break;
                    }else{
                        for(int j=0; j<n; ++j){
                            if(matrix[i][j]<=mid){
                                ++count;
                            }else{
                                break;
                            }
                        }
                    }
                }
            }
            
          if(count<k){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/378M.%20Kth%20Smallest%20Element%20in%20a%20Sorted%20Matrix.py)
```
class Solution(object):
    def kthSmallest(self, matrix, k):
        left, right = matrix[0][0], matrix[-1][-1]
        
        def search_less_equal(matrix, target):
            n = len(matrix)
            i, j, res = n-1, 0, 0
            while i>=0 and j<n:
                if matrix[i][j]<=target:
                    res += i + 1
                    j += 1
                else:
                    i -= 1
            return res
        
        while left < right:
            mid = (right+left)//2
            count = search_less_equal(matrix, mid)
            if count < k:
                left = mid+1
            else:
                right = mid
        return left
```

### 410H. Split Array Largest Sum
**Description:**\
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.\
Write an algorithm to minimize the largest sum among these m subarrays.\
**Method:**\
At first, we need to determine the value of left and that of right.\
The value of left should be the largest value in nums. Because that is the smallest sum of a subarray.\
The value of right should be the sum of nums, as it is the largest sum of a subarray.\
For mid=(right+left)/2, we need to check if it is a valid sum. In other words, if the sum of each single subarray is less than or equal to mid, we need to check if the total number of subarray is m.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/410H.%20Split%20Array%20Largest%20Sum.cpp)
```
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long left = 0, right = 0;
        // Determine the value of left and that of right
        for(int i=0; i<nums.size(); ++i){
            left = max(left, (long)nums[i]);
            right += nums[i];
        }
        while(left < right){
            long long mid = left + (right-left)/2;
            // Define a subfunction to determine if the array can be splitted into m subarrays
            if(can_split(nums, m, mid)){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
    
    bool can_split(vector<int>& nums, long m, long sum){
        long count = 1, curSum = 0;
        for(int i=0; i<nums.size(); ++i){
            // Add the current value to curSum
            curSum += nums[i];
            if(curSum > sum){
                // If curSum > sum, it means we have filled enough numbers into one subarray
                // The first number of the next subarray should be nums[i]
                curSum = nums[i];
                // Increase the number of subarray
                ++count;
                // Check if the total number of subarray is greater than m
                if(count > m){
                    return false;
                }
            }
        }
        return true;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/410H.%20Split%20Array%20Largest%20Sum.py)
```
class Solution(object):
    def splitArray(self, nums, m):
        left, right = 0, 0
        for num in nums:
            left = max(num, left)
            right += num
        
        def binarySearch(nums, targetSum, m):
            curSum, n = 0, 1
            for i in range(len(nums)):
                curSum += nums[i]
                if curSum > targetSum:
                    curSum = nums[i]
                    n += 1
                    if n > m:
                        return False
            return True
        
        while left < right:
            mid = (right + left)//2
            if binarySearch(nums, mid, m):
                right = mid
            else:
                left = mid + 1
        return left
```

### 4H. Median of Two Sorted Arrays
**Description:**
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).\
**Method:**\
The median value is the mean of (m+n+1)/2 and (m+n+2)/2. We can use binary search to find those two values in nums1 and nums2.\
To find Kth value in nums1 and nums2, we can search for the K/2th value in nums1 and nums2.\
If the K/2th in nums1 is greater than the K/2th in nums2, then we move left in nums2 by K/2.\
[C++](https://github.com/yshiyi/LeetCode/edit/main/Binary%20Search/4H.%20Median%20of%20Two%20Sorted%20Arrays.cpp)
```
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Get the length of nums1 and that of nums2
        int m = nums1.size(), n = nums2.size();
        // Target values 
        int left = (m+n+1)/2, right = (m+n+2)/2;
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right))/2.0;
    }
    // i and j are two pointers in nums1 and nums2, respectively
    int findKth(vector<int>& nums1, int i, vector<int>& nums2, int j, int k){
        // Corner cases, if i reaches the end of nums1, then kth value must be in nums2
        if(i>=nums1.size()){return nums2[j+k-1];}
        if(j>=nums2.size()){return nums1[i+k-1];}
        // If k==1, then return the minimum value of nums1[i] and nums[j]
        if(k==1){return min(nums1[i], nums2[j]);}
        // Find the k/2th value in nums1 and nums2. If it doesn't exist, then assign INT_MAX
        int midVal1 = (i+k/2-1 < nums1.size()) ? nums1[i+k/2-1] : INT_MAX;
        int midVal2 = (j+k/2-1 < nums2.size()) ? nums2[j+k/2-1] : INT_MAX;
        // Compare midVal1 and midVal2. Move the pointer in the one that has smaller midVal
        if(midVal1 < midVal2){
            return findKth(nums1, i+k/2, nums2, j, k-k/2);
        }else{
            return findKth(nums1, i, nums2, j+k/2, k-k/2);
        }
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/4H.%20Median%20of%20Two%20Sorted%20Arrays.py)
```
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        left, right = (m+n+1)//2, (m+n+2)//2
        
        def findKth(nums1, i, nums2, j, k):
            if i>=len(nums1):
                return nums2[j+k-1]
            if j>=len(nums2):
                return nums1[i+k-1]
            if k==1:
                return min(nums1[i], nums2[j])
            if (i+k//2-1)>=len(nums1):
                minVal1 = float('inf')
            else:
                minVal1 = nums1[i+k//2-1]
            if (j+k//2-1)>=len(nums2):
                minVal2 = float('inf')
            else:
                minVal2 = nums2[j+k//2-1]
            if minVal1 < minVal2:
                return findKth(nums1, i+k//2, nums2, j, k-k//2)
            else:
                return findKth(nums1, i, nums2, j+k//2, k-k//2)
            
        
        return (findKth(nums1, 0, nums2, 0, left) + findKth(nums1, 0, nums2, 0, right))/2.0
```


### 658M. Find K Closest Elements
**Description:**\
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. \
The result should also be sorted in ascending order.\
An integer a is closer to x than an integer b if:
```
|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
```
**Method:**\
Binary Search to find left bound\
Time complexity is O(log(N-k) + k). Take O(log(N-k)) to search for the left bound and O(k) to build the final answer.\
The basic idea is that we use binary search method to determine the position of the left bound.\
First of all, the biggest index the left bound could be is arr.size()-k. Suppose arr.size() = 5, k = 3\
0 1 2 3 4, the biggest index of the left bound is 2.\
Then, we consider arr\[mid\] and arr\[mid+k\]. Notice that only one of them could be in a final answer.\
If arr\[mid\] is closer than arr\[mid+k\], it means we don't need to consider all the values to the right of arr\[mid+k\] as well as arr\[mid+k\]. We should move the right pointer to avoid considering them.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/658M.%20Find%20K%20Closest%20Elements.cpp)
```
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size()-k;
        while(left < right){
            int mid = left + (right-left)/2;
            if(x-arr[mid]>arr[mid+k]-x){
                left = mid + 1;
            }else{
                /* 
                    Why don't we use right = mid - 1?
                    If we use right = mid - 1, the condition of while loop should be left<=right.
                    Hence, we will check the condition when left == right.
                    However, we are not supposed to check arr[right], because arr[right+k] is out of array.
                */
                right = mid;
            }
        }
        return vector<int>(arr.begin()+left, arr.begin()+left+k);
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/658M.%20Find%20K%20Closest%20Elements.py)
```
class Solution(object):
    def findClosestElements(self, arr, k, x):
        left, right = 0, len(arr)-k
        while left < right:
            mid = (left+right)//2
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left+k]
```

### 719H. Find Kth Smallest Pair Distance
**Description:**\
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums\[i\] and nums\[j\] where 0 <= i < j < nums.length.\
**Example:**\
Input: nums = \[1,3,1\], k = 1\
Output: 0\
Explanation: Here are all the pairs:\
(1,3) -> 2\
(1,1) -> 0\
(3,1) -> 2\
Then the 1st smallest distance pair is (1,1), and its distance is 0.\
**Method:**\
Binary Search.\
We don't search a particular value in nums. Instead, we search for the particular value of distance that satisfies the question requirement.\
We sort the vector first.\
The minimum distance is 0, and the maximum distance is the distance between the last and the first element.\
Then we will search for the answer within this range.\
mid = left+(right-left)/2 as usual. Then for this value of distance, we need to traverse nums and find out the number of distance that is less than or equal to mid.\
If the number is greater or equal to k, it means the value of mid is large, and we need to move right pointer. Otherwise, we move left pointer.\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/719H.%20Find%20K-th%20Smallest%20Pair%20Distance.cpp)
```
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0, right = nums.back()-nums[0];
        while(left<right){
            int mid = left + (right-left)/2;
            int count = 0, j = 0;
            
            /*
            In this method, we use two pointers technique.
            The second pointer keeps moving, if nums[j] - nums[i] <= mid.
            The tricky part is that for the next iteration of i, we don't need to reset j back to i+1.
            Because we have sorted the array, if nums[5] - nums[0] < mid, then nums[5] - nums[1] must be less than mid too.
            */
            for(int i=0; i<nums.size()-1; ++i){
                while(j<nums.size() && nums[j]-nums[i]<=mid){
                    ++j;
                }
                count += j - i - 1;
            }
            
            /*
            This method is little faster than the previous one.
            In this method, we use i to traverse nums.
            We keep moving i until nums[i] - nums[start] > mid.
            Then we count the difference between i and start, and move start forward by 1.
            */
            // int mid = left + (right - left) / 2, count = 0, start = 0;
            // for (int i = 0; i < nums.size(); ++i) {
            //     while (start < nums.size() && nums[i] - nums[start] > mid) ++start;
            //     count += i - start;
            // }
            
            if(count>=k){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/719H.%20Find%20K-th%20Smallest%20Pair%20Distance.py)
```
class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        left, right = 0, nums[-1]-nums[0]
        while left<right:
            mid = (right+left)//2
            count, j = 0, 1
            for i in range(len(nums)):
                while j<len(nums) and nums[j]-nums[i]<=mid:
                    j += 1
                count += j-i-1
            if count >=k:
                right = mid
            else:
                left = mid+1
        return left
```


## 6.5 Others
In this type of problem, the value of target is not fixed.\
For example, [162M. Find Peak Element](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/162M.%20Find%20Peak%20Element.cpp).\
In this problem, we need to compare two adjacent values, i.e., nums\[mid\] and nums\[mid+1\]. Hence, right = nums.size()-1. If right = nums.size(), mid can be out of boundary. In addition, the condition of while loop must be left<right.


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

### 744. Find Smallest Letter Greater Than Target
**Description:**\
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.\
Note that the letters wrap around. For example, if target == 'z' and letters == \['a', 'b'\], the answer is 'a'.\
**Method:**\
Similar to 162M. Find Peak Element.\
If target>=letters.back(), we can simply return letters\[0\].\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target.cpp)
```
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        if(letters.back()<=target){
            return letters[0];
        }
        int left = 0, right = letters.size()-1;  // In this problem, right=letters.size() also works.
        while(left < right){
            int mid = left + (right-left)/2;
            if(letters[mid]>target){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return letters[left];
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/744.%20Find%20Smallest%20Letter%20Greater%20Than%20Target.py)
```
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if letters[-1]<=target:
            return letters[0]
        left, right = 0, len(letters)
        while left < right:
            mid = (left+right)//2
            if letters[mid]<=target:
                left = mid + 1
            else:
                right = mid
        return letters[left]
```

### 852. Peak Index in a Mountain Array
**Description:**\
Let's call an array arr a mountain if the following properties hold:\
arr.length >= 3\
There exists some i with 0 < i < arr.length - 1 such that:\
arr\[0\] < arr\[1\] < ... arr\[i-1\] < arr\[i\]\
arr\[i\] > arr\[i+1\] > ... > arr\[arr.length - 1\]\
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr\[0\] < arr\[1\] < ... arr\[i - 1\] < arr\[i\] > arr\[i + 1\] > ... > arr\[arr.length - 1\].\
**Method:**\
Exact same as 162M. Find Peak Element\
[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/852.%20Peak%20Index%20in%20a%20Mountain%20Array.cpp)
```
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[mid]<=nums[mid+1]){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }
};
```
[Python](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/852.%20Peak%20Index%20in%20a%20Mountain%20Array.py)
```
class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = int(left + (right-left)/2)
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left
```

### 29M. Divide Two Integers
**Description:**\
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.\
Return the quotient after dividing dividend by divisor.\
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.\
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: \[−231, 231 − 1\]. For this problem, assume that your function returns 231 − 1 when the division result overflows.\
**Method:**\
Similar to 69. Sqrt(x)
The only tricky part is the negative bound of dividend or divisor is -2^31. The absolute value of which is out of bound of int. Therefore, we should use long instead of int. And the search range is from INT_MIN to INT_MAX.

[C++](https://github.com/yshiyi/LeetCode/blob/main/Binary%20Search/29M.%20Divide%20Two%20Integers.cpp)
```
class Solution {
public:
    int divide(int dividend, int divisor) {
        // This is a special case.
        if (dividend == INT_MIN && divisor == -1) return INT_MAX;
        long left = INT_MIN, right = INT_MAX;
        long num = dividend, den = divisor;
        while (left < right){
            long mid = left + (right-left)/2;
            if(mid == num/den){
                return mid;
            }
            if(mid>num/den){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
};
```


