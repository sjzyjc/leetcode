class Solution(object):
    def crackSafe(self, n, k):
        if n == 1:
            return "".join([str(i) for i in range(k)])
        
        seen = set()
        ans = []
        def dfs(node):
            for x in range(k):
                x = str(x)
                edge = node + x
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    #ans.append(x)  
                    
            #all edge are seen
            ans.append(node)
                    
        dfs("0" * (n-1))
        ans = ans[::-1]
        
        ret = ans[0]   
        for item in ans[1:]:
            ret += item[-1]
    
        return ret