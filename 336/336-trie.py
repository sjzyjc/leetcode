class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word_index, word):
        tmp = self.trie
        for index, char in enumerate(word):
            if char not in tmp:
                tmp[char] = {}
            
            if '#' not in tmp:
                tmp['#'] = []
                
            if word[index:] == word[index:][::-1]:
                tmp['#'].append(word_index)
                
            tmp = tmp[char]
                
        if '$' not in tmp:
            tmp['$'] = []
            
        if '#' not in tmp:
            tmp['#'] = []
            
        tmp['$'].append(word_index)
        tmp['#'].append(word_index)
        
    def search(self, word, symbol):
        ans = []
        tmp = self.trie
        for charr in word:
            if charr not in tmp:
                return ans
            
            tmp = tmp[charr]
            
        if symbol in tmp:
            ans.extend(tmp[symbol])
            
        return ans            

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []
        
        trie = Trie()
        for index, word in enumerate(words):
            trie.insert(index, word[::-1])
            
        ans = []
        for w_index, word in enumerate(words):
            match = trie.search(word, '#')
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    match.extend(trie.search(word[:i], '$'))
        
            for j in match:
                if j == w_index: continue
                ans.append([w_index, j])
                
        return ans