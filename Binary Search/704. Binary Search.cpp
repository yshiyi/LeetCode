/*
704. Binary Search
Binary Search

Description:
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
1 <= nums.length <= 104
-9999 <= nums[i], target <= 9999
All the integers in nums are unique.
nums is sorted in an ascending order.

Similar Questions:
Search in a Sorted Array of Unknown Size - Medium
*/

// Template I
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

// Template II
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        while(left < right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]>target){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        if(nums[left]==target){
            return left;
        }else{
            return -1;
        }
    }
};

// Template III
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        while(left+1< right){
            int mid = left + (right-left)/2;
            if(nums[mid]==target){
                return mid;
            }
            if(nums[mid]>target){
                right = mid;
            }else{
                left = mid;
            }
        }
        if(nums[left]==target){
            return left;
        }else if(nums[right]==target){
            return right;
        }else{
            return -1;
        }
    }
};
