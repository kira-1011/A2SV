from collections import defaultdict

graph = defaultdict(list)

def addEdge(u, v):
    graph[u].append(v)
    graph[v].append(u)

def vertex(u):
    return graph[u]

n = int(input())
k = int(input())

for _ in range(k):
    ops = list(map(int, input().split()))

    if ops[0] == 1:
        addEdge(ops[1], ops[2])
    
    elif ops[0] == 2:
        print(*vertex(ops[1]))
