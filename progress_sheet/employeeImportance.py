"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:

    def __init__(self):

        self.total = 0
        self.graph = None

    def dfs(self, employee, visited):

        self.total += self.graph[employee].importance

        visited.add(employee)

        for subordinate in self.graph[employee].subordinates:

            if subordinate not in visited:
                self.dfs(subordinate, visited)

    def getImportance(self, employees: List['Employee'], id: int) -> int:

        graph = defaultdict(list)
        importance_map = defaultdict(int)

        # build employee relationship graph using adjacency list
        for employee in employees:
            graph[employee.id] = employee
        
        self.graph = graph
        
        self.dfs(id, set())

        return self.total
