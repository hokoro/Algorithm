import sys
D1,D2,D3 = map(int,sys.stdin.readline().split())

dice_dict = dict()

for i in range(1,D1+1):
    for j in range(1,D2+1):
        for k in range(1,D3+1):
            key = i+j+k
            dice_dict[key] = dice_dict.setdefault(key,0) + 1


keys = list(dice_dict.keys())
values = list(dice_dict.values())

print(keys[values.index(max(values))])