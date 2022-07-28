count = 0
for i in range(8):
    strs = input()
    for j in range(8):
        if j % 2 == 0 and strs[j] == 'F':
            count += 1
print(count)
