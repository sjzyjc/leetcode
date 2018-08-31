class Solution:
    def test(self):
        a = "abc"
        self.change(a)
        print(a)
        left, right = 0, 19
        while left < right:
            left += 1
            print(left)

    def change(self, strr):
        strr = strr + 'd'    


sl = Solution()
print(sl.test())