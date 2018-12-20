class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word
    

from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words or k <= 0:
            return []
        
        count = defaultdict(int)
        for word in words:
            count[word] += 1
        
        heap = []
        for key in count:
            heapq.heappush(heap, Word(count[key], key))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap).word)
        
        return ans[::-1]