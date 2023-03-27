def findWinners(players, left, right, k):

    if left == right:
        return [left]

    mid = left + (right - left) // 2

    left_winners = findWinners(players, left, mid, k)
    right_winners = findWinners(players, mid + 1, right, k)

    current_winners = []

    l_ptr = 0
    r_ptr = 0

    # compare the left winners with the right winners in a sorted manner
    while l_ptr < len(left_winners) and r_ptr < len(right_winners):

        diff = abs(players[left_winners[l_ptr]] - players[right_winners[r_ptr]])

        if players[left_winners[l_ptr]] <= players[right_winners[r_ptr]]:

            # check if player on the left have the chance to win

            # if the left pointer lagged behind the right pointer 
            # it means the player had won against some player before 
            if diff <= k or l_ptr < r_ptr:
                current_winners.append(left_winners[l_ptr])
            
            l_ptr += 1

        else:

            
            # check if player on the left have the chance to win

            # if the right pointer lagged behind the left pointer 
            # it means the player had won against some player before 

            if diff <= k or l_ptr > r_ptr:
                current_winners.append(right_winners[r_ptr])

            r_ptr += 1
    
    # append remaining winners
    while l_ptr < len(left_winners):
        current_winners.append(left_winners[l_ptr])
        l_ptr += 1
    
    while r_ptr < len(right_winners):
        current_winners.append(right_winners[r_ptr])
        r_ptr += 1

    return current_winners

def main():

    n, k = map(int, input().split())
    size = 2 ** n
    players = list(map(int, input().split()))

    winners = findWinners(players, 0, size - 1 , k)
    winners = [winner + 1 for winner in winners]

    print(*sorted(winners))

main()
