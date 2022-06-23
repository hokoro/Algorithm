room = input()
room_list = list(room)
number_set = [0 for i in range(10)]
count = 1

print(room_list)
print(count)

for r in room_list:
    number_set[int(r)] = number_set[int(r)] + 1

print(number_set)
