n = int(input())

call_list = list(map(int,input().split()))

for call in call_list[::-1]:
    print(call , end = ' ')