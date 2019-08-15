class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here
        time_set = set(time)
        cur_min = int(time[:2]) * 60 + int(time[3:])
              
        while True:
            cur_min += 1
            cur_min %= 1440
            
            m1 = str((cur_min % 60) % 10)
            m2 = str((cur_min % 60) // 10)
            h1 = str((cur_min // 60) % 10)
            h2 = str((cur_min // 60) // 10)
            
            if m1 in time_set and m2 in time_set and h1 in time_set and h2 in time_set:
                return h2 + h1 + ":" + m2 + m1
            
        return cur_min
            