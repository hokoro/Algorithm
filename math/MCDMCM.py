a, b = map(int, input().split())
gcd = 0
lcm = a * b
while True:
    if a % b == 0:
        gcd = b
        break
    else:
        temp = b
        b = a % b
        a = temp

lcm = int(lcm / gcd)
print(gcd)
print(lcm)
