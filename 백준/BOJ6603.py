from itertools import combinations

while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    cases = list(combinations(nums[1:], 6))

    for case in cases:
        for i in range(len(case)):
            print(case[i], end=' ')
        print()
    print()



