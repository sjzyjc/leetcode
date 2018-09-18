class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        
        if not stones:
            return False
        
        f = {index:set() for index in stones}
        f[0] =  set([0])
        
        for stone in stones:
            avl_steps = f[stone]
            for step in avl_steps:
                for offset in range(-1, 2):
                    if step + offset > 0 and stone + step + offset in f:
                        f[stone + step + offset].add(step + offset)
        
        return len(f[stones[-1]]) != 0
                        
                    