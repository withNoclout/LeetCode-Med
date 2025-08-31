"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        mp = { e.id : e for e in employees} 

        total = 0 
        stack = [id] 
        while stack : 
            eid = stack.pop()
            emp = mp[eid]
            total += emp.importance
            for sub in emp.subordinates:
                stack.append(sub)
        return total
