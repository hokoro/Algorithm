call_count = [0] * 10000

n = int(input())

call_list = list(map(int,input().split()))


for call in call_list:
    call_count[call-1] = call_count[call-1] + 1


for call_c in call_count[:24]:
    print(call_c , end=' ')