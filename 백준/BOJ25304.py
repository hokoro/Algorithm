bilge = int(input())
test_case = int(input())
all_bilge = 0
for _ in range(test_case):
    a, b = map(int, input().split())
    all_bilge += (a * b)

if all_bilge == bilge:
    print("Yes")
else:
    print("No")
