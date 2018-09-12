class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):

            a[i:i+k] = self.reverse(a[i:i+k])
            
        return "".join(a)
    
    def reverse(self, listt):
        left, right = 0, len(listt) - 1
        while left <= right:
            listt[left], listt[right] = listt[right], listt[left]
            left += 1
            right -= 1
            
        return listt