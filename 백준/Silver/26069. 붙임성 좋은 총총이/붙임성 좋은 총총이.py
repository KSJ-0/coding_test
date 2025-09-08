import sys
input = sys.stdin.readline

N = int(input().strip())
dancing = {"ChongChong"}

for _ in range(N):
    p1, p2 = input().split()

    if p1 in dancing or p2 in dancing :
        dancing.add(p1)
        dancing.add(p2)

print(len(dancing))    