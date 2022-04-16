"""
1541. Minimum Insertions to Balance a Parentheses String

Description:
Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.


Example 1:
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string 
to be "(())))" which is balanced.

Example 2:
Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 

Constraints:
1 <= s.length <= 105
s consists of '(' and ')' only.
"""

# Solution:
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # num_in: record the number of brackets that we need to insert into the string 
        # need_right: record the number of right bracket we need from the string
        num_in, need_right = 0, 0
        for i in range(len(s)):
            if s[i]=="(":
                # we need 2 right brackest
                need_right += 2
                # if there is already one right bracket
                if need_right%2==1:
                    # we need to insert a right bracket
                    num_in += 1
                    # the need for the right bracket is then reduced by 1, since we will insert one right bracket
                    need_right -= 1
            if s[i]==")":
                need_right -= 1
                # if there is a redundant right bracket
                if need_right == -1:
                    # we need to insert a left bracket
                    num_in += 1
                    # we also need one right bracket from the string
                    need_right = 1

        return num_in + need_right
