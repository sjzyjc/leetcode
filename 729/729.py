class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left, self.right = None, None
        
class Tree:
    def __init__(self):
        self.root = Node(-1, -1)
    
    def insert(self, start, end):
        insert_node = Node(start, end)
        
        node = self.root
        while node:
            if node.start == start:
                return False
            elif node.end <= start:
                if node.right is None:
                    node.right = insert_node
                    return True
                node = node.right
            else:
                if node.start < end:
                    return False
                else:
                    if node.left is None:
                        node.left = insert_node
                        return True
                    node = node.left
                
class MyCalendar:

    def __init__(self):
        self.tree = Tree()        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        return self.tree.insert(start, end)
            
    
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)