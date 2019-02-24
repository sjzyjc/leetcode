import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        
        arr = []
        hash_map = {}
        for b in buildings:
            #point, height, is_left
            arr.append((b[0], b[2], 1))
            arr.append((b[1], b[2], 0))
            hash_map[(b[1], b[2])] = b[0]
            
        arr.sort()
        heap = []
        ans = []
        
        for i in arr:
            #print(heap)
            point = i[0]
            h = i[1]
            is_left = i[2]
            if not heap:
                ans.append([point, h, is_left])
                heapq.heappush(heap, (-h, point))
                
            else:
                if is_left == 1:
                    if -heap[0][0] < h:
                        ans.append([point, h, 1])
                    
                    heapq.heappush(heap, (-h, point))
                    
                else:
                    left_point = hash_map[(point, h)]
                    heap.remove((-h, left_point))
                    if not heap:
                        ans.append([point, 0, 0])
                    else:
                        heapq.heapify(heap)
                        if -heap[0][0] < h:
                            ans.append([point, -heap[0][0], 0])
                            
            ret = []
            cur_p = ans[0][0]
            cur_ans = ans[0][1]
            for index in range(len(ans)):
                p, h, is_left = ans[index][0], ans[index][1], ans[index][2] == 1
                if p == cur_p:
                    if is_left:
                        cur_ans = max(cur_ans, h)
                    else:
                        cur_ans = min(cur_ans, h)
                        
                else:
                    if ret and cur_ans == ret[-1][1] :
                        cur_p = p
                        cur_ans = h
                        continue
                        
                    ret.append([cur_p, cur_ans])
                    cur_p = p
                    cur_ans = h
                        
                    
        ret.append([cur_p, cur_ans])               
        return ret
                        
                        
            
            