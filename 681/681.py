class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    def nextClosestTime(self, time):
        # write your code here
        digits = [int(i) for i in time if i != ":"]
        cur_min = int(time[:2]) * 60 + int(time[3:])
        
        while True:
            cur_min = (cur_min + 1) % 1440
            
            hour = cur_min // 60
            minute = cur_min % 60
            
            if not (0 <= hour < 24 and 0 <= minute <= 60):
                continue
            
            if (hour // 10) in digits and (hour % 10) in digits and (minute // 10) in digits and (minute % 10) in digits:
                str_hour = str(hour) 
                str_minute = str(minute)
                if hour < 10:
                    str_hour = "0" + str_hour
                    
                if minute < 10:
                    str_minute = "0" + str_minute
                return str_hour + ":" + str_minute
                
        return time