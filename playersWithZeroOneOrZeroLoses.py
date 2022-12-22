class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        # Initialize dictionary that contains players lose count
        lose_count = {}
        answer = [[],[]]

        # Count the number of times a player lost
        for players in matches:
            loser = players[1]
            winner = players[0]

            lose_count[loser] = lose_count.get(loser, 0) + 1
            lose_count[winner] = lose_count.get(winner, 0)

        # Check players that have not lost any matches or lost exactly one match
        for player in lose_count:
            count = lose_count[player]
            if count == 0:
                answer[0].append(player)
            elif count == 1:
                answer[1].append(player)
        
        # Sort answer
        answer[0].sort()
        answer[1].sort()

        return answer