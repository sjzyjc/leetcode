# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1
            
        self.pos = head
        return self.convert(length)
    
    def convert(self, length):
        if length <= 0:
            return None
        
        node = TreeNode('#')
        node.left = self.convert(length // 2)
        node.val = self.pos.val
        self.pos = self.pos.next
        node.right = self.convert(length - length // 2 - 1)
        
        return node
        