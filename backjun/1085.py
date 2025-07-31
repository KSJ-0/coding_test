import sys
x, y, w, h = list(map(int,sys.stdin.readline().split()))

num = []
num.append(y)
num.append(w-x)
num.append(h-y)

least = num[0]
for i in num:
    if least>i:
        least=i

print(least)