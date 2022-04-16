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
Method: 
"""
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # num_in: record the number of bracket that we need to insert into the string
        # need_right: record the number of right bracket that we need from the string
        num_in, need_right = 0, 0
        for i in range(len(s)):
            if s[i]=="(":
                need_right += 1
            if s[i]==")":
                need_right -= 1
                # when there is an extra right bracket
                if need_right == -1:
                    # we need to insert a left bracket into the string
                    num_in += 1
                    # set need_right = 0, because we don't need any more right bracket from the string
                    need_right = 0
        return num_in + need_right
