from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not wordList or endWord not in wordList:
            return 0
        
        
        wordList = set(wordList)
        queue = deque([beginWord])
        visited = set([])
        ans = 1
        
        while queue:
            length = len(queue)
            ans += 1

            for _ in range(length):
                word = queue.popleft()
            
                for index, c in enumerate(word):
                    for new_char in range(ord('a'), ord('z') + 1):
                        if c == chr(new_char):
                            continue
                    
                        new_word = word[:index] + chr(new_char) + word[index + 1:]
                        if new_word not in wordList or new_word in visited:
                            continue
                    
                        if new_word == endWord:
                            return ans
                    
                        visited.add(new_word)
                        queue.append(new_word)
            
            
        return 0