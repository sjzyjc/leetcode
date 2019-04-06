
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord:
            return 0
        
        begin_seen = set()
        end_seen = set()
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        queue = deque([(beginWord, True), (endWord, False)])
        level = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                #print(queue)
                word, is_begin = queue.popleft()
                if (is_begin and word in end_seen):
                    return level
                elif (not is_begin and word in begin_seen):
                    return level + 1
                
                if (is_begin and word in begin_seen) or (not is_begin and word in end_seen):
                    continue
                    
                if is_begin:
                    begin_seen.add(word)
                else:
                    end_seen.add(word)
                    
                for index, charr in enumerate(word): 
                    for i in range(ord('a'), ord('z') + 1):
                        if chr(i) == charr:
                            continue
                            
                        new_word = word[:index] + chr(i) + word[index + 1:]
                        if new_word not in wordList:
                            continue
                            
                        queue.append((new_word, is_begin))
            level += 2
                        
        return 0
                    
        