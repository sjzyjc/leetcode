from collections import defaultdict, deque
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not wordList or endWord not in wordList:
            return []
        
        wordList.append(beginWord)
        indexes = defaultdict(list)
        self.buildIndexes(wordList, indexes)
        
        distances = {}
        self.bfs(endWord, distances, wordList, indexes)
        
        if beginWord not in distances:
            return []
        
        ans = []
        self.dfs(beginWord, endWord, distances, wordList, indexes, [beginWord], ans)
        return ans
    
    def buildIndexes(self, wordList, indexes):
        for word in wordList:
            for index, char in enumerate(word):
                indexes[word[:index] + '%' + word[index + 1:]].append(word)
    
    def findNextWords(self, word, wordList, indexes):
        ans = []
        for index, char in enumerate(word):
            ans.extend(indexes.get(word[:index] + '%' + word[index + 1:], []))
        
        return ans
    
    def bfs(self, end, distances, wordList, indexes):
        queue = deque([end])
        distances[end] = 0
        
        while queue:
            word = queue.popleft()

            for next_word in self.findNextWords(word, wordList, indexes):
                if next_word not in distances:
                    distances[next_word] = distances[word] + 1
                    queue.append(next_word)
    
    def dfs(self, current, end, distances, wordList, indexes, path, ans):
        if current == end:
            ans.append(path + [])
            return
        
        for next_word in self.findNextWords(current, wordList, indexes):
            if distances[next_word] != distances[current] - 1:
                continue
            
            path.append(next_word)
            self.dfs(next_word, end, distances, wordList, indexes, path, ans)
            path.pop()
            
                
            
            