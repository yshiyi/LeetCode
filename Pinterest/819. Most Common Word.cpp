/*
819. Most Common Word

Description:
Given a string paragraph and a string array of the banned words banned, 
return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.


Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
*/

/*
Method: The basic idea is to convert all characters in the paragraph to lower letters.
        1. Using isalpha() to check each character. 
           If it is an alphabetic letter, then use tolower() to convert it to lower letter.
        2. If it is not, then replace it with a space " ".
        Finally, create a hashmap to save each word in the paragraph and to count the number of appearances.
        Keep tracking the maximum number of appearances and the corresponding word.
*/

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        // Save all banned words to a set
        set<string> s;
        for(auto word:banned){
            s.insert(word);
        }
        string new_paragraph = "";
        for(auto letter:paragraph){
            if(isalpha(letter)){
                new_paragraph += tolower(letter);
            }else{
                new_paragraph += " ";
            }
        }
        
        istringstream iss(new_paragraph);
        string str;
        map<string, int> m;
        int max_len = 0;
        string res;
        while(iss >> str){
            if(!s.count(str)){
            // if(s.find(str)==s.end()){
                ++m[str];
                if(m[str]>max_len){
                    max_len = m[str];
                    res = str;
                }
            }
        }
        return res;
    }
};
