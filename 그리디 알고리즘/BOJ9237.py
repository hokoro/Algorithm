import sys
input = sys.stdin.readline

num = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse=True)
count = 0
answer = 0
while True:
    if count < num:
        count += 1

    for i in range(count):
        if nums[i] == 0:
            continue
        else:
            nums[i] -= 1
    answer += 1
    print(f'i : {answer}  / nums : {nums}')
    if nums.count(0) == num:
        break

print(answer)
