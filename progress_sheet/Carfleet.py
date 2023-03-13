class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        arrival_time = []
        mono_stack = []

        # Store position and speed in pairs inorder to sort the cars by position
        pos_speed = list(zip(position, speed))

        # Sort cars in non decreasing order
        pos_speed.sort()

        # calculate arrival time of each car
        for car in pos_speed:
            time = (target - car[0]) / car[1]
            arrival_time.append(time)
        
        # maintain a decreasing monostack based on arrival time to count the number of car fleet
        for time in arrival_time:

            while mono_stack and mono_stack[-1] <= time:
                mono_stack.pop()
                
            mono_stack.append(time)
        
        # return the number of elements remaining in the mono stack meaning the number of car fleet
        return len(mono_stack)
