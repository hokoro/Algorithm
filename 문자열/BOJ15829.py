
n = int(input())
s = input()
answer = 0
s_list = list(s)

for i in range(len(s_list)):
    answer = answer + (ord(s_list[i]) % 97 + 1) * (31 ** i)

print(answer % 1234567891)