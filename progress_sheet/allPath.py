class Solution:

    def __init__(self):

        self.paths = []
        self.graph = None
        self.destination = 0

    def dfs(self, node, curr_path):

        curr_path.append(node)

        if node == self.destination:
            self.paths.append(curr_path.copy())


        for neighbour in self.graph[node]:
            self.dfs(neighbour, curr_path)
        
        curr_path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        self.graph = graph
        self.destination = len(graph) - 1

        self.dfs(0, [])

        return self.paths
