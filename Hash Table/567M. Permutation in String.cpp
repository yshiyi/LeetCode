/*
567M. Permutation in String
Two pointers, Sliding window

Description:
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Similar Question:
Minimum Window Substring - Hard
Find All Anagrams in a String - Medium
*/

/* Solution:
   Method: Sliding window.
           Similar to 76H.Minimum Window Substring.
           Only differece is we need to check the length of the substring which contains the target characters.
           If the length is equal to that of the target string, then return true.
*/
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> window, need;
        int left = 0, right = 0, match = 0;
        int len = s1.size(), window_size = 0;
        for (auto& c:s1) {
            need[c]++;
        }
        while (right < s2.size()){
            char c = s2[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                if (window[c]==need[c]){
                    match++;
                }
            }
            right++;
            
            while (match==need.size()){
                char d = s2[left];
                if(need.find(d)!=need.end()){
                    if(window[d]==need[d]) {
                        match--;
                    }
                    window[d]--;
                }
                window_size = right - left;
                if (window_size==len){
                    return true;
                }
                left++;
            }
        }
        return false;
    }
};
