

/*
410H. Split Array Largest Sum
Binary Search, Dynamic Programming

Description:;
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], m = 2
Output: 9

Example 3:
Input: nums = [1,4,4], m = 3
Output: 4

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
*/

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long left = 0, right = 0;
        for(int i=0; i<nums.size(); ++i){
            left = max(left, (long)nums[i]);
            right += nums[i];
        }
        while(left < right){
            long long mid = left + (right-left)/2;
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
            curSum += nums[i];
            if(curSum > sum){
                curSum = nums[i];
                ++count;
                if(count > m){
                    return false;
                }
            }
        }
        return true;
    }
};
