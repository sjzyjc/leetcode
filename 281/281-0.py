class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.cur_ptr = 0
        self.arr = []
        
        ptr1 = ptr2 = 0
        while ptr1 < len(v1) and ptr2 < len(v2):
            self.arr.append(v1[ptr1])
            self.arr.append(v2[ptr2])
            ptr1 += 1
            ptr2 += 1
            
        if ptr1 < len(v1):
            self.arr.extend(v1[ptr1:])
            
        if ptr2 < len(v2):
            self.arr.extend(v2[ptr2:])
        
        
    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return -1
        
        ans = self.arr[self.cur_ptr]
        self.cur_ptr += 1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_ptr < len(self.arr)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())