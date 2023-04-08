class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        for vertex in graph:

            if len(graph[vertex]) == len(graph) - 1:
                return vertex
