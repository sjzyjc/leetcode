class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ""
        res, pos = self.helper(0, s)
        return res
        
    def helper(self, pos, s):
        res = ""
        number = 0
        while pos <len(s):
            if s[pos].isdigit():
                number = number * 10 + int(s[pos])
            elif s[pos] == "[":
                substring, pos = self.helper(pos + 1, s)
                res += substring * number
                number = 0
            elif s[pos] == "]":
                return res, pos
            else:
                res += s[pos]
            pos += 1
        return res, pos