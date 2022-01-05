N,K = map(int,input().split())
coin_list= []
answer = 0
for i in range(N):
    coin = int(input())
    coin_list.append(coin)

coin_list_reversed = reversed(coin_list)

for coin in coin_list_reversed:
    if K >= coin:
        answer = answer + (K // coin)
        K = K % coin


print(answer)

