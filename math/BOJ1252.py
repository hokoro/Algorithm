a,b = map(str,input().split())

a = "0b" + a
b = "0b" + b

int_a = int(a,2)
int_b = int(b,2)


answer = int_a + int_b

print(bin(answer)[2:])
