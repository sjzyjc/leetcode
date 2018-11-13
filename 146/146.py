class DoubleNode:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key
        
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        head = DoubleNode("^", "^")
        tail = DoubleNode("$", "$")
        head.next = tail
        tail.prev = head
        
        self.head = head
        self.tail = tail
        self.map = {}
        self.cap = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1
        
        
        node = self.map[key]
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        first.prev = node
        node.next = first
        
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = None
        if key in self.map:
            node = self.map[key]
            node.val = value
            
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node_next
            node_next.prev = node_prev
            
            first = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = first
            first.prev = node            
        else:
            node = DoubleNode(key, value)
            first = self.head.next

            self.head.next = node
            node.next = first
        
            first.prev = node
            node.prev = self.head
            self.map[key] = node
        

        if len(self.map) > self.cap:
            least = self.tail.prev
            prev = least.prev
            self.tail.prev = prev
            prev.next = self.tail
            del self.map[least.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)