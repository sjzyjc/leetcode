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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)
        
        mid = self.findMid(head)
        nextt = mid.next
        mid.next = None
        

        node = TreeNode(mid.val)
        if head != mid:
            node.left = self.sortedListToBST(head)
        
        node.right = self.sortedListToBST(nextt)
        
        return node
    
    def findMid(self, ptr):
        prev = None
        slow = ptr
        fast = ptr.next
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = None
        
        return slow
    
    def print(self, node):
        ptr = node
        while ptr:
            print(ptr.val, end = '->')
            ptr = ptr.next
            
        print("")
            
        