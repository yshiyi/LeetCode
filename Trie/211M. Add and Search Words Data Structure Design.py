class TrieNode(object):
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            if node.next[letter] == 0:
                node.next[letter] = TrieNode()
            node = node.next[letter]
        node.is_word = True
        
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        
        def searchTrie(node, word, i):
            if i==len(word):
                return node.is_word
            if word[i]!='.':
                if node.next[word[i]] is None:
                    return False
                return searchTrie(node.next[word[i]], word, i+1)
            else:
                for key in node.next:
                    if node.next[key] is not None and searchTrie(node.next[key], word, i+1):
                        return True
            return False
        
        return searchTrie(node, word, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
