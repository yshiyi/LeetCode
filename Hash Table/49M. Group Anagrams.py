'''
49. Group Anagrams
Hash Table, String

Description:
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Similar Questions:
Valid Anagram - Easy
Group Shifted Strings - Medium
'''

# Solution:
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        '''
        Method 1: Use collections to make a dictionary with list
                  >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
                  >>> d = defaultdict(list)
                  >>> for k, v in s:
                  ...     d[k].append(v)
                  ...
                  >>> d.items()
                  [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
        '''
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        
        '''
        Method 2: Because sorted(string) returns a list, we need to convert this list of characters to a complete string.
                  For each sorted string, we check if it is contained in result.
                  If not, create a new key. If so, add this word to the existing value.
        '''
        result = {}
        if len(strs) < 1:
            return [['']]
        for word in strs:
            sorted_word = self.toString(sorted(word))
            if sorted_word not in result:
                result[sorted_word] = [word]
            else:
                result[sorted_word] = result[sorted_word] + [word]
        return result.values()

    def toString(self, word):
        result = ''
        for char in word:
            result += char
        return result
        
