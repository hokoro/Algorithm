answer = 0
train_guest = 0
for i in range(4):
    getout,getin = map(int,input().split())
    train_guest = train_guest - getout + getin
    if train_guest > answer:
        answer = train_guest


print(answer)