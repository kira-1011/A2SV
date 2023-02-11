class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        size1, size2 = len(players), len(trainers)
        player = 0
        trainer = 0
        match = 0

        # Sort
        players.sort()
        trainers.sort()

        # find players and trainers that can match
        while player < size1 and trainer < size2:

            if players[player] <= trainers[trainer]:
                match += 1
                player += 1
            
            trainer += 1

        return match 
