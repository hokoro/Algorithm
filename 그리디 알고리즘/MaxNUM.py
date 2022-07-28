data = input()

result = int(data[0])

for s in data[0:]:
    num = int(s[0])

    if num <=1 or result <=1:
        result += num

    else:
        result *= num

print(result)