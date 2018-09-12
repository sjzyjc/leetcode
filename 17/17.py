class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.digit_to_num = {'2':['a', 'b', 'c'], '3':['d','e','f'], '4':['g', 'h', 'i'], '5':['j','k', 'l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        digit_list = list(digits)
        self.ans = []
        self.helper(digit_list, 0, "")
        return self.ans
        
    def helper(self, listt, index, strr):
        if index == len(listt):
            self.ans.append(strr)
            return
            
        for i in self.digit_to_num[listt[index]]:
            self.helper(listt, index + 1, strr + i)
        
        
        