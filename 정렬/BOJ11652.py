import sys
test_case = int(sys.stdin.readline())

nums_dict = dict()

for _ in range(test_case):
    num = int(sys.stdin.readline())
    nums_dict[num] = nums_dict.setdefault(num,0) + 1

result = sorted(nums_dict.items(),key = lambda x : (-x[1],x[0]))
print(result[0][0])


