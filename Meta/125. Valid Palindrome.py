'''
125. Valid Palindrome

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing 
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include 
letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Example 4:
".,": True
"0P": False

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# Solution
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1

        while left < right:
            while left < right and s[left].isalnum()==0:
                left += 1
            while left < right and s[right].isalnum()==0:
                right -= 1
            if s[left].lower()!=s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        
