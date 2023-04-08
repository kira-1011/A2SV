from collections import defaultdict

graph = defaultdict(list)

n = int(input())

for i in range(n):

    row = list(map(int, input().split()))

    for c in range(len(row)):

        if row[c] == 1:
            graph[i + 1].append(c + 1)

for vertex in graph:
    print(len(graph[vertex]), *graph[vertex])
