class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.map = {}
        self.cap = capacity
        
        self.head = Node("^", "^")
        self.tail = Node("#", "#")
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.map:
            return -1
            
        node = self.map[key]
        self.update(node)
        
        return node.val
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def put(self, key, value):
        # write your code here
        
        if key in self.map:
            node = self.map[key]
            node.val = value
            
            self.update(node)
        else:
            node = Node(key, value)
            first_node = self.head.next
            
            self.head.next = node
            node.prev = self.head
            
            node.next = first_node
            first_node.prev = node
            
            self.map[key] = node
                    
        
        if len(self.map) > self.cap:
            to_drop = self.tail.prev
            
            self.tail.prev = to_drop.prev
            to_drop.prev.next = self.tail
            
            del self.map[to_drop.key]
            

            
            
    def update(self, node):
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

        first_node = self.head.next
        node.next = first_node
        first_node.prev = node
        
        self.head.next = node
        node.prev = self.head

        
        

