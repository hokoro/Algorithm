people = int(input())

times = list(map(int,input().split()))

Y , M = 0 , 0
for time in times:
    y_count = time // 30
    m_count = time // 60

    Y += (y_count+1) * 10
    M += (m_count+1) * 15


if Y == M:
    print(f'Y M {Y}')

elif Y > M:
    print(f'M {M}')

else:
    print(f'Y {Y}')
