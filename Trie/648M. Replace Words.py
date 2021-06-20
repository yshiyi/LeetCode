class TrieNode(object):
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.is_word = False

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        root = TrieNode();
        def createTrie(word):
            node = root;
            for letter in word:
                if node.next[letter] is None:
                    node.next[letter] = TrieNode()
                node = node.next[letter]
            node.is_word = True
        
        def searchPrefix(word):
            node = root
            res = ""
            for letter in word:
                if node.next[letter] is None:
                    break
                res += letter
                node = node.next[letter]
                if node.is_word:
                    return res
            return word
        
        for word in dictionary:
            createTrie(word)
        res = ""
        for word in sentence.split():
            if res:
                res += " "
            res += searchPrefix(word)
        return res
        
