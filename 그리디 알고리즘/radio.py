a, b = map(int, input().split())
n = int(input())
count = 0
channelmarks = [int(input()) for _ in range(n)]

channel_dif = [abs(a - b)]

for channel in channelmarks:
    channel_dif.append(abs(channel -b))

channel_index = channel_dif.index(min(channel_dif))

if channel_index == 0:
    count += channel_dif[channel_index]

else:
    count = count + (1 + channel_dif[channel_index])


print(count)