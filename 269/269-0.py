from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        in_degree = {}
        graph = defaultdict(set)
        
        for index in range(len(words)):
            word1 = words[index]
            ptr1 = 0
            
            while ptr1 < len(word1):
                if word1[ptr1] not in in_degree:
                    in_degree[word1[ptr1]] = 0
                ptr1 += 1
                    
            if index + 1 >= len(words):
                continue
                
            word2 = words[index + 1]
            ptr1 = ptr2 = 0
            while ptr1 < len(word1) and ptr2 < len(word2):
                char1 = word1[ptr1]
                char2 = word2[ptr2]
                
                if char1 not in in_degree:
                    in_degree[char1] = 0
                    
                if char2 not in in_degree:
                    in_degree[char2] = 0
                
                if char1 == char2:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        in_degree[char2] += 1
                    break
                    
            while ptr2 < len(word2):
                if word2[ptr2] not in in_degree:
                    in_degree[word2[ptr2]] = 0
                
                ptr2 += 1
            
            #print(in_degree, graph)
            
        
        queue = deque([])
        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)
        
        ans = ""
        #print(in_degree, graph)
        while queue:
            #print(queue)
            node = queue.popleft()
            ans += node
            
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        #if len(ans) < len
        return ans if len(ans) == len(in_degree) else ""
        
        