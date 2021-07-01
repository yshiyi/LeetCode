/*
224H. Basic Calculator

Description:
Given a string s representing a valid expression, implement a basic calculator to evaluate it, 
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, 
such as eval().


Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Example 4:
Input: s = "+48 + -48"
Output: 0
Explanation: Numbers can have multiple digits and start with +/-.

Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
Every number and running calculation will fit in a signed 32-bit integer.

Similar Questions:
Evaluate Reverse Polish Notation - Medium
Basic Calculator II - Medium
Different Ways to Add Parentheses - Medium
Expression Add Operators - Hard
Basic Calculator III - Hard
*/

/*
Method: Stack.
        We process the equation from the left to right.
        1. Define a num to record the value of an input number.
        2. Define a sign to track the operation sign before each number
        3. Define a res to record the calculation result at the current position in the equation.
        3. When we encounter a left parenthesis, we push the value of res into the stack first.
           And push the sign which is right before '(' into the stack next.
           Reset res = 0 and keep calculating the operation inside the parenthesis.
        4. When we encounter a right parenthesis, note that the current value of res is the operation result
           within the parenthesis.
           Hence, we multiply res with the st.top() which is the sign before the left parenthesis,
           and add the next st.top() which is res (the operation result before the parenthesis).
        
        Time complexity: O(N), where N is s.size()
        Space complexity: O(N), which is mostly consumed by the stack.
*/
class Solution {
public:
    int calculate(string s) {
        int res = 0, sign = 1, n = s.size();
        stack<int> st;
        for(int i=0; i<n; ++i){
            char c = s[i];
            if(c>='0'){
                int num = 0;
                while(i<n && s[i]>='0'){
                    num = num*10 + (s[i]-'0');
                    ++i;
                }
                res += num * sign;
                --i;
            }else if(c=='+'){
                sign = 1;
            }else if(c=='-'){
                sign = -1;
            }else if(c=='('){
                st.push(res);
                st.push(sign);
                res = 0;
                sign = 1;
            }else if(c==')'){
                res *= st.top(); st.pop();
                res += st.top(); st.pop();
                sign = 1;
            }
        }
        return res;
    }
};
