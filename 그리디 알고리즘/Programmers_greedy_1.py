def solution(n, lost, reserve):

    reserve_o = set(reserve) - set(lost)
    lost_o = set(lost) - set(reserve)

    for i in reserve_o:
        f = i - 1
        b = i + 1
        if f in lost_o:
            lost_o.remove(f)
        elif b in lost_o:
            lost_o.remove(b)
    return n - len(lost_o)
