def euclid(a, b):
    if a % b == 0:
        return b

    return euclid(b, a % b)


print(int(72*30/euclid(72,30)))

