class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseTable = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = set()
        for word in words:
            morseCode = ''
            for c in word:
                morseCode += morseTable[ord(c) - ord('a')]
            result.add(morseCode)
        return len(result)

sl = Solution()
print(sl.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))     
            