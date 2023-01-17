from collections import deque


def solution(numbers, direction):

    if direction == "right":
        numbers.insert(0,numbers.pop())

    if direction == "left":
        numbers.append(numbers.pop(0))

    return numbers

solution([1,2,3],"right")