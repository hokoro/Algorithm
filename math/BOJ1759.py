import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alphas = list(map(str, sys.stdin.readline().split()))

alphas_combination = list(combinations(alphas, L))
vowel = ['a', 'e', 'i', 'o', 'u']
strs = []
for alpha in alphas_combination:
    alpha = list(set(alpha))
    alpha.sort()
    vowel_count = 0
    not_vowel_count = 0
    token = ''
    for al in alpha:
        if al in vowel:
            vowel_count += 1
            token += al
        else:
            not_vowel_count += 1
            token += al

    if vowel_count >= 1 and not_vowel_count >= 2:
        strs.append(token)

strs.sort()

for s in strs:
    print(s)


