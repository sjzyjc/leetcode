# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        logN + K
        """
        if not root:
            return []
        
        self.small = []
        self.large = []
        
        node = root
        while node:
            if node.val < target:
                self.small.append(node)
                node = node.right
            else:
                self.large.append(node)
                node = node.left
                
        counter = 0
        ans = []
        while counter < k:
            left_diff = abs(target - self.small[-1].val) if self.small else None
            right_diff = abs(target - self.large[-1].val) if self.large else None
            if left_diff is not None and right_diff is not None:
                if left_diff <= right_diff:
                    ans.append(self.small[-1].val)
                    self.findPrev()
                else:
                    ans.append(self.large[-1].val)
                    self.findNext()
            elif left_diff is not None:
                ans.append(self.small[-1].val)
                self.findPrev()
            else:
                ans.append(self.large[-1].val)
                self.findNext()
                
            counter += 1
                
        return ans
    
    def findPrev(self):
        node = self.small.pop()
        if not node:
            return None
        
        node = node.left
        while node:
            self.small.append(node)
            node = node.right
            
    def findNext(self):
        node = self.large.pop()
        if not node:
            return None
        
        node = node.right
        while node:
            self.large.append(node)
            node = node.left
            
    
    
                
        