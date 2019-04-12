class Trie:
    def __init__(self):
        self.trie = {}
        
    def insert(self, word):
        tmp = self.trie
        for charr in word:
            if charr not in tmp:
                tmp[charr] = {}
                
            tmp = tmp[charr]
            
        tmp['#'] = True
        
            
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict:
            return []
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word[::-1])
        
        dp = [[] for _ in range(len(s) + 1)]
        dp[0].append('')
        
        for i in range(1, len(s) + 1):
            tmp = trie.trie
            for j in range(i - 1, -1, -1):
                charr = s[j : j + 1]
                if charr not in tmp:
                    break
                    
                tmp = tmp[charr]
                if '#' in tmp:
                    for item in dp[j]:
                        if item:
                            dp[i].append(item + ' ' + s[j : i])
                        else:
                            dp[i].append(s[j : i])
                        
           
        return dp[-1]
        