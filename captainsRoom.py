# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_number = input().split(" ")
room_number = list(map(int, room_number))

captain_room_number = 0
occurence = {}

for num in room_number:
    occurence[num] = occurence.get(num, 0) + 1
    
for key, value in occurence.items():
    if value == 1:
        captain_room_number = key
        break

print(captain_room_number)