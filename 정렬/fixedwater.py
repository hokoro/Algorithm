N, L = map(int,input().split())
locationList = list(map(int,input().split()))
locationList.sort()

tape = 1
start = locationList[0]
end = start + L - 0.5
for i in locationList:
    if end >= i:
        continue
    else:
        tape += 1
        end = i + L - 0.5

print(tape)