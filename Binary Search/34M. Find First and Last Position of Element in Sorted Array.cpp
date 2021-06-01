/*
34M. Find First and Last Position of Element in Sorted Array
Array, Binary Search

Description:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

Similar Questions:
First Bad Version - Easy
*/

/*
Method: To search for the range of the duplicated value, we need to determine the first and last position of that value.
        In other words, we need to run binary search twice.
        In the first run, we can determine the left bound of the range.
        If there exists the target value, we run another time of binary search to determine the right bound.
*/
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
