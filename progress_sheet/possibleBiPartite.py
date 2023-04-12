class Solution:

    def __init__(self):
        self.group_map = defaultdict(int)

    def dfs(self, graph, person, group):
        
        self.group_map[person] = group

        for neighbour in graph[person]:

            if neighbour not in self.group_map:
                
                is_possible = self.dfs(graph, neighbour, -group)

                if not is_possible:
                    return False
            
            elif group == self.group_map[neighbour]:
                return False
        
        return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        is_possible = True

        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        
        # check any unassigned person
        for i in range(1, n + 1):

            if i not in self.group_map:

                is_possible = self.dfs(graph, i, 1)

                if not is_possible:
                    return False

        return is_possible
