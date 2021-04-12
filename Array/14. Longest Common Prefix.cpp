/*
14. Longest Common Prefix
String

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
*/

/* 
Solution: Use the characters in the first string as a reference, and compare each of them with other strings sequentially
*/
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0){
            return "";
        }
        string ans = "";
        for (int i=0; i< strs[0].size(); i++){
            for(int j=1; j<strs.size();j++){
                if(i==strs[j].size() || strs[0][i]!=strs[j][i]){
                    return ans;
                }
            }
            ans += strs[0][i];
        }
        return ans;
    }
};

