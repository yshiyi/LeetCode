/*
22M. Generate Parentheses
String, Backtracking

Description:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

Similar Questions:
Letter Combinations of a Phone Number - Medium
Valid Parentheses - Easy
*/

/*
Solution: backtrack
          1. setting up the base case, when the total length of the string is equal to 2*n
          2. if it is possible, insert "(" first.
          3. whenever the number of "(" is greater than ")", insert ")"
          Note: don't use if-else, in that case, we will only insert ")" when the number of "(" is equal to n.
*/
class Solution {
public:
    vector<string> res; 
    vector<string> generateParenthesis(int n) {
        backTrack(0, 0, n, "");
        return res;
    }
    void backTrack(int left, int right, int n, string S){
        if(S.size()==n*2){
            res.push_back(S);
            return;
        }
        if(left < n){
            backTrack(left+1, right, n, S+'(');
        }
        if(left > right){
            backTrack(left, right+1, n, S+')');
        }
    }
};
