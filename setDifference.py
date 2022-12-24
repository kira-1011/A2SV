# Enter your code here. Read input from STDIN. Print output to STDOUT
english_len = int(input())
english = set(input().split(" "))
french_len = int(input())
french = set(input().split(" "))

only_english = english.difference(french)
print(len(only_english))
