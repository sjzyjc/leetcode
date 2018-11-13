
class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        O(N)
        O(N)
        """
        if not pid or not ppid or kill not in pid:
            return []
        
        tree_map = {i:[] for i in ppid}
        
        for index, value in enumerate(pid):
            tree_map[ppid[index]].append(value)
            
        stack = [kill]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node)
            if node not in tree_map:
                continue
            
            for child in tree_map[node]:
                stack.append(child)
                
        return ans
            
        