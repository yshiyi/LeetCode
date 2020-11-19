'''
205. Isomorphic Strings
Hash Table

Description:
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Similar Question:
Word Pattern - Easy
'''

# Solution:
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        '''
        Method : The goal is to check the pattern of two strings.
                 Use zip() to pair two strings together.
                 Firstly, we check if the character has been seen before. If so, save it to a dictionary.
                 Secondly, if the character has been seen before in both strings, we check the previous position.
                 If it appears at the same position, we continue the loop. Otherwise, we return false.
                 If there are other scenarios, we return false.
        '''
        Dic1 = {}
        Dic2 = {}
        index = 0
        for cha1, cha2 in zip(s, t):
            if cha1 not in Dic1 and cha2 not in Dic2:
                Dic1[cha1] = index
                Dic2[cha2] = index
            elif cha1 in Dic1 and cha2 in Dic2:
                if Dic1[cha1] == Dic2[cha2]:
                    continue
                else:
                    return False
            else:
                return False
            index += 1
        return True
