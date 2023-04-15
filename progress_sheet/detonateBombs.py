class Solution:

    def dfs(self, graph, node, visited):

        visited.add(node)

        for next_node in graph[node]:

            if next_node not in visited:
                self.dfs(graph, next_node, visited)

    def checkDetonation(self, bomb1, bomb2):

        x1, y1, r1 = bomb1
        x2, y2, r2 = bomb2

        distance = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

        return distance <= r1

    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        graph = defaultdict(list)
        b_size = len(bombs)
        max_bombs = 0

        # construct a graph to represent the detonation relation
        for i in range(b_size):
            for j in range(b_size):

                # check if bomb i detonate bomb j
                if self.checkDetonation(bombs[i], bombs[j]):
                    graph[i].append(j)

        # count all the reachable bombs that can be detonated starting from each bomb
        for i in range(b_size):
            
            visited = set()

            self.dfs(graph, i, visited)

            max_bombs = max(max_bombs, len(visited))

        return max_bombs
