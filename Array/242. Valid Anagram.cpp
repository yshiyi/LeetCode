/*
242. Valid Anagram
Hash Table, Sort, String

Desciption:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Similar Questions:
Group Anagrams - Medium
Palindrome Permutation - Easy
Find All Anagrams in a String - Medium
*/

// Solution:
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> ms;
        for(auto& c:s){
            ms[c]++;
        }
        for(auto& c:t){
            if(ms.find(c)==ms.end()){
                return false;
            }else{
                ms[c]--;
            }
        }
        for(auto& key:ms){
            if(key.second!=0){
                return false;
            }
        }
        return true;
    }
};
