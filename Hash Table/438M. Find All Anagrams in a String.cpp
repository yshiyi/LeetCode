/*
438M. Find All Anagrams in a String
Hash Table, Sliding Window

Description:
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and 
the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Similar Questions:
Valid Anagram - Easy
Permutation in String - Medium
*/


/* Solution:
   Method: Sliding Window
           Similar to 567M. Permutation in String
           In this case, we need to record the value of left when we find the target string.
*/
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        unordered_map<char, int> window, need;
        int left = 0, right = 0, match = 0;
        int target_len = p.size();
        vector<int> res;
        for (auto& c:p){
            need[c]++;
        }
        while (right < s.size()){
            char c = s[right];
            if (need.find(c)!=need.end()){
                window[c]++;
                if(window[c]==need[c]){
                    match++;
                }
            }
            right++;
            while (match==need.size()){
                char d = s[left];
                if (need.find(d)!=need.end()){
                    if(window[d]==need[d]){
                        match--;
                    }
                    window[d]--;
                }
                if (right - left == target_len){
                    res.push_back(left);
                }
                left++;
            }
        }
        return res;
    }
};
