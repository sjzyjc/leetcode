from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if not target:
            return -1
        
        visited = set(deadends) if deadends else set()
        queue = deque([("0000", True), (target, False)])
        start_seen = set()
        end_seen = set()
        
        turn = 0
        while queue:
            length = len(queue)
           # print(queue)
            for _ in range(length):
                node, is_start = queue.popleft()
                if is_start and node in end_seen:
                    return turn - 1
                
                if not is_start and node in start_seen:
                    return turn
                
                if node in visited or (is_start and node in start_seen) or (not is_start and node in end_seen):
                    continue
                    
                if is_start:
                    start_seen.add(node)
                else:
                    end_seen.add(node)
                    
                for i in range(4):
                    queue.append((node[:i] + chr(ord('0') + (ord(node[i]) - ord('0') + 1) % 10) + node[i+1:], is_start))
                    queue.append((node[:i] + chr(ord('0') + (ord(node[i]) - ord('0') - 1) % 10) + node[i+1:], is_start))
                    
            turn += 2
            
        return -1
            
        