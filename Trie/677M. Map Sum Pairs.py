class TrieNode(object):
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.score = 0

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = 0
        if key in self.map:
            delta = val - self.map[key]
        self.map[key] = val
        node = self.root
        for letter in key:
            if node.next[letter] == 0:
                node.next[letter] = TrieNode()
            node = node.next[letter]
            if delta != 0:
                node.score = node.score + delta
            else:
                node.score = node.score + val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for letter in prefix:
            node = node.next[letter]
            if node.next[letter] is None:
                return 0
        return node.score
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
