test = list(map(int, input().split()))
cheseset = [1, 1, 2, 2, 2, 8]

for chese , t in zip(cheseset,test):
    print(chese - t , end = ' ')

