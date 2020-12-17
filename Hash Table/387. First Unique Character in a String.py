'''
387. First Unique Character in a String
Hash Table, String

Description:
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Similar Question:
Sort Characters By Frequency - Medium
'''

# Solution:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        Method: Create two dictionaries.
                The first one contains all the characters have been seen. The second one contains those haven't.
                Loop through all the characters in s.
                If the char is not in either of Seen and Unseen, we save it and its index to Unseen.
                If the char is in Unseen and not in Seen, we remove it from Unseen and save it to Seen.
                If len(Unseen.keys()) is not 0, we return min(Unseen.values()).
        '''
        Seen = {}
        Unseen = {}
        index = 0
        for char in s:
            if char not in Unseen and char not in Seen:
                Unseen[char] = index
            elif char in Unseen and char not in Seen:
                del Unseen[char]
                Seen[char] = index
            index += 1
        if len(Unseen.keys()) != 0:
            return min(Unseen.values())
        else:
            return -1
        
        
        """
        Method 2: build hash map : character and how often it appears
        """
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
