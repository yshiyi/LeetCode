/*
90M. Subsets II
Array, Backtracking

Description:
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10

Similar Questions:
Subsets - Mediuim
*/


/*
Solution: Similar to 47M. Permutations II
          Sort the array first so as to put duplicates together.
          Since there are duplicated values in the array, we need a vector "check" to check if the value has been added. 
*/
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> temp;
        vector<int> check(nums.size(), 0);
        sort(nums.begin(), nums.end());
        subsets(nums, temp, check, 0);
        return res;
    }
    void subsets(vector<int>& nums, vector<int>& temp, vector<int>& check, int start){
        res.push_back(temp);
        for(int i=start; i<nums.size(); ++i){
            if(isValid(nums, check, i)){
                temp.push_back(nums[i]);
                check[i] = 1;
                subsets(nums, temp, check, i+1);
                check[i] = 0;
                temp.pop_back();
            }
        }
    }
    bool isValid(vector<int>& nums, vector<int>& check, int& i){
        if(check[i]==1){
            return false;
        }
        if(i>0 && nums[i]==nums[i-1] && check[i-1]==0){
            return false;
        }
        return true;
    }
};
