class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        :Time: N
        :Space: 1
        """
        romanValues = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        combinedRoman = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        result = 0
        start = 0
        while (start < len(s)):
            if s[start] not in romanValues:
                return -1

            if s[start:start+2] in combinedRoman:
                result += combinedRoman[s[start:start+2]]
                start += 2
            else:
                result += romanValues[s[start]]
                start += 1

        return result

sl = Solution()
print(sl.romanToInt('III'))
print(sl.romanToInt('IV'))
print(sl.romanToInt('XIV'))
print(sl.romanToInt('CDI'))



