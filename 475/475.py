class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        O(N + M)
        """
        if not houses or not heaters:
            return -1
        
        houses.sort()
        heaters.sort()
        #print(houses)
        #print(heaters)
        
        ptr = 0
        ans = 0
        for index, heater in enumerate(heaters):
            if index > 0:
                low_bound = heater - ((heater - heaters[index - 1]) / 2)
                while ptr < len(houses) and houses[ptr] < low_bound:
                    ptr += 1
                
                if ptr < len(houses):
                    ans = max(ans, heater - houses[ptr])
            else:
                if heater > houses[0]:
                    ans = max(ans, heater - houses[0])
            #print(heater, ans, ptr)        
            if index < len(heaters) - 1:
                high_bound = heater + ((heaters[index + 1] - heater) / 2)
                
                while ptr < len(houses) and houses[ptr] <= high_bound:
                    ptr += 1
                    
                if 0 <= ptr - 1 < len(houses): 
                    ans = max(ans, houses[ptr - 1] - heater)
            else:
                if heater < houses[-1]:
                    ans = max(ans, houses[-1] - heater)
            
            #print(heater, ans)
                
        return ans
    

        
    