/*
151M. Reverse Words in a String.py
String

Description:
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Example 4:
Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"

Example 5:
Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"

Similar Question:
Reverse Words in a String II - Medium
*/

/* Method: there are two scenarios that need to be considered:
           1. if s[i] is not a space, then we save it to a string, word;
           2. if s[i] is a space, then we need to check the size of word.
              if word.size() is not 0, it means we have save a complete word and we save it to a vector.
*/
class Solution {
public:
    string reverseWords(string s) {
        vector<string> v;
        int right=0;
        string word="";
        while(right<s.size()){
            if(!isspace(s[right])){
                word += s[right];
                if(right==s.size()-1){
                    v.push_back(word);
                }
            }else{
                if(word.size()!=0){
                    v.push_back(word);
                    word = "";
                }
            }
            right++;
        }

        string ans;
        for(int i=v.size()-1;i>-1;i--){
            ans += v[i] +" ";
        }
        ans.pop_back();
        return ans;
    }
};
