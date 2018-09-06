from collections import deque
class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites is None:
            return []

        in_degree = [0 for i in range(numCourses)]
        next_courses = {i: [] for i in range(numCourses)}
        for pre in prerequisites:
            in_degree[pre[0]] += 1
            next_courses[pre[1]].append(pre[0])
        
        queue = deque()
        for key, val in enumerate(in_degree):
            if val == 0:
                queue.append(key)

        processed = []
        while queue:
            course = queue.popleft()

            processed.append(course)
            for next_course in next_courses[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        if len(processed) == numCourses:
            return processed
        else:
            return []