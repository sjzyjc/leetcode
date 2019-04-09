from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if not target:
            return -1
        
        visited = set(deadends) if deadends else set()
        queue = deque(["0000"])
        
        turn = 0
        while queue:
            length = len(queue)
           # print(queue)
            for _ in range(length):
                node = queue.popleft()
                if node == target:
                    return turn
                
                if node in visited:
                    continue
                    
                visited.add(node)
                for i in range(4):
                    queue.append(node[:i] + chr(ord('0') + (ord(node[i]) - ord('0') + 1) % 10) + node[i+1:])
                    queue.append(node[:i] + chr(ord('0') + (ord(node[i]) - ord('0') - 1) % 10) + node[i+1:])
                    
            turn += 1
            
        return -1
            
        