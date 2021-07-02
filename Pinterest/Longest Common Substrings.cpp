/*
Longest Common Substring | DP-29
Difficulty Level : Medium

Description:
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

Example 1:
Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
Output : 5
Explanation:
The longest common substring is “Geeks” and is of length 5.

Example 2:
Input : X = “abcdxyz”, y = “xyzabcd”
Output : 4
Explanation:
The longest common substring is “abcd” and is of length 4.

Example 3:
Input : X = “zxabcdezy”, y = “yzabcdezx”
Output : 6
Explanation:
The longest common substring is “abcdez” and is of length 6.
*/

/*
Method: This is a typical 2D dp problem.
        We need to create a 2D matrix. 
        The size of row and that of column are the size of str1 and that of str2, respectively.
          a b c d x y z
        a 1 0 0 0 0 0 0
        b 0 2 0 0 0 0 0
        c 0 0 3 0 0 0 0
        d 0 0 0 4 0 0 0
        x 0 0 0 0 1 0 0
        y 0 0 0 0 0 2 0
        z 0 0 0 0 0 0 3
        It is easily seen that if str1[i]==str2[j], then dp[i][j] = dp[i-1][j-1] + 1.
        At the end, we return the maximum value in dp.
        
        Time Complexity: O(mn), where m and n are the size of string1 and that of string2, respectively. 
        Space Space: O(mn)
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:
    int LCSubstrs(string str1, string str2){
        int n = str1.size(), m = str2.size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                if(i==0 && j==0 && str1[j]==str2[i]) {
                    dp[i][j] = 1;
                }else if(str1[j]==str2[i]){
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
            }
        }
        int res = 0;
        for(int i=0; i<m; ++i){
            res = max(res, *max_element(dp[i].begin(), dp[i].end()));
        }
        return res;
    }
};

int main(){
    string X = "OldSite:GeeksforGeeks.org";
    string Y = "NewSite:GeeksQuiz.com";

    Solution *obj = new Solution();
    cout << obj->LCSubstrs(X, Y) << endl;

}


