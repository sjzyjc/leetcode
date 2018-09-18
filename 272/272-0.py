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
        """
        
        if not root:
            return []
        
        self.sorted = []
        self.inOrder(root)
        
        start, end = 0, len(self.sorted) - 1
        firstLarge = self.findFirstLarge(target)
        counter = 0
        ans = []
        
        if firstLarge == 0:
            return self.sorted[: k]
        
        left, right = firstLarge - 1, firstLarge

        while counter < k:
            if left < 0 or right > len(self.sorted) - 1:
                break
                
            if abs(self.sorted[left] - target) <= abs(self.sorted[right] - target): 
                ans.append(self.sorted[left])
                left -= 1
            else:
                ans.append(self.sorted[right])
                right += 1    
            counter += 1
            
        if counter < k:
            if left < 0:
                ans.extend(self.sorted[counter: k])
            else:
                ans.extend(self.sorted[len(self.sorted) - k : len(self.sorted) - counter])
        
        return ans
    
    
    def inOrder(self, root):
        if not root:
            return
        
        self.inOrder(root.left)
        self.sorted.append(root.val)
        self.inOrder(root.right)
    
    def findFirstLarge(self, target):
        start, end = 0, len(self.sorted) - 1
        while start < end:
            mid = (start + end) // 2
            if self.sorted[mid] == target:
                return mid
            elif self.sorted[mid] < target:
                start = mid + 1
            else:
                end = mid
                
        return start
                
        