strs = input()

num_sum = 0

for i in range(len(strs)):
    if 65 <= ord(strs[i]) and ord(strs[i]) < 71:
        num = ord(strs[i]) - 55

    else:
        num = int(strs[i])

    num_sum = num_sum + num * (16 ** (len(strs) - i - 1))

print(num_sum)
