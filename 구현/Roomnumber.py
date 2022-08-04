room = input()
room_list = list(room)
number_set = [0 for i in range(10)]


for r in room_list:
    number_set[int(r)] = number_set[int(r)] + 1

if (number_set[6] + number_set[9]) % 2 ==0:
    sixornine = (number_set[6] + number_set[9]) // 2
else:
    sixornine = (number_set[6] + number_set[9]) // 2 +1
number_set[6] = sixornine
number_set[9] = sixornine

print(max(number_set))
