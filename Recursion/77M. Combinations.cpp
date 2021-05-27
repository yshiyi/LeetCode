/*
77M. Combinations
Backtracking

Description:
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
1 <= n <= 20
1 <= k <= n

Similar Questions:
Combination Sum - Medium
Permutations - Medium
*/

// Solution:
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        vector<int> ans;
        backtrack(ans, 1, n, k);
        return res;
    }
    void backtrack(vector<int>&ans, int start, int end, int k){
        if(ans.size()==k){
            res.push_back(ans);
            return;
        }
        for(int i=start; i<=end; i++){
            ans.push_back(i);
            backtrack(ans, i+1, end, k);
            ans.pop_back();
        }
    }
};

// Method 1:
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        vector<int> ans;
        backtrack(ans, 1, n, k);
        return res;
    }
    void backtrack(vector<int>&ans, int start, int end, int k){
        if(ans.size()==k){
            res.push_back(ans);
            return;
        }
        for(int i=start; i<=end; i++){
            ans.push_back(i);
            backtrack(ans, i+1, end, k);
            ans.pop_back();
        }
    }
};

// Method 2:
class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combine(int n, int k) {
        vector<int> ans;
        vector<int> check(n+1);
        backtrack(ans, check, 1, n, k);
        return res;
    }
    void backtrack(vector<int>&ans, vector<int>& check, int start, int end, int k){
        if(ans.size()==k){
            res.push_back(ans);
            return;
        }
        for(int i=start; i<=end; i++){
            if(check[i]==0){
                ans.push_back(i);
                check[i] = 1;
                backtrack(ans, check, i+1, end, k);
                ans.pop_back();
                check[i] = 0;
            }
        }
    }
};
