# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = input().split(" ")
n = int(n)
m = int(m)

group_a = defaultdict(list)

for i in range(n):
    letter = input()
    group_a[letter].append(str(i + 1))
    
for i in range(m):
    letter = input()
    
    if letter in group_a:
        print(" ".join(group_a[letter]))
    else:
        print(-1)
