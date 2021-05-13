/*
46M. Permutations
Backtracking

Description:
Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

Similar Questions:
Next Permutation - Medium
Permutations II - Medium
Permutation Sequence - Hard
Combinations - Medium
*/

/*
Method: This is similar to 77M.Combinations. 
        The difference is this question allows the duplicate answers, e.g., [1, 2], [2, 1].
        We can create a vector check which has the same size as nums.
        For each elements in nums, the corresponding position in check has two values: 
            0 - hasn't been added to the temp
            1 - has been added to the temp
*/

class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> temp;
        vector<int> check(nums.size(), 0);
        backtrack(nums, check, temp);
        return res;
    }
    void backtrack(vector<int>& nums, vector<int>& check, vector<int>& temp){
        if(temp.size()==nums.size()){
            res.push_back(temp);
            return;
        }
        for(int i=0; i<nums.size(); i++){
            if(check[i]==0){
                check[i] = 1;
                temp.push_back(nums[i]);
                backtrack(nums, check, temp);
                temp.pop_back();
                check[i] = 0;
            }
        }
    }
};
