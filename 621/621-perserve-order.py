from collections import defaultdict
class Solution:
    def leastInterval(self, tasks, k):
        if tasks is None:
            return 0
        
        if k <= 0:
            return len(tasks)
        
        last = [-1 for _ in range(26)]
        cur_slot = 0
        ans = []
        for task in tasks:
            cur_slot += 1
            orginal_time = cur_slot
            index = ord(task) - ord('A')
            if not(last[index] == -1 or cur_slot - last[index] - 1 >= k):
                cur_slot = last[index] + k + 1

            last[index] = cur_slot
            ans.extend(['idle'] * (cur_slot - orginal_time))
            ans.append(task)

        return "->".join(ans)

sl = Solution()
arr = ['A', 'B', 'A', 'C']
k = 2
print(sl.leastInterval(arr, k))            
        
            
        
            
            
        
        
        