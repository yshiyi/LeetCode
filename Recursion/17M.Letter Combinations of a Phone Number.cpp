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
Method 1: Recursive approach - backtracking
          The input digits are between 2 and 9. 
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
        map<char, string> m ={{'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, 
                              {'8', "tuv"}, {'9', "wxyz"}};
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


/*
Method 2: Iterative approach
          Imagine each digit is a node in a tree. 
          Each letter contained in the first digit connects to each letter contained in the second digit.
          e.g., 
                    a          b          c
                 /  |  \    /  |  \    /  |  \
                d   e   f  d   e   f  d   e   f
          To find out all possible combinations is like to using breadth-first search to traverse the tree.
          Hence, we need to use queue to store all combinations.
          For each string currently stored in the queue, we connect it to all possible children.
          And save the new combinations back to the queue.
*/
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if(digits.size()==0){
            return res;
        }
        map<char, string> m ={{'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, 
                              {'8', "tuv"}, {'9', "wxyz"}};
        
        string temp;
        queue<string> q;
        string letters = m[digits[0]];
        // Initially, we save all the letters contained in the first digit to the queue.
        for(int i=0; i<letters.size(); i++){
            // Note: the queue is supposed to store strings.
            //       to save char, we need string(1, char) to convert a char to string.
            q.push(string(1, letters[i]));
        }
        
        // We then loop through all the rest of digits.
        for(int i=1; i<digits.size(); i++){
            letters = m[digits[i]];
            // Obtain the current size of the queue
            int count = q.size();
            // We can't use q.size() as a condition, because we keep inserting new string to the queue.
            while(count){
                temp = q.front(); q.pop();
                // Take out the first string and add it to all possible letters contained in the next digit.
                for(int j=0; j<letters.size(); j++){
                    temp += letters[j];
                    q.push(temp);
                    temp.pop_back();
                }
                --count;
            } 
        }
        
        while(q.size()){
            res.push_back(q.front());
            q.pop();
        }
        return res;
    }
};
