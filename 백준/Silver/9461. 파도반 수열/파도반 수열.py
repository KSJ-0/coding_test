import sys
t = int(sys.stdin.readline().strip())
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    if len(p) >= n:
        print(p[n-1])
    else:
        while len(p)<=n:
            present = p[len(p)-5] + p[len(p)-1]
            p.append(present)
        print(p[n-1])
