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

    def findShortestPrefix(self, word):
        tmp = self.trie
        result = ''
        for char in word:
            if '#' in tmp:
                return result

            if char not in tmp:
                return -1

            result += char
            tmp = tmp[char]
            
        return -1        


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for root in dict:
            trie.insert(root)

        word_list = sentence.split(" ")
        for index, word in enumerate(word_list):
            prefix = trie.findShortestPrefix(word)
            if prefix != -1:
                word_list[index] = prefix   

        return " ".join(word_list)     


    


sl = Solution()
print(sl.replaceWords(["rat","cat"], "the rattle is cattle"))