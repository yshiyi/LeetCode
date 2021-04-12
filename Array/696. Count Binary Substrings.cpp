/*
696. Count Binary Substrings
String

Description:
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Similar Question:
Encode and Decode Strings - Medium
*/

/* 
Soultion:
Hint: How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?
*/
class Solution {
public:
    int countBinarySubstrings(string s) {
        vector<int> v;
        int i = 0, c = 0;
        while(i<s.size()){
            while(i<s.size() && s[i]=='0'){
                c++;
                i++;
            }
            if(c!=0){
                v.push_back(c);
                c = 0;
            }
            while(i<s.size() && s[i]=='1'){
                c++;
                i++;
            }
            if(c!=0){
                v.push_back(c);
                c = 0;
            }
        }
        int ans = 0;
        for(int j=0; j<v.size()-1; j++){
            ans += min(v[j], v[j+1]);
        }
        return ans;
    }
};
