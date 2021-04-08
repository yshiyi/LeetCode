/*
209. Minimum Size Subarray Sum
Two Pointers, Binary Search

Description:
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Similar Questions:
Minimum Window Substring - Hard
Maximum Size Subarray Sum Equals k - Medium
Maximum Length of Repeated Subarray - Medium
Minimum Operations to Reduce X to Zero - Medium
*/

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
