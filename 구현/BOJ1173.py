import sys

if __name__ == '__main__':
    N, m, M, T, R = map(int, sys.stdin.readline().split())
    minute, ex_minute = 0, 0
    pulse = m

    while ex_minute < N:
        # 운동을 할 수 없는 경우
        if m + T > M:
            break
        # 운동
        if pulse + T <= M:
            pulse += T
            ex_minute += 1
        # 휴식
        else:
            pulse = max(pulse - R, m)

        minute += 1
    print(minute if ex_minute == N else -1)