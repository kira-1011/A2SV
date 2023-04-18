def main():

    n = int(input())
    nums = list(map(int, input().split()))

    modified_nums = list(filter(lambda x : x % 2 == 0, nums))

    if len(modified_nums) == len(nums) or len(modified_nums) == 0:
        print(*nums)
        return

    print(*sorted(nums))

main()
