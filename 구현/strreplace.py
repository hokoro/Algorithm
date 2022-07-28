st = input()
alpha = []
answer = ''
num_sum = 0
for s in st:
    if s.isdigit():
        num_sum += int(s)
        continue
    print(s)
    alpha.append(s)


alpha.sort()

answer = ''.join(alpha)

if num_sum !=0:
    answer = answer + str(num_sum)

print(answer)


