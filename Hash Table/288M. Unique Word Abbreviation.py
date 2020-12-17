"""
288M. Unique Word Abbreviation
Hash Table, Design

Description:
An abbreviation of a word follows the form <first letter><number of characters><last letter>. Below are some examples of word abbreviations:
a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") -> false    "deer" and "door" have the same abbreviation
isUnique("cart") -> true     no other words have the same abbre
isUnique("cane") -> false    "cake" has the same abbre
isUnique("make") -> true     no other words have the same abbre


Similar Questions:
Two Sum III - Data structure design - Easy
Generalized Abbreviation
"""

# Solution:
"""
Method: At first, we need to find out the conditions to determine if a word's abbreviation is unique in the dictionary.
        There are only two conditions we return true for isUnique("word"):
             1. The abbreviation of the word does not appear in the dictionary.
             2. The abbreviation of the word appears in the dictionary and the word appears one and only once in the dictionary.
                In other words, if there are some other words have the same abbreviation, then return false.
        Therefore, we need to create a dictionary in which the key is the abbreviation and the value is a set which contains words.
"""

from collections import defaultdict


class ValidWordAbbr:
    def __init__(self, _dictionary):
        # self.dic = defaultdict(set)
        # for word in _dictionary:
        #     self.dic[self.abbrev(word)].add(word)
        self.dic = defaultdict(list)
        for word in _dictionary:
            self.dic[self.abbrev(word)].append(word)

    def isUnique(self, word):
        if self.abbrev(word) not in self.dic:
            return True
        elif word == self.dic[self.abbrev(word)]:
            return True
        else:
            return False

    def abbrev(self, word):
        if len(word) < 3:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]


dictionary = ["deer", "door", "cake", "card"]
obj = ValidWordAbbr(dictionary)
print(obj.isUnique("dear"), obj.isUnique("cart"), obj.isUnique("cane"), obj.isUnique("make"))

dictionary2 = ["a", "a"]
obj2 = ValidWordAbbr(dictionary2)
print(obj2.isUnique("a"))
