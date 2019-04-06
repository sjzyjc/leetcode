from collections import defaultdict
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""
        
        counts = defaultdict(int)
        for letter in S:
            counts[letter] += 1
            
        
        heap = []
        for key in counts:
            heapq.heappush(heap, (-counts[key], key))
            
        max_count, max_char = heapq.heappop(heap)
        max_count = -max_count
        empty_slots = max_count - 1
        index = 0
        
        ans = [[max_char] for _ in range(max_count)]
        #print(ans)
        while heap:
            count, charr = heapq.heappop(heap)
            count = -count
            for _ in range(min(max_count - 1, count)):
                ans[index % (max_count - 1)].append(charr)
                index += 1
                empty_slots -= 1
                
            if count == max_count:
                ans[-1].append(charr)
                
        #print(ans)
        if empty_slots > 0:
            return ""
        
        ans_arr = []
        for line in ans:
            ans_arr.append("".join(line))
        
        return "".join(ans_arr)
            
            

        
        
            
    
        