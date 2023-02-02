o = input()

value = int(o,8)


answer = bin(value)

answer = answer.replace('0b' , '')

print(answer)
