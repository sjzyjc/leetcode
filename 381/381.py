class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.list = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        is_not_contained = False
        if val not in self.map:
            self.map[val] = set()
            is_not_contained = True
        
        self.map[val].add(len(self.list))
        self.list.append(val)
        return is_not_contained
        
            
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.map:
            index = next(iter(self.map[val]))
            last_num = self.list[-1]
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            
            self.map[val].remove(index)
            self.map[last_num].add(index)
            self.map[last_num].remove(len(self.list) - 1)
            
            self.list.pop()
            if len(self.map[val]) == 0:
                del self.map[val]
            
            return True
        
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()