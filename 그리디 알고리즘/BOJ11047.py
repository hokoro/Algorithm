n,k = map(int,input().split())
answer = 0
coin_list = []
for i in range(n):
    coin = int(input())
    coin_list.append(coin)


coin_list.sort(reverse=True)


for coin in coin_list:
    if k < coin:
        continue

    else:
        answer += (k//coin)
        k = k % coin



print(answer)