line = input()

line = '0b' + line
data = int(line,2)
answer = oct(data)
answer = answer.replace('0o','')

print(answer)