/*
47M. Permutations II
Backtracking

Description:
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10

Similar Questions:
Next Permutation - Medium
Permutations - Medium
Palindrome Permutation II - Medium
Number of Squareful Arrays  - Hard
*/

/*
Method: Similar to 46M.Permutations
        However, since there exist duplicate elements, we must consider one more condition.
        We need to sort the nums first. 
        Then, if nums[i] is the same as nums[i-1], and check[i-1]==0, then we pass nums[i].
        Note: check[i-1] == 0 means nums[i-1] has been checked and returned back to 0.
              It doesn't mean that nums[i-1] hasn't been checked yet.
*/
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> temp;
        vector<int> check(nums.size(), 0);
        sort(nums.begin(), nums.end());
        backtrack(nums, check, temp);
        return res;
    }
    void backtrack(vector<int>& nums, vector<int>& check, vector<int>& temp){
        if(temp.size()==nums.size()){
            res.push_back(temp);
            return;
        }
        for(int i=0; i<nums.size(); i++){
            if(isValid(nums, check, i)){
                check[i] = 1;
                temp.push_back(nums[i]);
                backtrack(nums, check, temp);
                temp.pop_back();
                check[i] = 0;
            }
        }
    }
    bool isValid(vector<int>& nums, vector<int>& check, int i){
        if(check[i]==1){
            return false;
        }
        if(i>0 && nums[i]==nums[i-1] && check[i-1]==0){
            return false;
        }
        return true;
    }
};
