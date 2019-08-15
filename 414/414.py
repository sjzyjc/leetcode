INT_MIN = -(1 << 31) - 1
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        first_large = second_large = third_large = INT_MIN
        for num in nums:
            if num == first_large or num == second_large or num == third_large:
                continue
                
            if num > first_large:
                first_large, second_large, third_large = num, first_large, second_large
            elif num > second_large:
                second_large, third_large = num, second_large
            elif num > third_large:
                third_large = num
                 
        return third_large if third_large > INT_MIN else max(first_large, second_large)