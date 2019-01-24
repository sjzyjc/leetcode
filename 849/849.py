class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if not seats:
            return None
        
        last_person = -1
        max_distance = 0
        for index in range(len(seats)):
            if seats[index] == 0:
                continue
            
            #first person met
            if last_person == -1:
                max_distance = index
            else:
                max_distance = max(max_distance, (index - last_person) // 2)
                
            last_person = index
            
        return max(max_distance, len(seats) - 1 - last_person)
            
            
            
            