/*
269H. Alien Dictionary
Decription:
There is a new alien language that uses the English alphabet. 
However, the order among letters are unknown to you.
You are given a list of strings words from the dictionary, 
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language, and return it. 
If the given input is invalid, return "". If there are multiple valid solutions, return any of them.
 
Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:
Input: words = ["z","x"]
Output: "zx"
Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
Similar Question:
Course Schedule II - Medium
*/

/*
Method: Similar to 210M. Course Schedule II
        In this question, we need to create two maps instead of vectors to save data.
        Keep in mind, we need to first add the first letter in the first word into the map2.
*/
#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

class Solution{
public:
    string alienDictionary(vector<string> &words){
        // Creat a map, key is the parent letter, values are the children letters
        map<char, vector<char>> m1;
        // Creat another map, key is the letter, value is the number of parents of that letter
        map<char, int> m2;
        // Add the first letter in the first word into m2 first
        m2[words[0][0]] = 0;

        string res = "";
        // Traverse words and find the relation between each letter
        for(int i=0; i<words.size()-1; ++i){
            int mn = min(words[i].size(), words[i+1].size());
            for(int j=0; j<mn; ++j){
                if(words[i][j] != words[i+1][j]){
                    m1[words[i][j]].push_back(words[i+1][j]);
                    ++m2[words[i+1][j]];
                    break;
                }
            }
        }


        // Create a queue to traverse all the letters in the map
        queue<char> q;
        for(auto letter:m2){
            if(letter.second==0){
                q.push(letter.first);
            }
        }

        while(!q.empty()){
            char c = q.front(); q.pop();
            res += c;
            for(auto letter:m1[c]){
                --m2[letter];
                if(m2[letter]==0){
                    q.push(letter);
                }
            }
        }

        for(auto letter:m2){
            if(letter.second!=0){
                return {};
            }
        }
        return res;
    }
};

int main(){
    Solution* obj = new Solution();
    vector<string> words1 = {"wrt", "wrf", "er", "ett", "rftt"};
    vector<string> words2 = {"z", "x", "z"};
    vector<string> words3 = {"z", "x"};

    string res1 = obj->alienDictionary(words1);
    string res2 = obj->alienDictionary(words2);
    cout << res1 << "#" << endl;
    cout << res2 << "#" << endl;
    cout << obj->alienDictionary(words3) << "#" << endl;

}
