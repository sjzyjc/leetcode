class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ""
        
        if num1 == "0" or num2 == "0":
            return "0"
        
        ans = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                multi = int(num1[i]) * int(num2[j])
                second = i + j + 1
                first = second - 1
                
                tmp_sum = ans[second] + multi
                ans[second] = tmp_sum % 10
                ans[first] += tmp_sum // 10
                
        str_ans = ""
        for index, num in enumerate(ans):
            if index == 0 and num == 0:
                continue
                
            str_ans += str(num)
        
        return str_ans
                
        