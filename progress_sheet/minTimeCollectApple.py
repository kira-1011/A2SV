class Solution:

    def __init__(self):
        self.hasApple = None
        self.min_time = 0
        self.graph = None

    def dfs(self, node, visited):

        visited.add(node)

        for next_node in self.graph[node]:

            if next_node not in visited:
                
                # if there exist an apple on this path add 2 to the total time
               if self.dfs(next_node, visited):

                   # mark the current node true since there is a node having an apple on its path
                   self.hasApple[node] = True
                   self.min_time += 2
        
        return self.hasApple[node]

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.hasApple = hasApple
        self.graph = graph

        self.dfs(0, set())

        return self.min_time
