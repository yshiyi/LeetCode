/*
557. Reverse Words in a String III
String

Description:
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Similar Question:
Reverse String II - Easy
*/

// Method: using replace(start, # of char, newString)
class Solution {
public:
    string reverseWords(string s) {
        if(s.size()==1){
            return s;
        }
        int start = 0;
        for(int i=0; i<s.size()+1; i++){
            if(isspace(s[i])){
                s.replace(start, i-start, reverseString(s.substr(start, i-start)));
                start = i+1;
            }
            if(i==s.size()){
                s.replace(start, i-start, reverseString(s.substr(start, i-start)));
            }
        }
        return s;
    }
    string reverseString(string substr){
        int left = 0, right = substr.size()-1;
        while(left < right){
            swap(substr[left], substr[right]);
            left++; right--;
        }
        return substr;
    }
};
