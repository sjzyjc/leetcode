class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if n <= 0:
            return []
        
        ans = [0 for _ in range(n)]
        stack = []
        for log in logs:
            log_arr = log.split(':')
            pid = int(log_arr[0])
            is_start = (log_arr[1] == "start")
            time = int(log_arr[2])
            
            #print(log, stack, is_start, log[1])
            if is_start:
                stack.append(time)
            else:
                cumulate = 0
                while stack and stack[-1] < 0:
                    cumulate += -stack.pop()
                
                cost = time - cumulate - stack.pop() + 1
                ans[pid] += cost
                stack.append( -(cumulate + cost))
                
        return ans
                
        