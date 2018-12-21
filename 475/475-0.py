class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if not houses or not heaters:
            return -1
        
        houses.sort()
        heaters.sort()
        target = houses[0]
        ans = 0
        for index, heater in enumerate(heaters):
            #print(heater)
            if index > 0:
                target = heater - ((heater - heaters[index - 1]) / 2)
                first_large_equal = self.findFirstLarge(houses, target)
                if first_large_equal != -1:
                    ans = max(ans, heater - first_large_equal)

            else:
                if heater > houses[0]:
                    ans = max(ans, heater - houses[0])
            if index < len(heaters) - 1:
                target = heater + ((heaters[index + 1] - heater) / 2)
                
                last_small_equal = self.findLastSmall(houses, target)
                if last_small_equal != -1:
                    ans = max(ans, last_small_equal - heater)
            else:
                if heater < houses[-1]:
                    ans = max(ans, houses[-1] - heater)
            
            #print(heater, ans)
                
        return ans
    
    def findFirstLarge(self, houses, target):
        #print("!")
        #print(target)
        start, end = 0, len(houses) - 1
        while start < end:
            mid = start + (end - start) // 2
            if houses[mid] < target:
                start = mid + 1
            else:
                end = mid
            
        if houses[start] >= target:
            return houses[start]
        else:
            if start < len(houses) - 1:
                return houses[start + 1]
            else:
                return -1
        
    def findLastSmall(self, houses, target):
        #print("?")
        #print(target)
        start, end = 0, len(houses) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if houses[mid] > target:
                end = mid - 1
            else:
                start = mid
        
        if houses[end] <= target:
            return houses[end]
        else:
            if houses[start] <= target:
                return houses[start]
            else:
                return -1
        
        
    