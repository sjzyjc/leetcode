# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import heapq
class Solution:
    def findSecretWord(self, wordlist, master):
        heap = []
        heap = self.calZeroMatches(wordlist)
        res = -1
        while res != 6:
            c, word = heapq.heappop(heap)
            res = master.guess(word)
            self.update(res, word, heap)
    
    def calZeroMatches(self, wordlist):
        heap = []
        
        for word1 in wordlist:
            count = 0
            for word2 in wordlist:
                if word1 == word2:
                    continue
                    
                if self.match(word1, word2) == 0:
                    count += 1
                    
            heapq.heappush(heap, (count, word1))
            
        return heap
                    
                
    def update(self, res, word, heap):
        for item in heap:
            if self.match(word, item[1]) != res:
                heap.remove(item)
                
        heapq.heapify(heap)
                
            
    def match(self, word, guess):
        count = 0
        for index in range(len(word)):
            if word[index] == guess[index]:
                count += 1
        return count