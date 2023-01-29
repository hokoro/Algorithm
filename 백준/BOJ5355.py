test_case = int(input())

answers = []
for _ in range(test_case):
    operation = input()
    operation = operation.split(' ')
    nums = float(operation[0])
    for op in operation[1:]:
        if op == '@':
            nums = nums * 3
        elif op == '%':
            nums = nums + 5
        elif op == '#':
            nums = nums - 7
    answers.append(float(nums))

for ans in answers:
    print("{:.2f}".format(ans), end='\n')
