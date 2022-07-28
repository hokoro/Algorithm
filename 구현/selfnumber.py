not_self_number = []

for i in range(1, 10001):
    if i not in not_self_number:
        print(i)
    num = str(i)
    oper = 0
    for n in str(i):
        oper = oper + int(n)

    oper+=i
    not_self_number.append(oper)