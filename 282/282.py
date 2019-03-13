class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num or target is None:
            return []
        
        ans = []
        def helper(start_index, cur_val, last_expr, carry):
            #print(carry)
            if start_index == len(num):
                if cur_val == target:
                    ans.append(carry)
                return
        
            for i in range(start_index, len(num)):
                if len(num[start_index: i + 1]) > 1 and num[start_index] == '0':
                    continue
                
                operand = int(num[start_index: i + 1])
                helper(i + 1, cur_val + operand, operand, carry + '+' + str(operand))
                helper(i + 1, cur_val - operand, -operand, carry + '-' + str(operand))
                helper(i + 1, cur_val - last_expr + last_expr * operand, last_expr * operand, carry + '*' + str(operand))
                
        
        for i in range(len(num)):
            if len(num[: i + 1]) > 1 and num[0] == '0':
                    continue
            operand = int(num[: i + 1])
            helper(i+1, operand, operand, num[: i + 1])
        
        return ans
                
