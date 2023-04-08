n = int(input())

roads = 0

for i in range(n):
    row = list(map(int, input().split()))
    roads += sum(row)

print(roads // 2)
