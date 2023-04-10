class Solution:

    def __init__(self):

        self.graph = None

    def dfs(self, node, visited):

        visited.add(node)

        for neighbour in self.graph[node]:

            if neighbour not in visited:
                self.dfs(neighbour, visited)
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        province = 0
        graph = defaultdict(list)
        visited = set()

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                
                if isConnected[row][col] == 1:
                    graph[row + 1].append(col + 1)
        
        self.graph = graph

        for city in graph:

            if city not in visited:
                province += 1
                self.dfs(city, visited)

        return province
