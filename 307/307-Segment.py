class Node:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.val = val
        self.left = self.right = None
        
        
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.build(0, len(nums) - 1, nums)
    
    
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.modify(self.root, i, val)
       

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.query(self.root, i, j)
        
    def build(self, start, end, A):
        if start > end:
            return None
    	
        if start == end:
            return Node(start, end, A[start])
        
        node = Node(start, end, 0)
        
        mid = start + (end - start) // 2
        node.left = self.build(start, mid, A)
        node.right = self.build(mid + 1, end, A)
        
        if node.left:
            node.val += node.left.val
        
        if node.right:
            node.val += node.right.val
        
        return node
                
    def query(self, root, start, end):
        if not root:
            return
        
        if start == root.start and end == root.end:
            return root.val
        
        mid = root.start + (root.end - root.start) // 2
        if end <= mid:
            return self.query(root.left, start, end)
        elif start > mid:
            return self.query(root.right, start, end)
        else:
            return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)
        
    def modify(self, root, index, new_val):
        if not root:
            return
        
        if root.start == root.end:
            root.val = new_val
            return
        
        mid = root.start + (root.end - root.start) // 2
        if index <= mid:
            self.modify(root.left, index, new_val)
        else:
            self.modify(root.right, index, new_val)
            
        root.val = root.left.val + root.right.val


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)