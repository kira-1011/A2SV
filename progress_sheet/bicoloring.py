from collections import defaultdict

color_map = defaultdict(int)

def dfs(graph, node, color):

    if node in color_map:
         
        if color != color_map[node]:
            return False
        
        return True
    
    color_map[node] = color

    for neighbour in graph[node]:
            
        bicolourable = dfs(graph, neighbour, -color)

        if not bicolourable:
            return False
    
    return True

n = 1

while n:
    
    n = int(input())

    if n != 0:
        
        n_edge = int(input())

        graph = defaultdict(list)
        color_map = defaultdict(int)

        for _ in range(n_edge):

            node1, node2 = map(int, input().split())

            # construct the graph
            graph[node1].append(node2)
            graph[node2].append(node1)
        

        bicolourable = dfs(graph, 1, 1)

        if bicolourable:
            print("BICOLOURABLE.")

        else:
            print("NOT BICOLOURABLE.")
