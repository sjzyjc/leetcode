from collections import deque
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        T: V+E
        S: V^2
        """
        if not prerequisites or not prerequisites[0]:
            return True
        next_course = {i:[] for i in range(numCourses)}
        degree = [0 for i in range(numCourses)]
        
        for pre in prerequisites:
            degree[pre[0]] += 1
            next_course[pre[1]].append(pre[0])
            
        queue = deque()
        processed = []
        for key, value in enumerate(degree):
            if value == 0:
                queue.append(key)
        
        while queue:
            course = queue.popleft()
            if course is None:
                continue
                
            processed.append(course)
            for nextt in next_course[course]:
                degree[nextt] -= 1
                if degree[nextt] == 0:
                    queue.append(nextt)

        return len(processed) == numCourses


 

 