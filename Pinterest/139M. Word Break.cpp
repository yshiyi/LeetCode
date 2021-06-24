/*
139M. Word Break
Hash Table, Dynamic Programming, Trie

Description:
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
 

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

Similar Question:
Word Break II - Hard
*/

/*
Method: We can formulate this problem as a 1D dp problem.
        Each value in dp[] represents if the current substring can be segmented as words in the dictionary.
        For example, 
          [l e e t c o d e]
        dp[1 0 0 0 1 0 0 0 1]
        Notive that the size of dp is greater then s.size() by 1.
        Because dp[i] checks the substring before i. Hence, dp[0] must be 1.
        We then use another iterator j to check from 0 to i-1.
        If dp[j] is true and the substring s.substr(j, i-j) is in the set(dictionary), then dp[i] = 1.
        It means the substring before i can be segmented as words in the dictionary.
*/
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<int> dp(s.size()+1, 0); dp[0] = 1;
        for(int i=0; i<=s.size(); ++i){
            for(int j=0; j<i; ++j){
                if(dp[j] && wordSet.count(s.substr(j, i-j))){
                    dp[i] = 1;
                }
            }
        }

        return dp.back();
    }
};
