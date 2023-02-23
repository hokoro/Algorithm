import sys

input = sys.stdin.readline
score_dict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}

answer = 0
point_sum = 0
for _ in range(20):
    sub, point, score = map(str, input().split())
    score = score.replace('\n','')
    if score != 'P':
        answer += (float(point) * score_dict[score])
        point_sum += float(point)

print("{:.6f}".format(answer / point_sum))
