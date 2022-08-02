text = input()

alpha = [0] * 26


for i in range(len(text)):
    index = ord(text[i]) % 97

    alpha[index] += 1

for a in alpha:
    print(a,end=" ")
