/*
344. Reverse String
Two Pointers, String

Description:
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.
*/

// This is a solution using recursive approach.
class Solution {
public:
    void reverseString(vector<char>& s) {
        helper(s, 0, s.size()-1);
        return;
    }
    void helper(vector<char>& str, int left, int right){
        if(left>right){
            return;
        }
        swap(str[left], str[right]);
        helper(str, ++left, --right);
    }
};
