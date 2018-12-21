class UnionFind:
    def __init__(self):
        self.p = [i for i in range(10001)]
        self.size = [1 for _ in range(10001)]
        
    def find(self, i, j):
        return self.root(i) == self.root(j)
    
    def union(self, i, j):
        i = self.root(i)
        j = self.root(j)
        
        if self.size[i] < self.size[j]:
            self.p[i] = j
            self.size[j] += self.size[i]
        else:
            self.p[j] = i
            self.size[i] += self.size[j]
        
    def root(self,i):
        while i != self.p[i]:
            self.p[i] = self.p[self.p[i]]
            i = self.p[i]
            
        return i

    
class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        if not accounts:
            return []
        
        uf = UnionFind()
        hash_map = {}
        eid = 0
        for account in accounts:
            first_email = account[1]
            if first_email not in hash_map:
                hash_map[first_email] = eid
                eid += 1
                    
            for index in range(2, len(account)):
                second_email = account[index]

                if second_email not in hash_map:
                    hash_map[second_email] = eid
                    eid += 1
                
                uf.union(hash_map[first_email], hash_map[second_email])
                
        root_map = {}
        ans = []
        for account in accounts:            
            root = uf.root(hash_map[account[1]])
            if root in root_map:
                root_map[root][1].extend(account[1:])
            else:
                root_map[root] = (account[0], account[1:])
        
        for i in root_map:
            row = []
            row.append(root_map[i][0])
            
            emails = list(set(root_map[i][1]))
            emails.sort()
            row.extend(emails)
            ans.append(row)
        
        return ans
                    
                    
                