"""
921. Minimum Add to Make Parentheses Valid

Description:
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
 

Example 1:
Input: s = "())"
Output: 1

Example 2:
Input: s = "((("
Output: 3
 

Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.
"""

"""
Method: We need to record the number of moves for both left and right parenthese.
        Specifically, if we see a left bracket, the needs for the right bracket should increase by 1.
        When we see a right bracket, we reduce the needs for the right brackest by 1.
        The tricky part is how to deal witht the needs for the left bracket.
        When the needs for the right bracket is equal to -1, it means there is a redundant right bracket.
        In other words, we need an extra left bracket. Increase left by 1, and set right back to 0.
        
"""
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i]=="(":
                right += 1
            if s[i]==")":
                right -= 1
                if right == -1:
                    right = 0
                    left += 1
        return left + right
