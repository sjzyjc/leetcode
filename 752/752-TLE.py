from collections import deque
class Solution:
    def openLock(self, deadends, target):
        if not target:
            return -1
        
        locked = set(deadends)
        queue = deque(["0000"])
        visited = set()
        step = -1
        while queue:
            step += 1
            length = len(queue)
            print(len(visited), len(queue))
            for _ in range(length):
                cur = queue.popleft()

                if cur in visited or cur in locked:
                    continue
                            
                visited.add(cur)
                if cur == target:
                    return step
                
                for i in range(4):
                    for delta in [-1, 1]:
                        nextt = cur[:i] + chr((ord(cur[i]) - 48 + delta) % 10 + 48) + cur[i + 1:]
                        queue.append(nextt)
                        
        return -1

sl = Solution()
deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(sl.openLock(deadends, target))
