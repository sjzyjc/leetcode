OFFSETS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
class Trie:
    def __init__(self):
        self.trie = {}
        
    def getTrie(self):
        return self.trie
    
    def insert(self, word):
        tmp = self.trie
        for char in word:
            if char not in tmp:
                tmp[char] = {}
            
            tmp = tmp[char]
            
        tmp['#'] = True
        
    def isPrefix(self, target):
        tmp = self.trie
        for char in target:
            if char not in tmp:
                return False
            
            tmp = tmp[char]
            
        return True
    
    def isWord(self, target):
        self.isPrefix(self, target + '#')
                
        
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0] or not words:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
         
        ans = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.search(board, i, j, trie.getTrie(), ans, [])
                
        return list(set(ans))
    
    def search(self, board, i, j, trie, ans, carry):            
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] not in trie:
            return
        
        orig_char = board[i][j]
        board[i][j] = 0
        carry.append(orig_char)
        tmp = trie[orig_char]
        if '#' in tmp:
            ans.append("".join(carry))
        
        for offset in OFFSETS:
            self.search(board, i + offset[0], j + offset[1], tmp, ans, carry)
            
        board[i][j] = orig_char
        carry.pop()
            
                
        