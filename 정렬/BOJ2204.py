import sys

input = sys.stdin.readline

while True:
    num = int(input())

    if num == 0:
        break

    words = {}
    for _ in range(num):
        sentence = input()
        sentence = sentence.replace('\n', '')
        sentence_ = sentence.upper()
        words[sentence_] = sentence

    keys_ = sorted(list(words.keys()))
    print(words[keys_[0]])