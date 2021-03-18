/*
76H. Minimum Window Substring
Hash Table, Two Pointers, String, Sliding Window

Description:
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, 
it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Similar Questions:
Substring with Concatenation of All Words - Hard
Minimum Size Subarray Sum - Medium
Sliding Window Maximum - Hard
Permutation in String - Medium
Smallest Range Covering Elements from K Lists - Hard
Minimum Window Subsequence - Hard
*/


/* Solution:
   Method: Using sliding window.
           1. Create two unordered_map: need and window. 
              need contains the target string and the number of each characters.
              window contains the target characters and the corresponding number of appearances in the window.
              Note: use [key]++. In doing so, the map automatically assigns 0 to key, if key doesn't exist.
           2. Define some necessary variables
              two pointers: left and right
              number of matching characters: match
              starting position of the shortest substring: start
              length of the shortest substring: len
           3. Move the pointer right first until the window contains all the target characters
              Check if char c is in need, if so, window[c]++.
              When the number of c in window is equal to that in need, we increase match by 1.
           4. When match == need.size(), i.e., current window contains all target characters.
              We start to move the point left
              If char d is in need and if window[d]==need[d], then reduce match by 1.
              Otherwise, just reduce window[d] by 1;
           5. Finally, check the value of len.
              If it doesn't change, it means there is no such short string and return "".
              Otherwise, return s.substr(start, len+1).
              Note: the length of the shorstest substring is len+1. 
                    Because the pointer right points to the position of the last character.
*/
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> window, need;
        for (auto& c:t) {
            need[c]++;
        }

        int left = 0, right = 0, match = 0;
        int start = 0, len = INT_MAX;
        while(right < s.size()) {
            char c = s[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                // if (window[c]==1){ This doesn't work, if there are duplicate char in target string.
                if (window[c]==need[c]){
                    match++;
                }
            }
            while (match == need.size()) {
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                char d = s[left];
                if (need.find(d)!=need.end()){
                    if (window[d]==need[d]){
                        match--;
                    }
                    window[d]--;
                }                
                left++;
            }
            right++;
        }
        
        if (len!=INT_MAX){
            string res = s.substr(start, len+1);
            return res;
        }else{
            return "";
        }
        
    }
};
