class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.hashmap = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hashmap:
            self.list.append(val)
            self.hashmap[val] = len(self.list) - 1
            return True
        return False
    
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hashmap:
            index = self.hashmap[val]
            last_val = self.list[-1]
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            self.hashmap[last_val] = index
            
            del self.hashmap[val]
            self.list.pop()
            return True
        
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.list[random.randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()