alphabet_cnt = [0]*26 # 알파벳 갯수를 담는 배열

S = input()
for i in S:
    alphabet_cnt[ord(i)-65] += 1

odd_cnt = 0
odd_idx = 0
for j in range(26):
    if alphabet_cnt[j] % 2 == 1:
        odd_cnt += 1
        odd_idx = j

if odd_cnt > 1:
    print("I'm Sorry Hansoo")
    quit()

ans_front = ""
for k in range(26):
    ans_front += chr(k+65)*(alphabet_cnt[k]//2)
ans_back = ans_front[::-1]

if odd_cnt == 1:
    ans_front += chr(odd_idx+65)

print(ans_front+ans_back)