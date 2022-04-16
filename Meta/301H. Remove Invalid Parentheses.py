"""
301. Remove Invalid Parentheses

Description:
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
Return all the possible results. You may return the answer in any order.
 

Example 1:
Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:
Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:
Input: s = ")("
Output: [""]
 

Constraints:
1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

"""
Method: backtracking
        At first, we need to count the number of extra left brackets and extra right brackets.
        The end condition of the recursion is if there are no extra left or right brackets and the string is valid.
        To check if the string is valid, we only need to track the number of redundant left brackets.
        In the recursion function, we need to check the characters from start to len(s).
        If there are consecutive same bracket, we only need to remove the first one.
        Time complexity: O(2^(l+r))
        Space complexity: O(n^2)
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = 0, 0
        for c in s:
            if c=="(":
                l += 1
            elif c==")":
                if l==0:
                    r+=1
                else:
                    l -= 1
        self.res = []
        self.helper(s, 0, l, r)
        return self.res
    
    
    def isValid(self, s):
        left = 0
        for c in s:
            if c=="(":
                left += 1
            elif c==")":
                left-=1
            if left<0:
                return False
        return True if left==0 else False
    
    def helper(self, s, start, l, r):
        if l==0 and r==0:
            if self.isValid(s):
                self.res.append(copy.deepcopy(s))
            return
        for i in range(start, len(s)):
            if i!=start and s[i]==s[i-1]:
                continue
            if r>0 and s[i]==")":
                self.helper(s[:i]+s[i+1:], i, l, r-1)
            if l>0 and s[i]=="(":
                self.helper(s[:i]+s[i+1:], i, l-1, r)
