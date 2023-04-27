class Solution:

    def bfs(self, rooms):

        queue = deque([0])
        visited_rooms = set([0])

        while queue:

            level_len = len(queue)

            for i in range(level_len):

                key = queue.popleft()

                for next_key in rooms[key]:

                    if next_key not in visited_rooms:
                        visited_rooms.add(next_key)
                        queue.append(next_key)
        
        return visited_rooms

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        # Visit the rooms that have keys
        visited_rooms = self.bfs(rooms)

        # check if we visited all the rooms
        return len(visited_rooms) == len(rooms)
