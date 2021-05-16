/*
17M.Letter Combinations of a Phone Number
String, Backtracking, Depth-first Search, Recursion

Description:
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

Similar Questions:
Generate Parentheses - Medium
Combination Sum - Medium
Binary Watch - Easy
*/

/*
Solution: The input digits are between 2 and 9. 
          We need to first create a map to hold the digits and the corresponding letters.
          Define a variable, "count", to go through the input string.
          For each digit, we determine the corresponding letters using the map.
          Then using backtracking method to find out all possible combinations.
*/
class Solution {
public:
    vector<string> res;
    vector<string> letterCombinations(string digits) {
        if(digits.size()==0){
            return res;
        }
        map<char, string> m ={{'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};
        string temp;
        backtrack(digits, m, temp, 0);
        return res;
    }
    void backtrack(string& digits, map<char, string>& m, string& temp, int count){
        if(count==digits.size()){
            res.push_back(temp);
            return;
        }
        string str = m[digits[count]];
        for(int i=0; i<str.size(); i++){
            temp = temp + str[i];
            backtrack(digits, m, temp, count+1);
            temp.pop_back();
        }
    }
};
