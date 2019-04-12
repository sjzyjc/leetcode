# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        
        if not root1 or not root2:
            return False
        
        stack1 = [root1]
        stack2 = [root2]
        while stack1 and stack2:
            #self.print(stack1)
            #self.print(stack2)
            next_leaf_1 = self.getNext(stack1)
            next_leaf_2 = self.getNext(stack2)
            
            
            #print(next_leaf_1.val, next_leaf_2.val)
            if not next_leaf_1 or not next_leaf_2:
                return False
            
            if next_leaf_1.val != next_leaf_2.val:
                return False
            
        #self.print(stack1)
        #self.print(stack2)
        return len(stack1) == 0 and len(stack2) == 0
    
    def getNext(self, stack):
        #print("get next")
        ans = None
        while stack:
            #self.print(stack)
            node = stack.pop()
                
            if not node.left and not node.right:
                #print("before return")
                #self.print(stack)
                return node
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return ans