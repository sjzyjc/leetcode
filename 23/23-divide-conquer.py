# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        return self.merge_sub(lists)
    
    
    def merge_sub(self, lists):
        if len(lists) == 1:
            return lists[0]
        
        if len(lists) == 2:
            return self.merge(lists[0], lists[1])
        
        left = self.merge_sub(lists[:len(lists) // 2])
        right = self.merge_sub(lists[len(lists) // 2:])
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        if left is None:
            return right
        
        if right is None:
            return left
        
        ptr1 = left
        ptr2 = right
        
        dummy = ListNode('#')
        iterator = dummy
        
        while ptr1 and ptr2:
            node = None
            if ptr1.val < ptr2.val:
                node = ListNode(ptr1.val)
                ptr1 = ptr1.next
            else:
                node = ListNode(ptr2.val)
                ptr2 = ptr2.next
                
            iterator.next = node
            iterator = iterator.next
            
        if ptr1:
            iterator.next = ptr1
            
        if ptr2:
            iterator.next = ptr2
            
        return dummy.next
            
            
            