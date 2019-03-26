from collections import defaultdict
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []
        
        reversed_map = defaultdict(int)
        for index, word in enumerate(words):
            reversed_map[word[::-1]] = index
            
        ans = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                if word[j:] == word[j:][::-1] and word[:j] in reversed_map and reversed_map[word[:j]] != i:
                    ans.append([i, reversed_map[word[:j]]])
                    
            for j in range(1, len(word) + 1):
                if word[:j] == word[:j][::-1] and word[j:] in reversed_map and reversed_map[word[j:]] != i:
                    ans.append([reversed_map[word[j:]], i])
        return ans                    
        