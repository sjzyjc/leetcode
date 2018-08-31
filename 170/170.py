class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.map:
            self.map[number] = 1
        else:
            self.map[number] += 1  
        
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for i in self.map:

            if i != value / 2 and value - i in self.map:
                return True
            elif i == value / 2 and self.map[i] > 1:
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
obj.add(3)
obj.add(3)
obj.add(1)

print(obj.find(6))
print(obj.find(4))
print(obj.find(2))