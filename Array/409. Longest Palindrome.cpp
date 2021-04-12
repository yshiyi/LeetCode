/*
409. Longest Palindrome
Hash Table, String

Description:
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2

Similar Question:
Palindrome Permutation - Easy
*/

// Solution:
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> ms;
        for(auto& c:s){
            ms[c]++;
        }
        int flag = 0, ans = 0;
        for(auto& key:ms){
            if(key.second%2==0){
                ans += key.second;
            }else{
                ans += key.second - 1;
                flag = 1;
                /*
                if(ans%2==0){
                  ans += 1;
                }
                */
            }
        }
        if(flag){
            return ans+1;
        }else{
            return ans;
        }
    }
};
