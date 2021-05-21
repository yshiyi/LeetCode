/*
78M. Subsets
Array, Backtracking, Bit Manipulation

Description:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

Similar Questions:
Subsets II - Medium
Generalized Abbreviation - Medium
Letter Case Permutation - Medium
*/

/*
Method 1: Backtracking
          Image that all possible subsets can construct a tree:
                                 []
                    /            |           \
                  [1]           [2]           [3]
                 /   \           |
            [1,2]     [1,3]   [2, 3]
              |
          [1, 2, 3]
          We just simply traverse this tree.
*/
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        backtrack(nums, 0, temp);
        return res;
    }
    void backtrack(vector<int>& nums, int start, vector<int>& temp){
        res.push_back(temp);
        for(int i=start; i<nums.size(); i++){
            temp.push_back(nums[i]);
            backtrack(nums, i+1, temp);
            temp.pop_back();
        }
    }
};


/*
Method 2: Iterative approach
          Let's try some examples.
          The subsets of [1] is [[], [1]].
          The subsets of [1, 2] is [[], [1], [2], [1, 2]].
          We can see that the subsets of [1, 2] is just the combination of subsets of [1] and each subset of [1] add 2.
*/
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> temp;
        res.push_back(temp);
        for(auto v:nums){
            int n = res.size();
            for(int i=0; i<n; i++){
                temp = res[i];
                temp.push_back(v);
                res.push_back(temp);
            }
        }
        return res;
    }
};


