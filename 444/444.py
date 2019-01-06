class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if not seqs and not org:
            return True
        
        if seqs is not None:
            for seq in seqs:
                if not seq:
                    seqs.remove(seq)
                    
        if not seqs or not seqs[0] or not org:
            return False
        
        
        org_set = set(org)
        in_degree = [0 for _ in range(len(org))]
        graph = collections.defaultdict(list)
        for seq in seqs:
            if len(seq) == 1:
                if seq[0] not in org_set:
                    return False
                
            for index in range(len(seq) - 1):
                prev = seq[index]
                nextt = seq[index + 1]
                
                if prev not in org_set or nextt not in org_set:
                    return False
                
                graph[prev].append(nextt)
                in_degree[nextt - 1] += 1
        
        queue = collections.deque([])
        for index, val in enumerate(in_degree):
            if val == 0:
                queue.append(index + 1)
                
        if len(queue) == 0:
            return False
        
        ans = []
        while queue:
            if len(queue) > 1:
                return False
            
            node = queue.popleft()
            ans.append(node)
            for nei in graph[node]:
                in_degree[nei - 1] -= 1
                if in_degree[nei - 1] == 0:
                    queue.append(nei)
        
        print(ans)
        return ans == org
            