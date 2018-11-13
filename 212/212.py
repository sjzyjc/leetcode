DIRECTION = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Trie:
    def __init__(self):
        self.trie = {}
        
    
    def insert(self, word):
        tmp = self.trie
        for char in word:
            if char not in tmp:
                tmp[char] = {}
            
            tmp = tmp[char]
            
        tmp['#'] = True
    
    def isPrefix(self, prefix):
        tmp = self.trie
        for char in prefix:
            if char not in tmp:
                return False
            tmp = tmp[char]
            
        return True
        
    def isWord(self, word):
        return self.isPrefix(word + "#")


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def findWords(self, board, words):
        # write your code here
        if not board or not board[0] or not words:
            return []
        
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        
        ans = []
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited[i][j] = True
                self.dfs(board, i, j, board[i][j], visited, ans)
                visited[i][j] = False
                
        return list(set(ans))
        
    def dfs(self, board, i, j, carry, visited, ans):
        if self.trie.isWord(carry):
            ans.append(carry)
          
        for offset in DIRECTION:
            new_i = i + offset[0]
            new_j = j + offset[1]
            if not (0<= new_i < len(board) and 0 <= new_j < len(board[0])):
                continue

            if visited[new_i][new_j]:
                continue
            
            sub = carry + board[new_i][new_j]
            if not self.trie.isPrefix(sub):
                continue
            
            visited[new_i][new_j] = True
            self.dfs(board, new_i, new_j, sub, visited, ans)
            visited[new_i][new_j] = False
            
                
                
                
