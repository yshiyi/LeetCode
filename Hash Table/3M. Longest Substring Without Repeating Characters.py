'''
3M. Longest Substring Without Repeating Characters
Hash Table, Two Pointers, String, Sliding Window

Description:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Similar Questions:
Longest Substring with At Most Two Distinct Characters - Medium
Longest Substring with At Most K Distinct Characters - Hard
Subarrays with K Different Integers - Hard
'''

# Solution:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        Method 1: Brute force
                  Check all the elements one by one to see if there is any duplicate character.
                  There is only one pointer and two while loops in this method. 
                  Sweep the string from the beginning, and save the character and its position in a dictionary.
                  If we meet a duplicate character. We update the max_len with max_len = max(max_len, len(dic.keys())).
                  We then move the pointer back to its previous position + 1 and clear the dictionary.
        '''
        p = 0
        max_len = 0
        dic = {}
        
        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return 1
        
        while p < len(s) - 1:
            flag = True  # Check if there is a duplicate character
            while flag and p < len(s):
                if s[p] not in dic:
                    dic[s[p]] = p
                    p += 1
                    if p == len(s):
                        max_len = max(max_len, len(dic.keys()))
                        return max_len                    
                else:
                    flag = False
            p = dic[s[p]] + 1
            max_len = max(max_len, len(dic.keys()))
            dic = {}
        
        
        '''
        Method 2: Slideing window
                  A sliding window is an abstract concept commonly used in array/string problems. 
                  A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i, j)[i,j).
                  A sliding window is a window "slides" its two boundaries to the certain direction.
                  
                  Notice that we use two while loops in method 1. We can improve that method by using two pointers.
                  Specifically, we don't need to move the pointer a little by little. 
                  We can skip all the elements in the sliding window and let it be j+1 directly.
                  The difference between two pointers defines the length of the substring.
                  The pointer p2 sweeps the whole string.
                  The pointer p1 points to the first character at the beginning and will move to max(Dic[s[p2]], p1) when there is a duplicate character.
                  Notice, we let Dic[s[p2]] = p2 + 1. If we let p1  = max(Dic[s[p2]], p1) + 1, p1 will shift by 1 when we meet a duplicate character.
        '''
        p1 = 0
        max_len = 0
        Dic = {}
        
        for p2 in range(len(s)):
            if s[p2] in Dic:
                p1  = max(Dic[s[p2]], p1)
            Dic[s[p2]] = p2 + 1
            max_len = max(max_len, p2 - p1 + 1)
        
        return max_len

        # Another way using sliding window
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        window = {}
        right, left = 0, 0
        res = 0
        while (right < len(s)):
            c = s[right]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            right += 1
            while (window[c]>1):
                d = s[left]
                window[d] -= 1
                left += 1
            res = max(res, right-left)
        return res
