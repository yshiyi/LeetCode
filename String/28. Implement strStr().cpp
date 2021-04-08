/*
28. Implement strStr()
Two Pointers, String

Description:
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Similar Questions:
Shortest Palindrome - Hard
Repeated Substring Pattern - Easy
*/

// Method 1: Sliding Window
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.size()==0){
            return 0;
        }else if(haystack.size()==0){
            return -1;
        }
        int right = 0, left = 0;
        unordered_map<char, int> m_needle;
        for(auto& c:needle){
            m_needle[c]++;
        }
        unordered_map<char, int> m_window; int match = 0;
        while(right < haystack.size()){
            char c = haystack[right];
            if(m_needle.find(c)!=m_needle.end()){
                m_window[c]++;
                if(m_window[c]==m_needle[c]){
                    match++;
                }
            }
            right++;
            while(match==m_needle.size()){
                char cl = haystack[left];
                if(m_window.find(cl)!=m_window.end()){
                    m_window[cl]--;
                    if(m_window[cl]<m_needle[cl]){
                        match--;
                    }
                }
                string str_window = haystack.substr(left, right-left);
                if(str_window == needle){
                    return left;
                }
                left++;
            }
            
        }
        return -1;
    }
};


// Method 2: string.find(substr) searches the string for the first occurrence of the sequence specified by its        arguments. 
class Solution {
public:
    int strStr(string haystack, string needle) {
        if(needle.empty()) return 0;
        return haystack.find(needle);
    }
};
