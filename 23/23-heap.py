# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        queue = []
        ans = ptr = ListNode('dummy')
        
        if lists is None or len(lists) == 0:
            return None
    
        for index, listt in enumerate(lists):
            if listt is None:
                continue
                
            heapq.heappush(queue, (listt.val, index))
            listt = listt.next
        
        while queue:
            val, listt_index = heapq.heappop(queue)
            
            #set to next node
            lists[listt_index] = lists[listt_index].next
                           
            node = ListNode(val)
            ptr.next = node
            ptr = ptr.next
            
            if lists[listt_index]:
                heapq.heappush(queue, (lists[listt_index].val, listt_index))
            
        return ans.next