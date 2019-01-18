# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        
        small = []
        large = []
        node1 = node2 = root
        while node1:
            small.append(node1)
            node1 = node1.left
            
        while node2:
            large.append(node2)
            node2 = node2.right
            
        
        smallest = self.getNext(small)
        largest = self.getPrev(large)
        
        while smallest:
            next_node = self.getNext(small)
            if smallest.val > next_node.val:
                break
                
            smallest = next_node
            
        while largest:
            prev_node = self.getPrev(large)
            if largest.val < prev_node.val:
                break
            
            largest = prev_node
        
        #print(smallest, largest)
        smallest.val, largest.val = largest.val, smallest.val
        
    def getNext(self, small):
        if not small:
            return None
            
        ans = small.pop()
        node = ans.right
        while node:
            small.append(node)
            node = node.left
                
        return ans
        
    def getPrev(self, large):
        if not large:
            return None
            
        ans = large.pop()
        node = ans.left
        while node:
            large.append(node)
            node = node.right
                
        return ans
            
        
        