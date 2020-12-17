'''
249M. Group Shifted Strings
Hash Table

Description:
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
We can keep "shifting" which forms the sequence: "abc" -> "bcd" -> ... -> "xyz" or "adg -> beh -> cfi ..."
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:
given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''

# Solution:
class Solution(object):
    def groupStrings(self, strs):
        # Use function ord() to convert alphabet to integer. ord('a') -> 97, chr(97) -> 'a'
        # We use ord('a') - 97 to convert 'a' to 0.
        # Note that 'abc' -> 0,1,2, 'bcd' -> 1,2,3 and 'xyz' -> 23,24,25. If we subtract the first number from the list,
        #   we can get  'abc' -> 0,1,2, 'bcd' -> 0,1,2 and 'xyz' -> 0,1,2
        # Notice that the successive letter of 'z' is 'a'. 'az' -> 0,25 and 'ba' -> 1,0.
        #   If we subtract 1 from 1,0, we get 0, -1. In this case, we can take the modulus of 26.
        #   0 % 26 = 0, -1 % 26 = 25.

        # The basic idea to convert the string to a list of integers.
        # Check if the sequence of the integers has been seen. If not, create a new key. If so, save it to existing key.

        result = {}
        for word in strs:
            word_converted = self.convertWord(word)
            # print(word_converted)
            if word_converted not in result:
                result[word_converted] = [word]
            else:
                result[word_converted] = result[word_converted] + [word]
        return result.values()

    def convertWord(self, word):
        L_word = []
        for char in word:
            L_word.append(ord(char))
        L_word = [(num - L_word[0]) % 26 for num in L_word]
        L_str = ''
        for num in L_word:
            L_str += str(num)
        return L_str
    
