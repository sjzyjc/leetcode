# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root or k < 0:
            return []
        
        ans = []
        path = []
        self.find(root, target, path)
        if len(path) == 0:
            return []
        
        node = path.pop()
        ans.extend(self.searchDown(node, k, None))
        
        up = 1
        while path and k - up >= 0:
            prev = path.pop()
            ans.extend(self.searchDown(prev, k - up, node))

            node = prev
            up += 1
            
        return ans
        
    def find(self, cur, target, path):
        if cur is None:
            return False
        
        path.append(cur)
        if cur.val == target.val:
            return True
        
        if self.find(cur.left, target, path):
            return True
        
        if self.find(cur.right, target, path):
            return True
        
        path.pop()
        return False
    
    def searchDown(self, node, k, nextt):
        if not node:
            return []
        
        if k == 0:
            return [node.val]
        
        left_nodes = right_nodes = []
        if nextt == node.right or nextt is None: 
            left_nodes = self.searchDown(node.left, k - 1, None)
        
        if nextt == node.left or nextt is None:
            right_nodes = self.searchDown(node.right, k - 1, None)
            
        return left_nodes + right_nodes
            
            
        