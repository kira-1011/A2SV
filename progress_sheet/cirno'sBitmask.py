test_cases = int(input())

for _ in range(test_cases):

    x = int(input())
    mask = 1
    y = mask

    if x == 1:
        y = 3

    elif x & mask:
        y = 1
    
    else:

        while mask & x == 0:
            mask <<= 1

        if x ^ mask <= 0:
            mask += 1
        
        y = mask

    print(y)
