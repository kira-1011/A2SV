# Enter your code here. Read input from STDIN. Print output to STDOUT

blocks = []
results = []

test_case = int(input())

for i in range(test_case):
    n = int(input())
    blocks = input().split(" ")
    blocks = list(map(int, blocks))
    
    left = 0
    right = n - 1
    top = max(blocks[left], blocks[right])
    current = 0
    result = "Yes"
    
    while left < right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1
        
        if current > top:
            result = "No"
            break
        
        top = current

    results.append(result)

    
for i in results:
    print(i)