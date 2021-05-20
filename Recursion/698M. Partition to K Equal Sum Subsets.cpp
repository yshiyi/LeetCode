/*
698M. Partition to K Equal Sum Subsets
Dynamic Programming, Recursion, Backtracking

Description:
Given an integer array nums and an integer k, 
return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].

Similar Question:
Partition Equal Subset Sum - Medium
*/

/*
Method 1: Backtracking
          There are two different backtracking approaches for this questions.
          In this method, we define k buckests and iterate through the values in nums.
          To improve the computational efficiency, we sort nums in descending order first.
*/
class Solution {
public:
    // Declare this static predicate to sort nums in descending order
    static bool myCompare(int num1, int num2){
        return num1 > num2;
    }
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = 0;
        for(auto v:nums){
            sum += v;
        }
        // Check the reminder of sum/k, if it is non-zero, we can't divide nums into k subsets 
        if(sum%k!=0){
            return false;
        }
        int target = sum/k;
        // Create k subsets
        vector<int> bucket(k, 0);
        sort(nums.begin(), nums.end(), myCompare);
        return backtrack(nums, 0, bucket, target);
    }
    bool backtrack(vector<int>& nums, int index, vector<int>& bucket, int target){
        // When we reach to the end of nums, we need to check if the sum of each subset is equal to target
        if(index == nums.size()){
            for(int i=0; i<bucket.size();i++){
                if(bucket[i]!=target){
                    return false;
                }
            }
            return true;
        }
        // Iterate through all subsets
        for(int i=0; i<bucket.size(); i++){
            // If the sum of the subset is less than target, we can add this number to buckest[i]
            if(bucket[i]+nums[index]<=target){
                bucket[i] += nums[index];
                if(backtrack(nums, index+1, bucket, target)){
                    return true;
                }
                bucket[i] -= nums[index];
            }
        }
        return false;
    }
};

/*
Method 2:
*/
