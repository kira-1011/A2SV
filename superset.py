# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = input().split(" ")
set_a = set(map(int, set_a))
n = int(input())

isSuperSet = True

for i in range(n):
    set_b = input().split(" ")
    set_b = set(map(int, set_b))
    
    isSuperSet = set_a.issuperset(set_b)

print(isSuperSet)
