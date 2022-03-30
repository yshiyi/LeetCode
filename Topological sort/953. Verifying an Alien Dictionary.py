"""
953. Verifying an Alien Dictionary

Description:
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', 
where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

"""
Time complexity : O(M). M is the total number of characters in words.
Storing the letter-order relation of each letter takes O(N) time. 
For the nested for-loops, we examine each pair of words in the outer-loop and for the inner loop, 
we check each letter in the current word. Therefore, we will iterate over all of letters in words.

Taking both into consideration, the time complexity is O(M + N). 
However, we know that N is fixed as 26. Therefore, the time complexity is O(M).

Space complexity : O(1). 
The only extra data structure we use is the hashmap that serves to store the letter-order relations 
for each word in order. 
Because the length of order is fixed as 26, this approach achieves constant space complexity.
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = defaultdict(int)
        for index, char in enumerate(order):
            dic[char] = index
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if dic[words[i][j]] > dic[words[i+1][j]]:
                        return False
                    break
        return True
        
