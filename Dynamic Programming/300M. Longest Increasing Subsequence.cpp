/*
300M. Longest Increasing Subsequence

Description:
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or 
no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

Similar Questions:
Increasing Triplet Subsequence - Medium
Russian Doll Envelopes - Hard
Maximum Length of Pair Chain - Medium
Number of Longest Increasing Subsequence - Medium
Minimum ASCII Delete Sum for Two Strings - Medium
Minimum Number of Removals to Make Mountain Array - Hard
*/

/*
Method: Dynamic Programming
        This is a DP 1D problem. The value saved in dp[] is the maximum length of subsequence until the current value.
        For example, [10,9,2,5,3,7,101,18]
        for dp[6](nums[6]=7), the maximum length of subsequence is 2 ([2, 5], [2, 3]) which is saved at dp[3] and dp[4]
        hence dp[6] = 2 + 1.
        The procedure is to compare nums[i] (i=0,...,n-1) to nums[n].
        For those nums[i] < nums[n], we find the maximum among those dp[i].
        Add max(dp[i]) by 1, and save it to dp[n].
        Finally, we return the *max_element(dp.begin(), dp.end()).
*/
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        for(int i=1; i<nums.size(); ++i){
            int max_len = 0;
            for(int j=0; j<i; j++){
                if(nums[j]<nums[i]){
                    max_len = max(dp[j], max_len);
                }  
            }
            dp[i] = max_len + 1;
        }

        return *max_element(dp.begin(), dp.end());
    }
};
