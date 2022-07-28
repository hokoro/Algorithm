basic_channel = 100

channel = input()

broken_count = int(input())

broken_button = list(map(int, input().split()))

#button_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-']

answer = 0

for c in channel:
    if basic_channel == int(channel):
        break
    num = int(c)
    if num in broken_button:
        while True:
            num = num - 1
            if num not in broken_button:
                break
    else:
        answer += 1

    print(num)

print(answer)