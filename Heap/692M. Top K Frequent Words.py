'''
692. Top K Frequent Words

Description:
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Example 1:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Constraints:
1 <= words.length <= 500
1 <= words[i] <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
'''

# Solution:
class Freq(object):
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __cmp__(self, other):
        if self.count != other.count:
            return cmp(self.count, other.count)
        else:
            return cmp(other.word, self.word)

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # count = defaultdict(int)
        # for word in words:
        #     count[word] += 1
        count = collections.Counter(words)
        l = []
        heapq.heapify(l)
        for key in count.keys():
            heapq.heappush(l, Freq(count[key], key))
            if len(l)>k:
                heapq.heappop(l)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(l).word)
        return ans[::-1]
        
