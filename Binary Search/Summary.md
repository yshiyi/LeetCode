# Binary Search
<!-- GFM-TOC -->
* [Leetcode Binary Search](#Binary-Search)
    * [1. Introduction to Binary Search](#1-Introduction-to-Binary-Search)
       * [1.1 How to identify Binary Search](#11-How-to-identify-Binary-Search)
       * [1.2 3 Parts of a Successful Binary Search](#12-3-Parts-of-a-Successful-Binary-Search)
       * [704. Binary Search](#704-Binary-Search) 
    * [2. Template I Basic](#2-Template-I-Basic)
       * [69. Sqrt(x)](#69-Sqrtx)
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
[Python]()
