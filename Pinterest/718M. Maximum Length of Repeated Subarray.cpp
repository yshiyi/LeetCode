/*
718M. Maximum Length of Repeated Subarray
Dynamic Programming

Description:
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
 

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100

Similar Question:
Minimum Size Subarray Sum - Medium
*/

/*
Method: This is a DP 2D problem.
        Build a 2D DP matrix. For example, nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
           3 2 1 4 7
        1  0 0 1 0 0
        2  0 1 0 0 0
        3  1 0 0 0 0
        2  0 2 0 0 0
        1  0 0 3 0 0
        We can notice when there are two same values, 
        the dp[][] value is equal to 1 plus the value at its top left corner.
*/
class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        int row = nums1.size(), col = nums2.size();
        vector<vector<int>> dp(row, vector<int>(col, 0));
        
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(nums1[i]==nums2[j]){
                    ++dp[i][j];
                    if(i>=1 && j>=1){
                        dp[i][j] += dp[i-1][j-1];
                    }
                }
            }
        }
        
        int res = 0;
        for(int i=0; i<row; i++){
            res = max(res, *max_element(dp[i].begin(), dp[i].end()));
        }
        return res;
    }
};
