import random
class Node:
    def __init__(self, count):
        self.count = count
        self.set = set()
        self.next = None
        self.prev = None
        
    def add(self, key):
        self.set.add(key)
        
    def remove(self, key):
        if key in self.set:
            self.set.remove(key)
            
    def isEmpty(self):
        return len(self.set) == 0
    
    def get(self):
        return random.sample(self.set, 1)[0]
            
class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node((1 << 31) - 1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def isEmpty(self):
        return self.head.next == self.tail
    
    def insert(self, pos, node):
        nextt = pos.next

        pos.next = node
        node.prev = pos
        
        node.next = nextt
        nextt.prev = node
    
    def remove(self, node):
        prev = node.prev
        nextt = node.next
        
        prev.next = nextt
        nextt.prev = prev
        
    
    def getMax(self):
        if self.isEmpty():
            return ""
        
        return self.tail.prev.get()
    
    def getMin(self):
        if self.isEmpty():
            return ""
        
        return self.head.next.get()
        
     
        
class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_map = {}
        self.ll = DoubleLinkedList()
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """
        cur_node = self.key_map[key] if key in self.key_map else self.ll.head
        cur_node.remove(key)
        
        nextt = cur_node.next
        if cur_node.count + 1 == nextt.count: #has next node
            new_node = nextt
        else:
            new_node = Node(cur_node.count + 1)
            self.ll.insert(cur_node, new_node)
            
        new_node.add(key)
        self.key_map[key] = new_node
        
        if cur_node != self.ll.head and cur_node.isEmpty():
            self.ll.remove(cur_node)
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.key_map:
            return
        
        cur_node = self.key_map[key]
        cur_node.remove(key)
        
        if cur_node.count > 1:
            prev = cur_node.prev
            if cur_node.count - 1 == prev.count:
                new_node = prev
            else:
                new_node = Node(cur_node.count - 1)
                self.ll.insert(prev, new_node)
                
            new_node.add(key)
            self.key_map[key] = new_node
        else:
            del self.key_map[key]
            
        if cur_node.isEmpty():
            self.ll.remove(cur_node)
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.ll.getMax()

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.ll.getMin()
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()