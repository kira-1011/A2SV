class Solution:

    def __init__(self):
        self.color = None
        self.graph = None

    # 0 -> white(not visited)   1 -> gray(being processed)    2 -> black(visited)
    def dfsCycle(self, root):

        if self.color[root] == 1:
            return True
        
        if self.color[root] == 2:
            return False
        
        # node is being processed so color it as gray
        self.color[root] = 1

        for neighbour in self.graph[root]:

            if self.dfsCycle(neighbour):
                return True
        
        self.color[root] = 2

        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        self.graph = graph
        self.color = [0 for i in range(len(graph))]

        safe_nodes = []

        for node in range(len(graph)):

            if not self.dfsCycle(node):
                safe_nodes.append(node)
        
        return safe_nodes
        
