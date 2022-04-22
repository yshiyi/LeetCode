class Node(object):
    def __init__(self, k, v, next=None, prev=None):
        self.key = k
        self.value = v
        self.next = next
        self.prev = prev

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = collections.defaultdict(Node)
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic.keys():
            return -1
        self.removeNode(self.dic[key])
        self.addNode(self.dic[key])
        
        return self.dic[key].value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic.keys():
            self.removeNode(self.dic[key])
        self.dic[key] = Node(key, value)
        self.addNode(self.dic[key])
        if len(self.dic) > self.cap:
            node = self.head.next
            self.removeNode(node)
            self.dic.pop(node.key, None)
    
    def removeNode(self, node):
        tmp1 = node.prev
        tmp2 = node.next
        tmp1.next = node.next
        tmp2.prev = node.prev
    
    def addNode(self, node):
        tmp1 = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        tmp1.next = node
        node.prev = tmp1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
