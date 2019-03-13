import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings or not buildings[0]:
            return []
        
        arr = []
        for b in buildings:
            arr.append([b[0], 0, b[2]])
            arr.append([b[1], 1, b[2]])
            
        arr.sort()
        heap = []
        ans = []
        #print(arr)
        for i in arr:
            x = i[0]
            h = i[2]
            is_left = (i[1] == 0)
            
            if is_left:
                if not heap or -heap[0] < h:
                    ans.append([x, h, True])
                
                heapq.heappush(heap, -h)
            else:
                heap.remove(-h)
                if heap:
                    heapq.heapify(heap)
                
                if not heap:
                    ans.append([x, 0, False])
                elif -heap[0] < h: 
                    ans.append([x, -heap[0], False]) 
        
        ret = []
        last_x = last_h = None
        for i in ans:
            x = i[0]
            h = i[1]
            is_left = i[2]
            
            if last_x is None:
                last_x = x
                last_h = h
            elif x == last_x:
                if is_left:
                    last_h = max(last_h, h)
                else:
                    last_h = min(last_h, h)
            else:
                ret.append([last_x, last_h])
                last_x = x
                last_h = h
                
        ret.append([last_x, last_h])
        return ret
                        