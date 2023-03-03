test_cases = int(input())

def getMaxTeams(p, m, max_range):
    
    start = 0
    end = max_range
    max_teams = 0
    
    # check the maximum possible teams that can be formed
    while start <= end:
        
        mid = start + (end - start) // 2
        current_team = (p + m) // 4
        
        if current_team > mid:
            start = mid + 1
            max_teams = mid
        
        elif current_team < mid:
            end = mid - 1
        
        else:
            return mid
        
    return max_teams

for _ in range(test_cases):
    
    # P for programmers and M for mathematicians
    p, m = map(int, input().split())
    
    max_teams = getMaxTeams(p, m, min(p, m))
    print(max_teams)
