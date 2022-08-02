num = int(input())

primes = []

i = 2
while num != 1:
    if num % i == 0:
        primes.append(i)
        num = num / i
    else:
        i = i + 1

for prime in primes:
    print(prime, end='\n')
