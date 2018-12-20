from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word_indices = defaultdict(list)
        for index, word in enumerate(words):
            self.word_indices[word].append(index)
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.word_indices[word1]
        list2 = self.word_indices[word2]
        
        ptr1 = ptr2 = 0
        ans = (1 << 31) - 1
        while ptr1 < len(list1) and ptr2 < len(list2):
            while ptr1 < len(list1) and list1[ptr1] < list2[ptr2]:
                ptr1 += 1
            
            if 0 < ptr1 <= len(list1):
                ans = min(ans, list2[ptr2] - list1[ptr1 - 1])
            
            if ptr1 < len(list1):
                ans = min(ans, list1[ptr1] - list2[ptr2])
            
            ptr2 += 1
            
        return ans
            


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)