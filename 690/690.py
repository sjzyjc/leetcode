
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
from collections import deque
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if not employees:
            return 0

        queue = deque([self.getEmployeeById(employees, id)])
        importance = 0
        while queue:
            employee = queue.popleft()
            
            if not employee:
                continue
            
            importance += employee.importance
            for sub_id in employee.subordinates:
                queue.append(self.getEmployeeById(employees, sub_id))

        return importance

    def getEmployeeById(self, employees, id):
        for employee in employees:
            if employee.id == id:
                return employee
        
        return None
        