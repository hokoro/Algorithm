dices = list(map(int,input().split()))
price = 0
same_count = 1
check_dice = []
same_dice = []
for dice in dices:
    if dice in check_dice:
        same_count += 1
        same_dice.append(dice)
    else:
        check_dice.append(dice)
        continue



if same_count ==1:
    price = max(dices) * 100

elif same_count == 2:
    price = 1000 + (same_dice[0]) * 100

else:
    price = 10000 + (same_dice[0]) * 1000


print(price)