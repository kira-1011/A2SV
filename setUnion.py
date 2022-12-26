# Enter your code here. Read input from STDIN. Print output to STDOUT
# Receive english subscribers and french subscribers
n = int(input())
english = set(input().split(" "))
b = int(input())
french = set(input().split(" "))

# Take the union of english and french subscribers
both = english.union(french)
total_students = len(both)

# Print the total number of students that subscribed to at least one newspaper
print(total_students)
