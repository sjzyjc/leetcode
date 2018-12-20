class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0
        
        cat = set()
        i = j = 0
        counter = 1
        cat.add(tree[0])
        
        ans = 0
        for j in range(1, len(tree)):
            if len(cat) == 2 and tree[j] not in cat:
                ans = max(ans, j - i)
                i = j - counter
                cat = set([tree[j - 1], tree[j]])
                
            if tree[j] != tree[j - 1]:
                counter = 0
                
            cat.add(tree[j])
            counter += 1
            
        return max(ans, j - i + 1)
            
                    
        