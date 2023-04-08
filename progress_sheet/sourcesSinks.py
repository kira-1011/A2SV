n = int(input())
source = []
sink = []
col_sum = [0] * n

for i in range(n):
    row = list(map(int, input().split()))

    # check for sinks
    row_sum = sum(row)

    if row_sum == 0:
        sink.append(i + 1)
    
    # accumulate sum to check sources
    for r in range(len(row)):
        col_sum[r] += row[r]

for c in range(len(col_sum)):
    if col_sum[c] == 0:
        source.append(c + 1)

print(len(source), *source)
print(len(sink), *sink)
