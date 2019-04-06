from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.idx_map = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        ans = False
        if val not in self.idx_map:
            ans = True
            
        self.arr.append(val)
        self.idx_map[val].add(len(self.arr) - 1)
        return ans
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.idx_map:
            return False
        
        last_val = self.arr[-1]
        
        if last_val == val:
            self.idx_map[val].remove(len(self.arr) - 1)
        else:
            idx = next(iter(self.idx_map[val]))
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        
            self.idx_map[val].remove(idx)
            self.idx_map[last_val].remove(len(self.arr) - 1)
            self.idx_map[last_val].add(idx)
        
        if len(self.idx_map[val]) == 0:
            del self.idx_map[val]
        
        self.arr.pop()
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()