from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if tasks is None:
            return 0
        
        if n <= 0:
            return len(tasks)
        
        count = [0 for _ in range(26)]
        max_count = 0
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort(reverse = True)
        size = count[0] - 1
        total_idle = size * n
        
        for i in range(1, len(count)):
            total_idle -= min(size, count[i])
                
        #even no space can insert into a cooling intervel
        return total_idle + len(tasks) if total_idle > 0 else len(tasks)
            
        
            
        
            
            
        
        
        