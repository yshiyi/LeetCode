"""
227. Basic Calculator II

Description:
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
 

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

"""
Method: Stack
        We need a stack to save the result of each part of operation. 
        At the end of code, we only need to return the sum of all the values stored in the stack.
        We also need record the operator to save the previous operator.
        For example:
        -4/2+
        When we reach "-", we put the previous result into the stack and update op as "-".
        When we reach "/", we check op. Since op == "-", we push -4 into the stack and update op as "/".
        When we reach "+", we check op. Since op == "/", we push -4/2 into the stack and udpate op as "+".
        
        Note:
        In python, -3/2 = -2.
        Therefore, we need to convert -3 to float first.
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = collections.deque()
        num = 0
        op = "+"
        s += op
        for c in s:
            if c == " ":
                continue
            elif c.isnumeric():
                num = int(c) + num*10
            else:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop()*num)
                elif op == "/":
                    stack.append(int(float(stack.pop())/num))
                num, op = 0, c

        return sum(stack)
