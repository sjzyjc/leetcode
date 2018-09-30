class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m == n:
            return head
        
        count = 1
        iterator = head
        init = ListNode(-1)
        init.next = head
        m_prev = prev = init
        
        while count <= n:
            if count == m:
                m_prev = prev
                
            elif m < count <= n:
                nextt = iterator.next
                iterator.next = prev
                prev = iterator
                iterator = nextt
                count += 1
                continue
            
            prev = iterator
            iterator = iterator.next
            count += 1
        
        m_node = m_prev.next
        m_prev.next = prev
        m_node.next = iterator
        
        return init.next
            
        