# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read inputs
size = input().split(" ")
n = int(size[0])
m = int(size[1])

nums = input().split(" ")
nums = list(map(int, nums))

setA = input().split(" ")
setA = set(map(int, setA))

setB = input().split(" ")
setB = set(map(int, setB))

happiness = 0

#  if i element of set A add 1 to happiness. If i elemt of set B add -1 happiness
for i in nums:
    likes = i in setA
    dislikes = i in setB
    
    happiness += likes
    happiness -= dislikes
    
print(happiness)