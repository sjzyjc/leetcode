# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        dummy = ptr = ListNode('#')
        queue = []
        for index, listt in enumerate(lists):
            if not listt:
                continue
                
            heapq.heappush(queue, [listt.val, index])
            
        while queue:
            val, index = heapq.heappop(queue)
            
            node = lists[index]
            lists[index] = node.next
            
            node.next = None
            ptr.next = node
            ptr = ptr.next
            
            if lists[index]:
                heapq.heappush(queue, [lists[index].val, index])
                
        return dummy.next
            
            
            
        