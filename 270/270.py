# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return int(self.findClosestVal(root, target))
    
    def findClosestVal(self, node, target):
        if not node:
            return None
        
        if node.val == target:
            return target
            
        elif node.val < target:
            right_closest = self.findClosestVal(node.right, target)
            if right_closest is None or abs(node.val - target) < abs(right_closest - target):
                return node.val
            else:
                return right_closest
                
        else:
            left_closest = self.findClosestVal(node.left, target)
            if left_closest is None or abs(node.val - target) < abs(left_closest - target):
                return node.val
            else:
                return left_closest

                
