from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if not wordList or len(wordList) == 0 or endWord not in wordList:
            return 0
        wordListSet = set(wordList)
        wordListSet.add(beginWord)
        wordListSet.add(endWord)
        
        queue = deque()
        queue.append((beginWord, 0))
        while queue:
            word, step = queue.popleft()
            
            if word == endWord:
                return step + 1
            for index, char in enumerate(word):
                for alphebet in range(ord('a'), ord('z') + 1):
                    if chr(alphebet) != char:
                        new_word = word[:index] + chr(alphebet) + word[index+1:]
                        if new_word in wordListSet:
                            queue.append((new_word, step + 1))
                            wordListSet.remove(new_word)

        return 0