"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from collections import deque
class Solution:
    def __init__(self):
        self.global_buf = deque([])
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        if n <= 0:
            return 0
        
        ptr = 0
        while self.global_buf and ptr < n:
            buf[ptr] = self.global_buf.popleft()
            ptr += 1
            
        count = n // 4 if n % 4 == 0 else n // 4 + 1
        for i in range(count):
            tmp = [""] * 4
            l = read4(tmp)
            
            if l <= 0:
                break
                
            for item in tmp:
                if not item:
                    break
                    
                if ptr < n:
                    buf[ptr] = item
                    ptr += 1
                else:
                    self.global_buf.append(item)
                      
        return ptr
            
        
        