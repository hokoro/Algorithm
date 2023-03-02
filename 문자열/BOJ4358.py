import sys

input = sys.stdin.readline

tree_dict = dict()
count = 0
while True:
        name = input().rstrip()
        if not name:
            break
        tree_dict[name] = tree_dict.setdefault(name, 0) + 1
        count += 1


names = sorted(list(tree_dict.keys()))

for na in names:
    num = "{:.4f}".format(tree_dict[na] / count*100,4)
    print(f'{na} {num}')