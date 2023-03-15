import sys

input = sys.stdin.readline

angles = [int(input()) for _ in range(3)]

if sum(angles) != 180:
    print('Error')
elif sum(angles) == 180 and len(set(angles)) == 3:
    print('Scalene')
elif sum(angles) == 180 and len(set(angles)) == 2:
    print('Isosceles')
elif angles[0] == angles[1] == angles[2] == 60:
    print('Equilateral')

