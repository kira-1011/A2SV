class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        friends = []

        # Store numbers from 1 to n
        for num in range(1, n + 1):
            friends.append(num)
        
        index = 0

        # Count the next k friends in the clockwise direction and remove the last friend
        while len(friends) != 1:

            index = (index + (k - 1)) % len(friends)
            friends.pop(index)
            index = index % len(friends)
        
        return friends[0]